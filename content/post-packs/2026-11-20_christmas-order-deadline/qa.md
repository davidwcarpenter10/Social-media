# QA: Christmas order-by deadline

QA & Compliance, 2026-11-20. Source of truth: `posts.json`. intel.md "Owner decisions" and "Owner confirmations" (David, 2026-11-20) override earlier intel.

**Update (QA pass 2, 2026-11-20):** David confirmed that all three ornaments are live on Etsy, that the Memorial Ornament has no insignia, and the Etsy prices (Jewelry Box $20, $15 per ornament). The Etsy prices are back in the FB and IG captions, and the jewelry box color list is gone from FB. Questions 1-3 are resolved.

## Pack-level
- ✅ posts.json was checked against the four `posts.<platform>.json` fragments and `visuals.json`: all identical, and aiMedia matches. The fragments and visuals.json were then deleted as redundant.
- ✅ .md copy is identical to posts.json for: FB text and firstComment, IG hook, caption and alt text, TikTok caption, YT description, title and tags. This was checked by script.
- ✅ Featured products are only B (Travel Jewelry Box), D (Memorial Ornament), E (Baby First Christmas Ornament) and F (Dog Memorial Ornament). There is no pet stone and no wallet.
- ✅ Order-by wording follows the owner decision: "Order by Sunday, Dec 13 for Christmas delivery". On screen it reads "Order by Sun, Dec 13 / for Christmas delivery". Dec 13, 2026 is a Sunday. No per-item processing days are stated anywhere.
- ✅ aiMedia is false. TikTok `isAiGenerated` is false and YT `containsSyntheticMedia` is false, which matches. The plan uses real footage only.
- ✅ Schedule slots match blotato-config: FB Tue 11/24 12:15p, IG Wed 11/25 7:25p, TikTok Fri 11/27 7:05p, YT Sun 11/29 6:20p. The posts are 1-2 days apart.
- ✅ Prices are now consistent. FB and IG use the Etsy prices David confirmed: Jewelry Box $20 and $15 for each ornament. TikTok, YT and the on-screen text stay price-free. The CTA points to Etsy, so the posts follow Etsy, not Shopify.

