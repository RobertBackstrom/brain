---
name: Deliverables go in project GDrive folder
description: Always upload client deliverables to a Deliverables subfolder inside the project's own GDrive folder, not the general Deliverables folder. Create the subfolder if it doesn't exist.
type: feedback
---

Always upload client docs/deliverables to a Deliverables subfolder within the project's GDrive folder. Create the folder if it doesn't exist.

**Why:** Each project has its own GDrive folder (linked in the project memory). Deliverables need to live there so they're organized per-client, not dumped into a general bucket.

**How to apply:** Before uploading, check the project memory for the GDrive folder ID. Look for a Deliverables subfolder inside it. If none exists, create one with `--create-folder "Deliverables" <project-folder-id>`, then upload into it.
