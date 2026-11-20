# Blotato Publishing Config

Always call `blotato_list_accounts` first and prefer live values if these drift.

| Platform | accountId | Extra required |
|---|---|---|
| Facebook | 53000 | pageId `370318706175109` (HonorCraft Laser Work) |
| Instagram | 72147 | mediaType `reel` for Reels; omit for carousel |
| TikTok | 60345 | privacyLevel, disabledComments, disabledDuet, disabledStitch, isBrandedContent, isYourBrand, isAiGenerated |
| YouTube | 50377 | title, privacyStatus, shouldNotifySubscribers; Products playlist `PLzmhjKCSrFwpTAOsA9OMEhkf5Wrs3jIEI` |

Verified 2026-11-20.

## Time slots (America/New_York, ISO 8601 with offset, odd minutes)
- Facebook: Tue–Thu 12:15p / 7:10p, Sat 9:20a
- Instagram: weekdays 11:40a / 7:25p
- TikTok: Tue–Sat 6:45p–9:00p
- YouTube: 3:10p or 6:20p
- Stagger the same product 1–2 days apart across platforms.
- Check `blotato_list_schedules` to avoid double-booking. `useNextFreeSlot` if David prefers his queue.

## Media
- Every mediaUrl must be public. Local files → `blotato_create_presigned_upload_url` then HTTP PUT; temp URLs → `blotato_upload_media`.
- Slideshow from real photos: `blotato_create_design` with template
  `/base/v2/image-slideshow/5903b592-1255-43b4-b9ac-f8ed7cbf6a5f/v1`, poll `blotato_get_design_status`.
  Check `blotato_get_credits` first.

## Common failures
Non-public URL · wrong aspect ratio · non-H.264 video · IG > 5 hashtags · carousel > 10 items.

## Automations (only with David's OK)
IG/FB comment-keyword DM: keyword `ENGRAVE` → DM with product link (`blotato_create_automation`).
