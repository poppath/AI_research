# SOURCES — แหล่งอ้างอิงและระดับความน่าเชื่อถือ

> **Review 7 พ.ย. 2026:** เอกสารเดิมเป็น research snapshot มีตัวเลข/heuristic และข้ออ้างที่ยังต้องตรวจรายกรณี ไม่ใช่กฎสากลหรือ rate ปัจจุบัน; ก่อนใช้ให้ดู [ข้อจำกัดและรายการแก้ไข](../../REPO-REVIEW-2026-11-07.md) และ `AGENTS.md` โดยเฉพาะก่อนตัดสินใจงบ กฎหมาย หรือ automation.

**วันที่เก็บข้อมูล:** 2026-11-06

## ระดับความน่าเชื่อถือ

| Tier | ความหมาย | ใช้อย่างไร |
|---|---|---|
| **A** | เอกสารทางการของแพลตฟอร์ม / กฎหมาย / หน่วยงานรัฐ | ใช้อ้างได้ |
| **B** | รายงานอุตสาหกรรมที่มีระเบียบวิธีชัดเจน (Bain, Klaviyo, Omnisend) | ใช้เป็น benchmark |
| **C** | agency / blog ที่มีตัวเลขระบุแหล่ง | ใช้เป็นกรอบ ต้องระบุว่า vendor |
| **D** | ความเห็น / ประสบการณ์ | ใช้เป็นสมมติฐาน ไม่ใช่อ้าง |

---

## line-pricing
| # | แหล่ง | Tier | ใช้ในบท | สาระสำคัญ |
|---|---|---|---|---|
| 1 | LINE for Business Thailand — แพ็กเกจ broadcast | A | 02, 11, METRICS | Free 300 / Basic ฿1,280/15,000 / Pro ฿1,780/35,000 (ต.ค. 2026, ไม่รวม VAT) |
| 2 | linebot.pro — LINE Automation in Thailand 2026 | C | 02, 11 | จุดตัด 20,000 messages; MyCustomer ฿369 (ฟรีบน Pro); OA Chat Package ฿555 |
| 3 | relevantaudience.com — LINE OA service Bangkok | C | 02 | setup ฿8,000–25,000; จัดการ ฿15,000–50,000/เดือน |
| 4 | idmcouncil.com — LINE OA 2026 ฟีเจอร์ใหม่ | C | 02 | verified ฿888 ครั้งเดียว; Premium ID ฿444/ปี |
| 5 | makewebeasy.com — LINE OA package | C | 02 | ยืนยันโครงแพ็กเกจเดียวกับ LINE |

## line-oa-features / rich-menu
| # | แหล่ง | Tier | ใช้ในบท | สาระสำคัญ |
|---|---|---|---|---|
| 6 | mcixagency.com — LINE Rich Menu Strategy Thailand 2026 | C | 02 | 4 ปุ่มชนะ 6 ปุ่ม; per-user menu; วัด tap → downstream action |
| 7 | mcixagency.com — LINE OA for Thai retail 2026 | C | 02 | journey 12 สัปดาห์; use case แยกตาม vertical |
| 8 | sphereagency.com — LINE OA setup guide Thailand | C | 02, 06 | open rate เป้า 60%+; block rate < 5%; 2–4 broadcast/เดือน |
| 9 | hypelive.io — LINE OA automation SME | C | 02 | greeting / auto-reply / rich menu / chat tag พื้นฐาน |
| 10 | relevantaudience.com — CRM lives in chat | C | 02, 04 | 3 สิ่งที่ทำให้ OA เป็น CRM: tag standard, segmented send, key ผูกประวัติซื้อ |