## Facebook (Reel, angle A)
- ✅ Limits: 1118 chars out of the 2,200 allowed for a Reel. 3 hashtags. pageId is correct. The link is in firstComment.
- ✅ Hook is in the first 125 chars (124): "Custom takes time. Order by Sunday, Dec 13 for Christmas delivery..."
- ✅ Angle A (honest deadline). There is no countdown or scarcity language, and the stock of 1 per color is not mentioned.
- ✅ Facts: the jewelry box lid engraving (name, monogram, date, quote) comes from the listing. The ornaments are described as wood with a name or personalization, which matches intel. The price lines are Jewelry Box $20, Memorial $15, Baby First Christmas $15 and Dog Memorial $15, all Etsy prices confirmed by David.
- ✅ CTA "Link to our Etsy shop in the first comment" suits FB, where the comment link is clickable.
- ✅ Guardrails 1-9: no uniform or rank, no insignia, no "official" wording, no Made in USA claim, no customer names, no Foundation mention. Brand name is "HonorCraft" only.
- ❌→✅ **Fixed:** pass 1 removed the Shopify prices. Pass 2 put back the Etsy prices David confirmed (guardrail #6).
- ❌→✅ **Fixed (pass 2):** removed the color list (Light Blue, Burgundy, Seafoam, Blue Matte, Pink). Those colors are confirmed on Shopify only, not on Etsy.

## Instagram (Reel, angle C)
- ✅ Limits: 659 chars, 5 out of 5 hashtags, alt text included. The Reel has 1 media item and shareToFeed is true. coverImageUrl is `TODO:cover`.
- ✅ Hook is in the first 125 chars (122): "The paper comes off. / They read the name, the date, the words you chose. / The gift they keep long after the tree comes down."
- ✅ Angle C (Christmas-morning reveal). The caption is not a copy of the FB caption.
- ✅ Guardrails: "Veteran-owned. Engraved in Ohio." is approved wording. Nothing else is flagged.
- ❌→✅ **Fixed:** pass 1 removed the Shopify prices. Pass 2 put back the Etsy prices: Jewelry Box $20 and $15 for each ornament.
- ❌→✅ **Fixed:** the CTA was "Comment ENGRAVE for the link, or tap the link in bio...". It is now "Tap the link in bio for our Etsy shop." The ENGRAVE comment-to-DM automation does not exist. Adding it later is optional and needs David's OK (noted in instagram.md).
- ❌→✅ **Fixed:** the alt text described a red-and-green wrapping-paper unwrap that is not in the shot plan. It was rewritten to follow visuals.md shots 1-7 and the section 3 overlays (807 chars).

## TikTok (video, angle B)
- ✅ Limits: 295 chars (target 100-300), 4 hashtags (3-5 allowed). All required flags are correct.
- ✅ On-screen hook "Why custom gifts need a head start" is 7 words (limit 8), with the laser moving in the first second (visuals.md shot 1).
- ✅ The caption covers the search keywords: personalized Christmas gift, custom engraved gift, #laserengraving.
- ✅ CTA "Link in bio" works for TikTok, where links are not clickable.
- ✅ No prices. The sample name is staged.
- ❌→✅ **Fixed (consistency):** the text-beat table in tiktok.md differed from the shared master overlays in visuals.md. I added a note to tiktok.md saying the visuals.md section 3 overlays are final and the table is the original draft. The hook and end card already matched.

## YouTube Shorts (angle B, different cut)
- ✅ Title "Custom Christmas Gift: How Long It Really Takes" is 47 chars and starts with the keyword.
- ✅ The description is 404 bytes and includes #Shorts. Tags total 299 chars. public, notify subscribers, isMadeForKids false and the Products playlist are all set.
- ✅ CTA "Link in the pinned comment" suits Shorts. The pinned comment is in youtube.md, and David pins it by hand.
- ✅ The copy does not repeat TikTok. The title, description and pinned comment are all different.
- ❌→✅ **Fixed (consistency):** the beats suggested in youtube.md differed from the single master. I added a note that they apply only if the editor makes the optional YT alternate cut (visuals.md section 1). Otherwise the Short uses the master overlays.
- ⚠️ If the alternate cut is not made, YT and TikTok carry the same video. That is acceptable because both are angle B and the copy differs, but the alternate cut is preferred.

## Visuals (visuals.md)
- ✅ Shots are hands only, with no uniform, insignia or real customer data. The safe zones are specified. There are no prices or day counts on screen.
- ❌→✅ **Fixed:** the overlay "Then we laser it, one at a time" made an unverified process claim ("one at a time"). It now reads "Then it goes on the laser".
- ✅ The Memorial Ornament insignia check is RESOLVED. David confirmed there is no insignia. visuals.md section 4 is marked resolved and the listing photos are cleared for the fallback slideshow.

## Fixes made
1. **Prices (pass 1): removed from FB and IG** (facebook.md, instagram.md, posts.json). The CTA points to Etsy, the Etsy prices are UNKNOWN, and guardrail #6 says price must match the live listing. TikTok, YT and the on-screen text already left prices out. In pass 2, the prices went back in using the Etsy prices David confirmed (Jewelry Box $20, ornaments $15 each). The colors were dropped from FB.
2. IG CTA changed to "link in bio" only.
3. IG alt text rewritten to match the visuals.md shot plan.
4. Notes added to tiktok.md and youtube.md saying the visuals.md overlays are final for the shared master.
5. visuals.md overlay softened to "Then it goes on the laser".
6. Char counts, fact-source notes and payload references updated in the .md files.
7. `posts.facebook.json`, `posts.instagram.json`, `posts.tiktok.json`, `posts.youtube.json` and `visuals.json` deleted after checking they match posts.json.
8. brief.md Status changed to QA-PASS.
9. Pass 2: in visuals.md, the insignia check is marked RESOLVED and the HOLD on both Memorial Ornament listing photos is removed. The fact notes in facebook.md and instagram.md are updated, and posts.json is re-synced. A script check confirms the .md copy matches posts.json on all 4 platforms.

## qa_check.py output (final run)
```
WARN    [facebook] media placeholder TODO:master-video
WARN    [instagram] media placeholder TODO:master-video
WARN    [tiktok] media placeholder TODO:master-video
WARN    [youtube] media placeholder TODO:master-video

0 error(s), 4 warning(s) -> PASS
```
Exit code 0. The IG `coverImageUrl: TODO:cover` is also a placeholder, but the script does not check that field.

## Warnings: the scheduler blocks on these, copy QA does not
- `TODO:master-video` on all 4 posts and `TODO:cover` on IG. Footage is not filmed yet. David needs to film shots 1-7 by Mon 11/23.
- The Etsy listings (Q2) and the insignia check (Q3) are now resolved. Only the footage and the cover still block scheduling.

## Questions for David
1. ✅ RESOLVED (Etsy prices: Jewelry Box $20, ornaments $15). Was: **Etsy prices:** are the Etsy prices the same as Shopify (Jewelry Box $20.00, Memorial Ornament $13.00, Baby First Christmas $15.00, Dog Memorial $15.00), and are the jewelry box colors the same? If yes, QA can put the prices back in the FB and IG captions.
2. ✅ RESOLVED (all three ornaments are live on Etsy, so the Etsy CTA stands). Was: **Etsy listings:** are the Memorial Ornament, Baby First Christmas Ornament and Dog Memorial Ornament live in the Etsy shop? If not, should the CTA point to honorcraftlw.com, or should the ornaments come out of the posts?
3. ✅ RESOLVED (no insignia, photos cleared). Was: **Insignia:** does the Memorial Ornament (tagged "Military") show any branch emblem, seal or insignia? Whatever the answer, the piece you film must have none.
4. **Footage:** the shots 1-7 master video and the IG cover still are needed by Mon 11/23.
5. **New:** Shopify lists the Memorial Ornament at $13.00, but Etsy has it at $15. Is this intentional, or should one of the listings be updated? This is not blocking, because the posts use Etsy.
6. (Optional) Do you want the IG/FB "ENGRAVE" comment-to-DM automation set up later?

RESULT: PASS
