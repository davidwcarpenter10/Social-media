# HonorCraft Social Content Agent

A multi-agent Claude Code team that **plans, creates, QA-checks and schedules** social content for
HonorCraft on Facebook, Instagram, TikTok and YouTube Shorts, publishing through **Blotato**.

## The team (`.claude/agents/`)
| Agent | Job |
|---|---|
| `content-strategist` | Weekly calendar, pillar mix, audience, occasions, 3 hook angles per product |
| `product-intel` | Verifiable facts from Shopify / Etsy (price, options, materials, photos) |
| `facebook-writer` · `instagram-writer` · `tiktok-writer` · `youtube-writer` | Platform-native copy, run in parallel |
| `visual-director` | Phone shot list, 9:16 master spec, carousels, Canva / Blotato slideshows from real photos |
| `qa-compliance` | Hard limits via `tools/qa_check.py`, fact check, brand guardrails — blocks until PASS |
| `blotato-scheduler` | Uploads media and schedules via Blotato — **only after human approval** |
| `performance-analyst` | Weekly analytics scorecard, drafted replies, playbook updates |

The orchestrator (main Claude session, instructions in `CLAUDE.md`) routes work between them.

## Usage
Open this repo in Claude Code (CLI, desktop, or claude.ai/code) with the Blotato, Shopify and Canva connectors on.

```
/plan-week                                   # calendar + briefs for next week
/create-pack https://honorcraftlw.com/products/...   # one product → QA-checked pack
/run-week <links>                            # plan + build every pack for the week
approve                                      # you approve
/schedule content/post-packs/2026-11-24_flag-case   # schedule in Blotato
/review                                      # weekly performance review
```

## Layout
```
CLAUDE.md                 orchestrator rules and pipeline
.claude/agents/           the 10 specialist agents
.claude/commands/         slash commands
playbook/                 brand voice, platform limits, Blotato config, pack template (source of truth)
tools/qa_check.py         hard-limit validator for posts.json
content/calendars/        weekly plans
content/post-packs/       one folder per product pack
content/scorecards/       weekly reviews
```

## Safety gates
Nothing is published without explicit approval from David or Lisa. QA PASS is required, the scheduler re-validates
with `--strict` (no placeholder media), and posts default to future scheduled times.