## line-ads
| # | แหล่ง | Tier | ใช้ในบท | สาระสำคัญ |
|---|---|---|---|---|
| 11 | LINE for Business Thailand — LINE Ads | A | 03, METRICS | 6 รูปแบบการซื้อ: CPM, CPC, CPF, CPV, CPA, CPI |
| 12 | redclawey.com — LINE Ads Platform Guide 2026 | C | 03 | โครงทดสอบ 3–5 ad group; ห้ามแก้ 3 วันแรก; +20–30%/3 วัน |
| 13 | everydaymarketing.co — LINE Marketing 2026 | C | 01, 03, 08 | CPM เฉลี่ย ~฿15; chat commerce 85–98%; allocation 40/25/25/10 |
| 14 | tumwebsme.com — LINE Ads for SME | C | 03 | daily budget ตั้งได้ถึงสตางค์; ตัวอย่าง ฿300–500/วัน |
| 15 | phoenixmedia.co.th — costs of ads Thailand | C | 03 | CPM ~฿15, CPV ~฿1.22; ต้องผ่าน agency |
| 16 | nipa.co.th — LINE Ads packages | C | 03 | ขั้นต่ำ ฿500/วัน; CPM premium ฿50–200 |

## line-crm / loyalty
| # | แหล่ง | Tier | ใช้ในบท | สาระสำคัญ |
|---|---|---|---|---|
| 17 | lineforbusiness.com — MyCustomer CRM vs Reward Card | A | 08 | Reward Card ไม่เก็บข้อมูล; CRM เก็บชื่อ/เบอร์/tier/tag/MyShop |
| 18 | lineforbusiness.com — MyCustomer CRM คู่มือ | A | 08 | ฿369/เดือน, ทดลอง 30 วัน, ฟรีบน Pro; 5 วิธีให้ point |
| 19 | blog.cresclab.com — ราคา LINE OA 2026 | C | 11, METRICS | ตารางแพ็กเกจ + CRM add-on |

## chat-commerce / myshop
| # | แหล่ง | Tier | ใช้ในบท | สาระสำคัญ |
|---|---|---|---|---|
| 20 | LINE Thailand (อ้างผ่าน everydaymarketing) | C | 07 | chat commerce + MyShop + LINE Pay ปิดยอด 85–98% (vendor claim) |
| 21 | marketingagency.sg — LINE advertising SEA | C | 07 | LINE Shopping / MyShop สำคัญในไทย; CPM ไทย ฿30–80 |
| 22 | vos.line-scdn.net — LINE Ads Platform Media Guide | A | 03 | placement: Smart Channel, TODAY, VOOM, Wallet, Home, OpenChat, Album |

## retention-benchmarks
| # | แหล่ง | Tier | ใช้ในบท | สาระสำคัญ |
|---|---|---|---|---|
| 23 | trylexsis.com — Ecommerce Retention Benchmarks 2026 | B | 01, 09, METRICS | retention เฉลี่ย 30%, top 10% 62%; RPR 28.2%; repeat customer spend +67% |
| 24 | ask-luca.com — LTV:CAC benchmarks | C | 01, 09 | retention-led 4.2:1 vs acquisition 1.8:1; RPR 20–30% เฉลี่ย, 35–45% มี flow |
| 25 | eightx.co — cohort analysis 2026 | C | 05, 09 | m1 repeat 35–42%; m3 22–25%; beauty 90-day 30–40%; supplements 35–50% |
| 26 | usedaymark.io — D2C benchmarks 2026 | B | 09, METRICS | RPR ~19%; consumables 25–40%; apparel 12–17%; LTV:CAC 2.5–4:1 |
| 27 | exposegrowth.com — retention LTV vs CAC | C | 05, 09 | 90-day repeat by source; time to 2nd order; post-purchase flow share |
| 28 | layerfive.com — ecommerce analytics DTC | C | 09 | CAC payback < 90 วัน; MER 2.5–4×; 60-day repeat เป็น leading indicator |
| 29 | branvas.com — jewelry benchmarks | C | 05 | ตัวอย่าง vertical ที่ repeat ต่ำโดยธรรมชาติ |

## lifecycle-flows / email-automation-benchmarks
| # | แหล่ง | Tier | ใช้ในบท | สาระสำคัญ |
|---|---|---|---|---|
| 30 | Klaviyo (อ้างผ่าน digitalapplied) — flows benchmarks 2026 | B | 05 | flows = ~41% ของ email revenue จาก 5.3% ของ sends |
| 31 | research.stripo.email — Email Automation Benchmarks 2026 | B | 05 | welcome open 35%, conv 2.11%, cart 3.33%; 4 core flows = +320% rev/email |
| 32 | bsandco.us — Klaviyo flow benchmarks (14 แบรนด์) | C | 05 | welcome median CR 4.37%; post-purchase open 51.3% |
| 33 | sendx.io — ecommerce flows 2026 | C | 05 | automated RPR $2.87 vs campaign $0.18 |
| 34 | darkroomagency.com — email benchmarks 2026 | C | 05 | flow revenue 58–65% ของ email revenue; welcome conv 12–18% (P90) |
| 35 | digitalapplied.com — welcome sequence 2026 | C | 05 | 3–7 email series; +90% orders vs single email |

