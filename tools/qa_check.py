#!/usr/bin/env python3
"""Hard-limit checker for HonorCraft post packs (posts.json).

Usage: python3 tools/qa_check.py <pack>/posts.json [--strict]
Exit 0 = no errors. --strict also fails on warnings (TODO media, missing schedule time).
"""
import json
import re
import sys

HASHTAG = re.compile(r"(?<!\w)#\w+")
PRODUCTS_PLAYLIST = "PLzmhjKCSrFwpTAOsA9OMEhkf5Wrs3jIEI"
EXPECTED_ACCOUNTS = {"facebook": "53000", "instagram": "72147", "tiktok": "60345", "youtube": "50377"}
BANNED_PHRASES = [r"\bofficial\b", r"\bapproved by\b", r"\bgovernment[- ]issued\b", r"\bissued\b",
                  r"\blaser works\b", r"\bonly \d+ left\b", r"\bselling fast\b"]


def hashtags(text):
    return HASHTAG.findall(text or "")


def check(pack):
    errors, warnings = [], []
    ai = pack.get("aiMedia")
    if not isinstance(ai, bool):
        errors.append("top-level aiMedia must be true/false")

    for i, post in enumerate(pack.get("posts", [])):
        p = post.get("platform", f"post[{i}]")
        c = post.get("content", {}) or {}
        t = post.get("target", {}) or {}
        text = c.get("text", "") or ""
        media = c.get("mediaUrls", []) or []
        tags = hashtags(text)
        E = lambda m: errors.append(f"[{p}] {m}")
        W = lambda m: warnings.append(f"[{p}] {m}")

        if EXPECTED_ACCOUNTS.get(p) and post.get("accountId") != EXPECTED_ACCOUNTS[p]:
            W(f"accountId {post.get('accountId')} != expected {EXPECTED_ACCOUNTS[p]} (verify with blotato_list_accounts)")
        if not text.strip():
            E("text is empty")
        if not media:
            E("no mediaUrls")
        for u in media:
            if u.startswith("TODO"):
                W(f"media placeholder {u}")
            elif not u.startswith("https://"):
                E(f"media URL not public https: {u}")
        if not post.get("scheduledTime"):
            W("scheduledTime not set")
        for pat in BANNED_PHRASES:
            if re.search(pat, text, re.I):
                W(f"review wording: matches /{pat}/")
        if re.search(r"made in (the )?usa", text, re.I):
            W("'Made in USA' claim — confirm intel.md says all/virtually all US-made")

        if p == "facebook":
            if t.get("pageId") != "370318706175109":
                E("pageId missing/wrong")
            limit = 2200 if t.get("mediaType") == "reel" else 63206
            if len(text) > limit:
                E(f"text {len(text)} > {limit}")
            if len(tags) > 3:
                E(f"{len(tags)} hashtags > 3")
            if not c.get("firstComment"):
                W("no firstComment link")
        elif p == "instagram":
            if len(text) > 2200:
                E(f"caption {len(text)} > 2200")
            if len(tags) > 5:
                E(f"{len(tags)} hashtags > 5 (hard limit)")
            if not c.get("altText"):
                E("altText missing")
            if t.get("mediaType") == "reel":
                if len(media) != 1:
                    E("reel must have exactly 1 video")
                if t.get("shareToFeed") is not True:
                    W("reel shareToFeed not true")
            elif t.get("mediaType") in (None, ""):
                if not 2 <= len(media) <= 10:
                    E(f"carousel has {len(media)} items (2-10)")
            if re.search(r"https?://", text):
                W("URL in IG caption is not clickable — use link in bio / Comment ENGRAVE")
        elif p == "tiktok":
            if len(text) > 2200:
                E(f"caption {len(text)} > 2200")
            if not 3 <= len(tags) <= 5:
                E(f"{len(tags)} hashtags (need 3-5)")
            if not 100 <= len(text) <= 300:
                W(f"caption {len(text)} chars (target 100-300)")
            req = {"privacyLevel": "PUBLIC_TO_EVERYONE", "disabledComments": False, "disabledDuet": False,
                   "disabledStitch": False, "isBrandedContent": False, "isYourBrand": True}
            for k, v in req.items():
                if t.get(k) != v:
                    E(f"{k} must be {v!r}, got {t.get(k)!r}")
            if t.get("isAiGenerated") is not ai:
                E(f"isAiGenerated {t.get('isAiGenerated')!r} != pack aiMedia {ai!r}")
            title = t.get("title")
            if title and len(title) > 90:
                E(f"photo title {len(title)} > 90")
        elif p == "youtube":
            title = t.get("title", "") or ""
            if not title:
                E("title required")
            elif len(title) > 100:
                E(f"title {len(title)} > 100")
            elif len(title) > 60:
                W(f"title {len(title)} > 60 (aim shorter)")
            if len(text.encode("utf-8")) > 5000:
                E(f"description {len(text.encode('utf-8'))} bytes > 5000")
            if "#shorts" not in text.lower():
                E("description missing #Shorts")
            tag_len = sum(len(x) for x in t.get("tags", []) or [])
            if tag_len > 500:
                E(f"tags total {tag_len} > 500")
            if t.get("privacyStatus") not in ("public", "private", "unlisted"):
                E("privacyStatus missing")
            if t.get("isMadeForKids") is not False:
                E("isMadeForKids must be false")
            if t.get("containsSyntheticMedia") is not ai:
                E(f"containsSyntheticMedia {t.get('containsSyntheticMedia')!r} != pack aiMedia {ai!r}")
            if PRODUCTS_PLAYLIST not in (t.get("playlistIds") or []):
                W("not added to Products playlist")
        else:
            W("unknown platform — not checked")
    return errors, warnings


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    strict = "--strict" in sys.argv
    if len(args) != 1:
        print(__doc__)
        return 2
    with open(args[0], encoding="utf-8") as f:
        pack = json.load(f)
    errors, warnings = check(pack)
    for e in errors:
        print("ERROR  ", e)
    for w in warnings:
        print("WARN   ", w)
    failed = bool(errors) or (strict and bool(warnings))
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s) -> {'FAIL' if failed else 'PASS'}"
          + (" (strict)" if strict else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
