# Intel: Christmas order-by deadline (themed pack)

Compiled by product-intel, 2026-11-20. Facts only. Pack theme: "Order custom gifts in time for Christmas."

**Etsy data could not be fetched.** `www.etsy.com` and `honorcraftlw.etsy.com` do not resolve in this
session (the hosts are outside the session's allowed network). Everything below comes from the Shopify
Admin API (honorcraftlw.com), plus one owner-supplied fact that the orchestrator relayed.

---

## 1. Shop-level facts

| Field | Value | Source |
|---|---|---|
| Shop name (Shopify) | HonorCraft | Shopify get-shop-info |
| Etsy shop name | UNKNOWN (URL handle is `honorcraftlw`) | Etsy not reachable |
| Location | Piketon, Ohio, United States | Shopify shopAddress |
| Currency | USD | Shopify |
| **Christmas order-by date** | **December 13, 2026. Wording: "Order by December 13 for Christmas delivery"** | **David (owner), 2026-11-20.** The orchestrator relayed this. product-intel did not see it in any shop listing, announcement or policy. |
| Etsy shop announcement / holiday note | UNKNOWN | Etsy not reachable |
| Etsy processing / shipping policy | UNKNOWN | Etsy not reachable |
| Shopify shipping policy (full text) | "We will do everything in our power to get you the best rates and items in a timely manner. Rates are base off your location." No processing time, carrier, transit time or holiday cutoff is stated. | Shopify shopPolicies SHIPPING_POLICY |
| Shopify refund policy, custom items | "Certain types of items cannot be returned, like ... custom products (such as special orders or personalized items)". Returns are 30 days for other items. The policy still contains the placeholder "[INSERT RETURN ADDRESS]". | Shopify shopPolicies REFUND_POLICY |
| Holiday cutoff anywhere on Shopify | None found in the policies or the product descriptions I checked | Shopify |

**Conflict check (Dec 13 vs. listed processing times):** I could not run it. None of the selected
products shows a processing time on Shopify, and the Etsy "Ready to ship in X–Y days" values could not
be fetched. No conflict was found, but none can be ruled out. One more data point: the Shopify
fulfillments report shows a median of 0.0 days from order to fulfillment (284 orders, last 365 days).
That figure is store-wide and most of those orders are shirts and patches (see note 5). It is **not** a
processing time for custom gifts, so do not use it as one.

---

## 2. Selected personalizable, giftable products

**How these were chosen:** Etsy best-seller and favorite counts were not available. Shopify sales for
the last 365 days are dominated by non-catalog "1191" apparel and patches. No product below has more
than 1 recorded Shopify sale, so none can be called a best seller. I chose these because they are
personalizable, giftable and active on the online store. The first two are confirmed Etsy cross-listings.

Prices are copied exactly as listed on Shopify. No product has a compare-at price.

### A. Personalized Pet Memorial Stone – Laser Engraved Granite Grave Marker
- Shopify: https://honorcraftlw.com/products/personalized-pet-memorial-stone-laser-91816
- Price: Small - 4x6 **$36.00 USD**; Large - 5x7 **$43.00 USD**
- Inventory: 4 per variant (tracked)
- Material (listing text): "Polished Black Granite" / "solid Absolute Black Granite"
- Dimensions (listing text): "SM = 4x6, LG= 5x7 and .30in thick"
- Personalization (listing text): pet's photo, name, dates and a short dedication. The buyer enters the name and dates in the personalization box, then sends a photo "via Etsy Messages". "We will send you a proof before we make it."
- Processing time: **UNKNOWN**
- Etsy cross-listing: Etsy listing ID **4442891816** (Shopify metafield `shuttle.etsy_product_id`). The likely URL is https://www.etsy.com/listing/4442891816. I built that URL from the ID and could not open it to check. Etsy price: UNKNOWN.
- Images (cdn.shopify.com, 3000x2250; the filenames show they were synced from Etsy):
  - https://cdn.shopify.com/s/files/1/0808/4969/9097/files/il_fullxfull.8375135482_4sfi.jpg
  - https://cdn.shopify.com/s/files/1/0808/4969/9097/files/il_fullxfull.7613069990_9s1n.jpg
  - https://cdn.shopify.com/s/files/1/0808/4969/9097/files/il_fullxfull.7613070208_ss87.jpg

### B. Personalized Leatherette Travel Jewelry Box
- Shopify: https://honorcraftlw.com/products/personalized-leatherette-travel-jewelry-36298
- Price: **$20.00 USD** (all colors)
- Colors: Light Blue, Burgundy, Seafoam, Blue Matte, Pink (1 of each in stock)
- Material (listing text): "durable leatherette", "water-resistant leatherette with a secure zippered closure", "Soft velvet-style lining"
- Dimensions (listing text): 4" x 4" x 2" tall
- Interior (listing text): 6 ring rolls, 3 necklace hooks with elastic pocket, 4 divided compartments (removable)
- Personalization (listing text): custom text (monograms, names, dates, quotes) or custom images and logos, laser engraved on the lid. The buyer adds the text and font in the personalization box and sends images via Etsy message.
- Processing time: **UNKNOWN**
- Etsy cross-listing: Etsy listing ID **4474736298**. The likely URL is https://www.etsy.com/listing/4474736298 (built from the ID, not checked). Etsy price: UNKNOWN.
- Images (cdn.shopify.com):
  - https://cdn.shopify.com/s/files/1/0808/4969/9097/files/il_fullxfull.7871341973_92oa.jpg (1333x1778)
  - https://cdn.shopify.com/s/files/1/0808/4969/9097/files/il_fullxfull.7871456635_ffgd.jpg (2000x2000)
  - https://cdn.shopify.com/s/files/1/0808/4969/9097/files/il_fullxfull.7823394154_qeap.jpg (1176x1569)
- Duplicate: Shopify also has "Custom Leatherette Traveling Jewelry Box" at the same price, $20.00 USD (https://honorcraftlw.com/products/custom-leatherette-traveling-jewelry-box, 9 in stock). It has 1 recorded Shopify sale.

### C. Custom Metal engraved wallet
- Shopify: https://honorcraftlw.com/products/custom-metal-engraved-wallet
- Price: **$15.00 USD**
- Colors: Black (0 in stock), Orange 3, Green 2, Blue 3, Silver 4, Pink 5, Purple 5
- Material: "metal" (product type). The specific metal is UNKNOWN.
- Dimensions: UNKNOWN
- Personalization (listing text): "Choose your design, initials, or meaningful message laser-engraved". The buyer emails details to honorcraftlw@gmail.com after purchase, with the order number in the subject line.
- Processing time: **UNKNOWN**
- Etsy cross-listing: none found (no Etsy ID metafield). UNKNOWN whether it is on Etsy.
- Images (3000x4000):
  - https://cdn.shopify.com/s/files/1/0808/4969/9097/files/20260320_163623.jpg
  - https://cdn.shopify.com/s/files/1/0808/4969/9097/files/20260320_163628.jpg
  - https://cdn.shopify.com/s/files/1/0808/4969/9097/files/20260320_163616.jpg

### D. Memorial Ornament with custom text
- Shopify: https://honorcraftlw.com/products/memorial-ornament-with-custom-text
- Price: **$13.00 USD**
- Material (listing text): "quality wood with precision laser engraving". The wood species is UNKNOWN.
- Dimensions: UNKNOWN
- Personalization (listing text): "Personalize with any name". Details go by email after purchase.
- Inventory: 0 and not tracked, so it can still be ordered. Treat it as made to order.
- Tags include "Military" and "Memorial". See the insignia note in section 3.
- Processing time: **UNKNOWN**
- Etsy cross-listing: none found. UNKNOWN.
- Images:
  - https://cdn.shopify.com/s/files/1/0808/4969/9097/files/MemorialOrnamentfront.jpg (2236x2982)
  - https://cdn.shopify.com/s/files/1/0808/4969/9097/files/MemorialOrnamenttop.jpg (1933x2577)

### E. Baby first Christmas Ornament
- Shopify: https://honorcraftlw.com/products/baby-first-christmas-ornament
- Price: **$15.00 USD**
- Material: Wooden Ornament (product type). The wood species is UNKNOWN.
- Dimensions: UNKNOWN
- Personalization (listing text): details go by email after purchase. The fields that can be personalized are not specified.
- Inventory: 0 and not tracked
- Processing time: **UNKNOWN**
- Etsy cross-listing: none found. UNKNOWN.
- Images:
  - https://cdn.shopify.com/s/files/1/0808/4969/9097/files/transparent-Photoroom.jpg (2048x1536)
  - https://cdn.shopify.com/s/files/1/0808/4969/9097/files/FirstChristmasBacker.png (1200x1200, backer card)

### F. Dog Memorial Ornament
- Shopify: https://honorcraftlw.com/products/dog-memorial-ornament
- Price: **$15.00 USD**
- Material: Wooden Ornament (product type). The wood species is UNKNOWN.
- Dimensions: UNKNOWN
- Personalization (listing text): details go by email after purchase. The fields are not specified.
- Inventory: 0 and not tracked
- Processing time: **UNKNOWN**
- Etsy cross-listing: none found. UNKNOWN.
- Images:
  - https://cdn.shopify.com/s/files/1/0808/4969/9097/files/Dog.png (553x553, low resolution)
  - https://cdn.shopify.com/s/files/1/0808/4969/9097/files/DogMemBacker.png (1200x1200)

**Alternate, not selected:** "Grill Master BBQ Tool Set – Custom Engraved Wooden Box", $60.00 USD
(https://honorcraftlw.com/products/grill-master-bbq-tool-set-custom-engraved-wooden-box). The listing
describes a fixed "Grill Master" American flag engraving and fixed tool-name engravings. It is UNKNOWN
whether buyers can personalize it, which is why it was left out.

**Excluded:** the Firefighter "Welcome to Our Home" door hanger (Etsy ID 4580000653). The listing says
"this design isn't personalized". Its description also still contains placeholder text: "[Insert your
current processing time ...]".

---

## 3. Compliance facts

- **Made in USA:** UNKNOWN for every product. The listings describe engraving and customizing in the
  Ohio shop ("customized right here in our Southern Ohio shop"). They do not say where the blanks come
  from: granite, leatherette boxes, metal wallets, wood ornament blanks. Do not make a "Made in USA" claim.
  "Veteran-owned" appears in the jewelry box listing text.
- **Military insignia:** UNKNOWN. The Memorial Ornament is tagged "Military", but the images were not
  inspected and the listing text names no branch emblem. None of the other selected products
  describes any insignia. The visual director should check the memorial ornament images before using them.
- **Reviews:** the Judge.me metafields show 0 reviews on every selected product. Do not mention reviews or ratings.
- **Scarcity:** inventory counts are real but low (for example, 1 of each jewelry box color). Do not
  imply scarcity unless the strategist decides to and checks the count live.

---

## UNKNOWN:
1. **Processing time ("Ready to ship in X–Y days") for every product.** Blocks any claim that orders
   placed before Dec 13 will arrive by Christmas. It also blocks the conflict check against Dec 13.
2. Etsy shop announcement and any holiday cutoff posted on Etsy (to confirm it matches Dec 13).
3. Etsy shipping policy: carriers, transit times, whether upgrades are offered.
4. Etsy prices for listings 4442891816 and 4474736298, and whether the built listing URLs work.
5. Whether the products in sections C to F are on Etsy, and their Etsy URLs, prices and i.etsystatic.com images.
6. Etsy best-seller and favorite data.
7. Made in USA status for all products.
8. Military insignia on the Memorial Ornament.
9. Dimensions and wood or metal species for the wallet and the ornaments.
10. Personalization fields for the Baby First Christmas and Dog Memorial ornaments.

To fill items 1 to 6, the user can either allow `www.etsy.com` in the session network settings, or
paste these for each listing: title, price, "Ready to ship in" text, personalization text and photo
URLs, plus the shop announcement and shipping policy text.

## Notes / inconsistencies (facts for QA)
- The Shopify descriptions for the Pet Memorial Stone and the Travel Jewelry Box tell buyers to send
  photos "via Etsy Messages". The copy was synced from Etsy and sounds wrong on the Shopify site.
- The Shopify refund policy still contains "[INSERT RETURN ADDRESS]".
- Shopify sales for the last 365 days mainly come from "1191" apparel and patch items and blank-title
  line items. None of the gift products has more than 1 recorded Shopify sale.

## Sources:
- Shopify Admin API (connected store honorcraftlw.com): get-shop-info; GraphQL `products` (titles,
  prices, variants, descriptions, media, metafields including `shuttle.etsy_product_id`);
  GraphQL `shop.shopAddress`, `shop.shopPolicies`.
- Shopify ShopifyQL: `FROM sales ... GROUP BY product_title SINCE -365d`; `FROM fulfillments ... SINCE -365d`.
- Shopify policy pages: https://checkout.shopify.com/80849699097/policies/44902842649.html (shipping),
  https://checkout.shopify.com/80849699097/policies/44638077209.html (refund).
- Owner fact relayed by the orchestrator: Christmas order-by date Dec 13, 2026, from David (owner), 2026-11-20.
- Tried and failed: WebFetch https://www.etsy.com/shop/honorcraftlw and https://honorcraftlw.etsy.com
  (the hosts do not resolve; they are outside the session's network allowlist).

## Owner decisions — David, 2026-11-20 (verified, source: David)
- **Featured products (only these):** B. Personalized Leatherette Travel Jewelry Box ($20.00), D. Memorial Ornament with custom text ($13.00), E. Baby First Christmas Ornament ($15.00), F. Dog Memorial Ornament ($15.00). Do NOT feature A (Pet Memorial Stone) or C (wallet).
- **Order-by:** All featured items can be made and delivered for Christmas when ordered by **Sunday, December 13, 2026**. Posts state "Order by Sunday, Dec 13 for Christmas delivery". Do not state per-item processing day counts (still UNKNOWN).
- **Link / CTA destination:** Etsy shop https://honorcraftlw.etsy.com (use the shop URL, not unverified listing URLs).
