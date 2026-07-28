# Local AI Agent Setup (aider + Ollama)

Self-hosted agent to do the same repo work Claude Code does: bring a part photo plus context, it fills in the correctly formatted row and commits. Runs entirely on local hardware, no API cost.

**Target machine:** X399 Taichi, Threadripper 1950X, **RX 9060 XT 16 GB (RDNA4, gfx1200)**, 128 GB RAM.

> Everything in this folder is config and docs. The actual models run via Ollama, and aider drives the edits. Config lives here; launch aider from the repo root pointing at these files (see step 6).

---

## What runs where

| Piece | Choice | Why |
|---|---|---|
| Coder model | `qwen2.5-coder:32b` (Q4, ~19 GB) | 32B is the tier that handles aider edits cleanly. Fits with a little CPU offload; the 128 GB RAM makes that painless |
| Vision model | `qwen2.5vl:7b` | Reads part photos, transcribes scale/caliper values |
| Editor | aider, `edit-format: whole` | Whole-file rewrites are far more reliable for local models than SEARCH/REPLACE diffs (the format that made the earlier Ollama mess) |
| Conventions | `CLAUDE.md` (repo root) | Loaded read-only so the model formats rows the repo's way |

---

## Step by step

### 1. Install ROCm 7.x (AMD GPU driver + compute stack)

The RX 9060 XT (gfx1200) is officially supported in **ROCm 7.0.2+**. On Linux, RDNA4 works well now.

Ubuntu/Debian (adapt version/codename from AMD's current [ROCm quick-start](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/)):

```bash
sudo apt update
# grab the latest amdgpu-install .deb from AMD's ROCm page, then:
sudo apt install ./amdgpu-install_*.deb
sudo amdgpu-install --usecase=rocm
sudo usermod -aG render,video $USER
sudo reboot
```

Verify after reboot:

```bash
rocminfo | grep -i gfx      # should show gfx1200
rocm-smi                    # should list the RX 9060 XT with VRAM
```

### 2. Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Use **Ollama 0.30.6 or newer** (native RDNA4 support, no DLL/override hacks). Check with `ollama --version`.

### 3. Set environment (add to `~/.bashrc`)

```bash
export OLLAMA_API_BASE=http://127.0.0.1:11434
export OLLAMA_CONTEXT_LENGTH=32768        # server-side context; analysis docs + CLAUDE.md are big
# Only if the GPU is NOT detected on an older ROCm:
# export HSA_OVERRIDE_GFX_VERSION=12.0.0
```

Then restart the Ollama service (or `ollama serve` in a terminal).

### 4. Pull the models

```bash
ollama pull qwen2.5-coder:32b
ollama pull qwen2.5vl:7b
```

Sanity check the GPU is actually used (watch `rocm-smi` in another terminal while this runs):

```bash
ollama run qwen2.5-coder:32b "write a one-line hello"
```

### 5. Install aider

```bash
python3 -m pip install --upgrade aider-chat
# or, isolated: pipx install aider-chat
```

### 6. Launch aider (from the repo root)

```bash
cd /path/to/CheapAzTuningRC
aider \
  --config local-ai/aider.conf.yml \
  --model-settings-file local-ai/aider.model.settings.yml
```

The config points aider at Ollama, loads `CLAUDE.md` as conventions, uses whole-file edits, and auto-commits.

---

## The photo workflow

Plain aider expects one model, so vision plus editing is a two-step flow:

1. Describe the pic with the vision model:
   ```bash
   ollama run qwen2.5vl:7b "Identify this RC part, brand, and any part number or scale reading." < /path/to/photo.jpg
   ```
   (or use aider's `/add photo.jpg` if you launch aider on the vision model instead)
2. Paste that description into aider as context and tell it which `<part>_analysis.md` to update. The coder model writes the formatted row per `CLAUDE.md`.

A tighter one-command pipeline can come later; start with the two-step to confirm the pieces work.

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| Ollama falls back to CPU (0 VRAM used) | Confirm ROCm 7.0.2+ and Ollama 0.30.6+. Set `HSA_OVERRIDE_GFX_VERSION=12.0.0`. Check `rocm-smi` shows the card |
| "Context silently discarded" / model forgets | Raise `OLLAMA_CONTEXT_LENGTH` and `num_ctx` in `aider.model.settings.yml` |
| Out of memory loading 32B | Lower `num_ctx` to 16384, or drop to `qwen2.5-coder:14b` (fits fully in 16 GB) |
| aider makes malformed edits | Keep `edit-format: whole`; do not switch to `diff` on a local model |
| Model ignores repo formatting | Confirm `CLAUDE.md` is in the `read:` list and you launched from the repo root |

---

## Files in this folder

- `aider.conf.yml` — main aider config (model, whole edits, auto-commit, conventions)
- `aider.model.settings.yml` — sets the model context window (`num_ctx`)
- `README.md` — this guide
