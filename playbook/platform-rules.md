# Platform Rulebook (hard limits are enforced by tools/qa_check.py)

## Facebook — Page "HonorCraft Laser Work"
- Hook in the first 125 characters. Warm, full sentences.
- 0–3 hashtags.
- Product link goes in `firstComment` (clickable there).
- Video only as a Reel (`mediaType: reel`).
- Limits: text ≤ 63,206 chars; Reel caption ≤ 2,200.
- Cadence: 3–4 / week.

## Instagram — @honorcraftlw
- Caption ≤ 2,200 chars, hook in the first 125.
- **Max 5 hashtags (hard).**
- Alt text always.
- Carousel: 2–10 images, 4:5, 1080×1350 (omit mediaType). Reel: 9:16 (`mediaType: reel`, `shareToFeed: true`, `coverImageUrl`).
- Links are not clickable: "link in bio" or "Comment ENGRAVE for the link".
- Cadence: 4–5 / week, at least 2 Reels.

## TikTok — @honorcraftlw
- Caption ≤ 2,200 (API); aim for 100–300 chars with search keywords. 3–5 hashtags.
- 1-second on-screen hook + text beats (most people watch muted).
- Photo post title ≤ 90 chars, `autoAddMusic: true`.
- Links not clickable.
- Flags: `privacyLevel: PUBLIC_TO_EVERYONE`, `isYourBrand: true`, `isBrandedContent: false`,
  `disabledComments/Duet/Stitch: false`, `isAiGenerated: true` if any AI media.
- Trending-sound plan: `isDraft: true` and tell David to add the sound in the app.
- Cadence: 4–7 / week.

## YouTube Shorts
- Title required, ≤ 100 chars (aim ≤ 60, keyword first).
- Description ≤ 5,000 **bytes** (UTF-8) including `#Shorts`.
- Tags ≤ 500 chars total.
- Video ≤ 3 min, vertical 9:16.
- Links not clickable in Shorts: point to the pinned comment or channel.
- `privacyStatus: public`, `shouldNotifySubscribers: true`, `isMadeForKids: false`,
  `containsSyntheticMedia` per pack, add to Products playlist.
- Cadence: 2–4 / week.

## Shared video spec
- One 1080×1920 master, 15–35 s, for Reels / TikTok / Shorts.
- Safe zone: keep text clear of the top 220 px and bottom 380 px.
- Motion or the finished product in the first 2 seconds.
- H.264 MP4.
