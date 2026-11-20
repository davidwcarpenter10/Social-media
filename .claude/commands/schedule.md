---
description: Schedule an approved post pack in Blotato
argument-hint: <pack path or "all approved"> [platforms] [post now]
---

Schedule: $ARGUMENTS

1. Confirm the user has explicitly approved this pack (and which platforms) in this conversation.
   If not, show the pack summary and ask for approval — stop here.
2. Show the target Blotato accounts (from `playbook/blotato-config.md`) and the planned times; get a yes.
3. Delegate to `blotato-scheduler` with the pack path, approved platforms, the approver's name, and whether "post now" was said.
4. Show the returned table: platform | date/time ET | format | ID | status.
