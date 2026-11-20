---
description: Build a QA-checked post pack for one product across FB, IG, TikTok and YouTube using the agent team
argument-hint: <product link | path to brief.md>
---

Build a post pack for: $ARGUMENTS

1. **Brief** — if a brief.md path was given, use it. Otherwise create the pack folder
   `content/post-packs/<today>_<slug>/` and delegate to `content-strategist` for a single brief.
2. **Intel** — delegate to `product-intel` with the product link and pack path. If it returns blocking UNKNOWNs, ask the user once.
3. **Create (parallel)** — in ONE message launch `facebook-writer`, `instagram-writer`, `tiktok-writer`,
   `youtube-writer` and `visual-director`, each given the pack path.
4. **QA** — delegate to `qa-compliance` with the pack path. If FAIL needs human input, ask; then re-run QA.
5. **Report** — hook per platform, the shot list, QA result, anything David must film or confirm.
   End with: "Reply **approve** (or approve specific platforms) to schedule in Blotato."

Never call Blotato write tools in this command.
