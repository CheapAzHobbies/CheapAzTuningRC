# Trackside Shop

A mobile-friendly parts catalog for the QR code on the track. People browse on their phone, find something they want, then pay cash in person — this page doesn't do checkout or payments, it's just a browsable list.

## How to add a product

Open [`products.json`](products.json) and add a new entry (copy an existing one and edit it):

```json
{
  "id": "unique-short-slug",
  "name": "Traxxas 2075 Waterproof Servo",
  "brand": "Traxxas",
  "partNumber": "2075",
  "category": "Servos",
  "scale": "1/10",
  "price": 18,
  "condition": "New",
  "qty": 2,
  "photo": "images/electronics_traxxas_servo_2075.jpg",
  "notes": "Short description — condition, what it fits, why it's a good deal."
}
```

| Field | Notes |
|---|---|
| `id` | Unique, lowercase, dashes — used internally, never shown |
| `name` | Full product name |
| `brand` | `Traxxas`, `Generic`, etc. — leave blank if unknown |
| `partNumber` | Manufacturer part #, blank if none |
| `category` | Start with: `Servos`, `Wheels & Tires`, `Screws & Hardware`, `Electronics`, `Traxxas Parts`, `Other`. Add a new category any time — the filter row picks it up automatically |
| `scale` | `1/8`, `1/10`, `1/12`, `1/16`, `1/18`, `1/24`, `Universal` (fits multiple / not scale-specific) |
| `price` | Number, no `$` |
| `condition` | `New`, `Used - Like New`, `Used - Good`, `Used - Fair` |
| `qty` | How many you have. `0` shows as "sold out" |
| `photo` | Path to the image, relative to this folder (see below) |
| `notes` | 1-2 sentences: condition detail, fitment, why it's a deal |

The page (`index.html`) reads this file automatically — no HTML editing needed. Category and scale filters build themselves from whatever values appear in `products.json`.

## Adding photos

Drop the image in [`images/`](images/) and point `photo` at it, e.g. `images/servo_2075.jpg`. Until you have a real photo, leave it as `images/placeholder.svg` — the page shows a "photo needed" placeholder card instead of a broken image.

## Publishing (GitHub Pages)

One-time setup, does not need to be redone per product:

1. On GitHub: **Settings → Pages**
2. Under **Build and deployment → Source**, choose **Deploy from a branch**
3. Branch: **main**, folder: **/ (root)**
4. Save. GitHub will publish the whole repo; this shop will be live at:

   `https://cheapazhobbies.github.io/CheapAzTuningRC/shop/`

   (First deploy takes a minute or two. Every push to `main` re-deploys automatically.)

## QR code

Once Pages is live, generate a QR code pointing at that URL (any free QR generator works, e.g. `https://www.qr-code-generator.com/` or `qrcode.show/<url>`) and print it for the track. The page is filter-friendly on mobile, so it's fine to link the plain shop URL rather than a specific category.

## Notes

- Cash-only banner and contact info live at the top of `index.html` — edit that text directly if your terms change.
- This is a static catalog, not a store: no cart, no online payment. That's intentional — keeps it simple and avoids any payment-processing overhead for a cash trackside setup.
