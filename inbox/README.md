# Inbox

Dropzone for files (images, screenshots, order receipts, anything) that need to be sorted into the right place but you didn't have a chance to route manually.

> **Workflow:** drop files in here → tell Claude "check inbox" (or describe what you dropped) → Claude inspects each file, figures out what it is, and moves/copies it to the correct location with the correct naming.

---

## What can go in here

- **Part photos** — Claude renames them per [CONTRIBUTING.md image scheme](../CONTRIBUTING.md#image-naming-convention) and drops them in the right `cars/<CarName>/src/` folder
- **Order receipts / cart screenshots** — Claude reads the price + part info and adds a row to the relevant `Deals/<file>.md` or `<part>_analysis.md` Price History section
- **Random screenshots / spec sheets / PDFs** — Claude reads them and routes the info into the right car README section (Suspension, Drivetrain, etc.) or analysis doc
- **3D models** — Claude moves to the right `cars/<CarName>/3d-models/` folder

---

## After routing

Claude **deletes the file from `inbox/`** after the info has been captured into the destination (the source file lives on in the destination as the renamed image, or its content is preserved in the relevant `.md`). Keep originals in your Downloads / phone if you need them.

If a file can't be confidently routed, Claude leaves it in `inbox/` and asks you what to do with it.

---

## Notes

- File names don't matter here — drop them with whatever name your device gave them. Claude renames on the way out.
- Multiple files in one drop is fine — Claude processes them in batch.
- Don't commit large numbers of files at once on slow connections; the sandbox repo is git-tracked, so big batches push slowly.