## rfm-segmentation
| # | แหล่ง | Tier | ใช้ในบท | สาระสำคัญ |
|---|---|---|---|---|
| 36 | digitalapplied.com — RFM Segmentation 2026 | C | 04 | 11 segment + % base/revenue + cap + action map |
| 37 | skillsetmaster.com — RFM SQL tutorial | C | 04 | NTILE(5) query; CASE mapping |
| 38 | fullmetrix.com — segmentation ecommerce | C | 04 | 10 segment มาตรฐาน + criteria |
| 39 | digitalapplied.com — segmentation stack 2026 | C | 04 | 4 ชั้น: RFM → behavioral → demographic → predictive |

## pdpa / thai-advertising-law / direct-marketing-law
| # | แหล่ง | Tier | ใช้ในบท | สาระสำคัญ |
|---|---|---|---|---|
| 40 | lexbangkok.com — Direct Marketing in Thailand (PDPA) | B | 10 | 2 ด่าน: PDPA + พ.ร.บ.ขายตรง; OCPB registration; draft guidance 7 ก.ค. 2026 |
| 41 | logon-int.com — Thailand PDPA guide | B | 10 | consent แยก, opt-out, sensitive data, grandfathering |
| 42 | fitconsent.com — PDPA cookie rules 2026 | C | 10 | opt-in, ไม่ pre-tick, เก็บหลักฐาน consent |
| 43 | callmark.com.my — PDPA สำหรับ sales call | C | 10 | implied consent ใช้ไม่ได้; ต้อง log |
| 44 | mywifinetworks.com — PDPA practical | C | 10 | privacy notice ภาษาไทย; แยก consent |

## thailand-market
| # | แหล่ง | Tier | ใช้ในบท | สาระสำคัญ |
|---|---|---|---|---|
| 45 | linebusinessconnect.com — LINE Ads Thailand | C | 01 | ผู้ใช้ LINE ไทย ~56M; ขั้นต่ำ ฿1,000/เดือน |
| 46 | adsterra.com — advertising in Thailand 2026 | C | 01 | ~92% ของคนไทยใช้ LINE รายสัปดาห์; LINE Ads CPM ฿50–200 premium |
| 47 | sphereagency.com — social media pricing Thailand 2026 | C | 03, 11 | LINE OA management ฿10,000–40,000/เดือน; LINE Ads ขั้นต่ำ ฿10–25K/เดือน |

## tools-stack / operations
| # | แหล่ง | Tier | ใช้ในบท | สาระสำคัญ |
|---|---|---|---|---|
| 48 | linebot.pro — tools landscape | C | 11 | native vs paid add-on vs third-party; 1 channel = 1 webhook |

---

## คำเตือนคุณภาพแหล่ง

1. **ตัวเลข LINE ในไทยส่วนใหญ่มาจาก agency ที่ขายบริการ** → มีแรงจูงใจให้ตัวเลขดูดี (CPM ต่ำ, conversion สูง) ใช้เป็นทิศทาง ไม่ใช่ fact
2. **85–98% chat commerce conversion** เป็นตัวเลขที่ถูกอ้างซ้ำโดยไม่มีระเบียบวิธี → อย่าใส่ deck โดยไม่ระบุที่มา
3. **Benchmark retention ส่วนใหญ่เป็น DTC ตะวันตก** โดยเฉพาะ Shopify — โครงสร้างตลาดไทย (marketplace, COD, return rate) ต่างกันมาก
4. **ราคา LINE เปลี่ยนหลายครั้ง** — ตาราง ณ ต.ค. 2026 ต้องเช็คหน้า LINE for Business ไทยก่อนตั้งงบ
5. **กฎหมาย**: เนื้อหาบท 10 เป็นสรุปเพื่อการปฏิบัติ ไม่ใช่คำปรึกษาทางกฎหมาย
