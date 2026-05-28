#!/usr/bin/env python3
"""
Image search + downloader for filling in 'Need image' placeholders in analysis docs.

TWO MODES:

1) SEARCH MODE -- uses DuckDuckGo Images (not Google -- Google aggressively
   blocks scrapers and requires a paid API at scale; DuckDuckGo is more
   permissive). NOTE: DuckDuckGo can still rate-limit / block requests from
   data-center IPs; works reliably from a normal home/desktop connection.

2) URL MODE -- you paste a list of image URLs (one per line) and the script
   downloads them. More reliable than search since you control what comes in.
   Best workflow: open a browser, search Google/Bing Images yourself, right-
   click 'Copy image address' on the ones you want, paste into a text file,
   feed it to this script.

Usage:
    # SEARCH MODE: top 5 results to /tmp/img_picks/
    python tools/image_search.py search "Castle 1415 2400KV motor"

    # SEARCH MODE: specify output + count + filename prefix
    python tools/image_search.py search "Tekin Pro4 HD 2500KV" \\
        --out cars/FastAzJato4x4/src --prefix electronics_tekin_pro4_hd_2500kv --count 3

    # URL MODE: download URLs listed in a text file
    python tools/image_search.py urls urls.txt --out /tmp/picks --prefix castle_1415

    # URL MODE: read URLs from stdin
    echo "https://example.com/foo.jpg" | python tools/image_search.py urls - \\
        --out cars/FastAzJato4x4/src --prefix electronics_castle_1415_2400kv

Recommended workflow when SEARCH mode is rate-limited:
    1. Open the manufacturer / retailer product page in a browser
       (Tekin, Castle, Hobbywing, AMain, Tower, eBay, AliExpress)
    2. Right-click the product image, 'Copy image address'
    3. Paste URLs into a text file, one per line
    4. Run URL MODE on that file

Install once:
    pip install ddgs

Notes:
    - Some image hosts (alicdn.com, some retailer CDNs) are blocked by the
      env network policy and will fail to download. The script keeps going.
    - For RC parts specifically, going straight to a retailer/manufacturer
      product page usually gives better-quality official product shots than
      any search result.
"""

import argparse
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

try:
    from ddgs import DDGS
except ImportError:
    try:
        # legacy fallback for the older package name
        from duckduckgo_search import DDGS
    except ImportError:
        print("missing dependency: pip install ddgs", file=sys.stderr)
        sys.exit(1)


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "image/avif,image/webp,image/png,image/jpeg,image/*;q=0.8",
}


def safe_ext(url: str) -> str:
    """Guess a file extension from the URL; default to .jpg."""
    tail = url.split("?")[0].split("#")[0].lower()
    for ext in ("jpg", "jpeg", "png", "webp", "avif", "gif"):
        if tail.endswith("." + ext):
            return ext
    return "jpg"


def download(url: str, dest: Path, timeout: int = 15) -> bool:
    """Download a single URL to dest. Returns True on success."""
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
        if len(data) < 1024:
            print(f"  skip (too small, likely an error page): {url}")
            return False
        dest.write_bytes(data)
        return True
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        print(f"  fail: {url} -- {e}")
        return False
    except Exception as e:
        print(f"  fail: {url} -- {type(e).__name__}: {e}")
        return False


def search_and_download(
    query: str,
    out_dir: Path,
    count: int = 5,
    prefix: str | None = None,
) -> int:
    """Search DuckDuckGo images and download the top results."""
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"searching DuckDuckGo Images: {query!r}")
    results = []
    backoffs = [0, 3, 8, 20]
    for attempt, backoff in enumerate(backoffs):
        if backoff:
            print(f"  rate-limited, waiting {backoff}s before retry ({attempt}/{len(backoffs) - 1})...")
            time.sleep(backoff)
        try:
            with DDGS() as ddgs:
                results = list(ddgs.images(query, max_results=count * 3))
            break
        except Exception as e:
            msg = str(e)
            if "ratelimit" in msg.lower() or "rate limit" in msg.lower():
                if attempt < len(backoffs) - 1:
                    continue
            print(f"search failed: {type(e).__name__}: {e}")
            return 0

    if not results:
        print("no results")
        return 0

    saved = 0
    name_base = prefix or query.lower().replace(" ", "_")[:50]

    for r in results:
        if saved >= count:
            break
        url = r.get("image")
        if not url:
            continue
        ext = safe_ext(url)
        dest = out_dir / f"{name_base}_{saved + 1:02d}.{ext}"
        print(f"trying {url}")
        if download(url, dest):
            saved += 1
            size_kb = dest.stat().st_size // 1024
            print(f"  -> {dest} ({size_kb} KB)")

    print(f"\ndone: saved {saved}/{count} to {out_dir}")
    return saved


def main() -> None:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("query", help="search query (e.g. 'Castle 1415 2400KV motor')")
    p.add_argument(
        "--out",
        default="/tmp/img_picks",
        help="output folder (default: /tmp/img_picks)",
    )
    p.add_argument(
        "--count",
        type=int,
        default=5,
        help="number of images to download (default: 5)",
    )
    p.add_argument(
        "--prefix",
        default=None,
        help="filename prefix (default: derived from query)",
    )
    args = p.parse_args()

    saved = search_and_download(
        args.query,
        Path(args.out),
        count=args.count,
        prefix=args.prefix,
    )
    if saved == 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
