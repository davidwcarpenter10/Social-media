# Post Pack Template

Folder: `content/post-packs/YYYY-MM-DD_<product-slug>/`

## brief.md  (content-strategist)
```
Status: BRIEF | DRAFT | QA-PASS | APPROVED | SCHEDULED
Product: <name> — <link>
Audience: <one of 4>
Occasion / gift moment:
Pillar:
Core message (1 sentence):
Hook angles:
  A:
  B:
  C:
Assignment: FB=<A|B|C> IG=<> TikTok=<> YT=<>
Target dates: FB <date> · IG <date> · TikTok <date> · YT <date>
```

## intel.md  (product-intel)
Title · price · compare-at · variants/options · materials · dimensions · personalization ·
processing time · image URLs · other-marketplace link · UNKNOWN list · sources.

## <platform>.md  (writers)
Final copy, the hook, hashtags, alt text / title / tags as applicable, CTA, and a char count line.

## visuals.md  (visual-director)
Format per platform, numbered shot list, text overlays with timings, carousel order, media URLs,
AI-media flag decision.

## posts.json  (writers + visual-director; consumed by qa_check.py and blotato-scheduler)
```json
{
  "pack": "2026-11-24_flag-case",
  "aiMedia": false,
  "posts": [
    {"platform": "facebook",  "accountId": "53000", "scheduledTime": "", "content": {"text": "", "mediaUrls": [], "firstComment": ""}, "target": {"pageId": "370318706175109", "mediaType": null}},
    {"platform": "instagram", "accountId": "72147", "scheduledTime": "", "content": {"text": "", "mediaUrls": [], "altText": ""}, "target": {"mediaType": "reel", "shareToFeed": true, "coverImageUrl": ""}},
    {"platform": "tiktok",    "accountId": "60345", "scheduledTime": "", "content": {"text": "", "mediaUrls": []}, "target": {"privacyLevel": "PUBLIC_TO_EVERYONE", "disabledComments": false, "disabledDuet": false, "disabledStitch": false, "isBrandedContent": false, "isYourBrand": true, "isAiGenerated": false}},
    {"platform": "youtube",   "accountId": "50377", "scheduledTime": "", "content": {"text": "... #Shorts", "mediaUrls": []}, "target": {"title": "", "tags": [], "privacyStatus": "public", "shouldNotifySubscribers": true, "isMadeForKids": false, "containsSyntheticMedia": false, "playlistIds": ["PLzmhjKCSrFwpTAOsA9OMEhkf5Wrs3jIEI"]}}
  ]
}
```
Media URLs may be `TODO:<shot-id>` until footage exists; QA reports them as warnings, the scheduler blocks on them.

## qa.md  (qa-compliance)
Checklist result per platform, fixes made, final `RESULT: PASS` or `RESULT: FAIL — <reasons>`.

## schedule.md  (blotato-scheduler)
| platform | date/time ET | format | postSubmissionId | status |
