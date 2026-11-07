# AI_research

> **ตรวจ repo 7 พ.ย. 2026:** มีข้อจำกัดและคำเตือนสำคัญเรื่องสูตร/ตัวเลข/หลักฐานใน [repo review และ gap register](REPO-REVIEW-2026-11-07.md). เป็น research ไม่ใช่ระบบที่ทดสอบจริง; ตรวจแหล่งและบัญชีปัจจุบันก่อนใช้.

Deep-research playbooks written so that **an AI agent can read, reason with, and execute them** — not just humans.

## AI readiness

[เริ่มใช้ repo กับ LLM และ agent](ai-readiness/README.md) · [สถานการณ์จำลองและ decision tree](ai-readiness/scenarios/README.md) · [Agent contract](ai-readiness/AGENT-CONTRACT.md) · [Claim registry](ai-readiness/claims.json) · [Evaluation suite](ai-readiness/evals/README.md) · [สถานะและข้อจำกัด](ai-readiness/STATUS.md). ไม่ใช่ระบบ production หรือ training dataset ที่ตรวจครบ.

## Playbooks

| Playbook | Scope | Status |
|---|---|---|
| [`playbooks/tiktok-performance-marketing/`](playbooks/tiktok-performance-marketing/00-START-HERE.md) | TikTok Performance Marketing 2026 — paid, Shop/GMV Max, affiliate, LIVE, creative system, measurement, TH compliance | ✅ Live (2026-11) — [Notion](https://app.notion.com/p/TikTok-Performance-Playbook-2026-TH-Paid-Shop-GMV-Max-Affiliate-LIVE-41076ada3488811082f3ff29bc2a1dd5) · [Google Docs](https://docs.google.com/document/d/1c3ZzV3mA-6XtgLSJuB-pL_5MFIjMkKzfFzI2Po4GoPo) |
| [`playbooks/meta-ads-ai-2026/`](playbooks/meta-ads-ai-2026/README.md) | Meta Ads × AI (FB / IG / Reels / Threads) | ✅ Live (2026-11) — [Notion](https://app.notion.com/p/Meta-Ads-AI-Playbook-2026-Facebook-IG-Reels-Threads-41076ada3488814c953eccd33af83ca3) · [Google Docs](https://docs.google.com/document/d/1Gz2zKZZ5svZ0jjaVxYEZc9_Yb2AY22-HoFPxwm84A28/edit) |
| [`playbooks/line-crm-retention-2026/`](playbooks/line-crm-retention-2026/00-START-HERE.md) | LINE OA × CRM × Retention/LTV 2026 — OA foundation, friend growth, RFM segmentation, lifecycle flows, broadcast, chat commerce/MyShop, loyalty, LTV measurement, PDPA (TH) | ✅ Live (2026-11) — [Notion](https://app.notion.com/p/LINE-OA-CRM-Retention-LTV-Playbook-2026-TH-41176ada348881399a95e49da3842858) · [Google Docs](https://docs.google.com/document/d/1NcTC3CIYyDC_i9hnhBKgu9jMX4FHBxfKk1pqAd4VnuM/edit) |
| [`playbooks/profit-unit-economics-2026/`](playbooks/profit-unit-economics-2026/00-START-HERE.md) | Profit & Unit Economics 2026 — cost stack 13 ชั้น, CM ladder, marketplace take rate, COD/refusal, ค่าส่ง, voucher math, breakeven ROAS/MER/CAC, LTV, ภาษี/CCC, pricing floor (TH) | ✅ Live (2026-11) |

| [`playbooks/customer-research-positioning-2026/`](playbooks/customer-research-positioning-2026/00-START-HERE.md) | Customer Research & Positioning — interviews, evidence, segmentation, positioning, validation, privacy (TH) | ✅ Live (2026-11) |
| [`playbooks/ai-creative-production-2026/`](playbooks/ai-creative-production-2026/00-START-HERE.md) | AI Creative Production — concept, production, claim/rights QA, experimentation, operating system (TH) | ✅ Live (2026-11) |

| [`playbooks/marketing-measurement-attribution-2026/`](playbooks/marketing-measurement-attribution-2026/00-START-HERE.md) | Measurement & Attribution | ✅ Research guide (2026-11) |
| [`playbooks/conversion-rate-optimization-2026/`](playbooks/conversion-rate-optimization-2026/00-START-HERE.md) | CRO & Landing Pages | ✅ Research guide (2026-11) |
| [`playbooks/ecommerce-operations-fulfillment-2026/`](playbooks/ecommerce-operations-fulfillment-2026/00-START-HERE.md) | E-commerce Operations & Fulfillment | ✅ Research guide (2026-11) |
| [`playbooks/offer-merchandising-promotion-2026/`](playbooks/offer-merchandising-promotion-2026/00-START-HERE.md) | Offer, Merchandising & Promotion | ✅ Research guide (2026-11) |
| [`playbooks/google-ads-search-demand-2026/`](playbooks/google-ads-search-demand-2026/00-START-HERE.md) | Google Ads & Search Demand | ✅ Research guide (2026-11) |
| [`playbooks/customer-experience-service-reviews-2026/`](playbooks/customer-experience-service-reviews-2026/00-START-HERE.md) | Customer Experience, Service & Reviews | ✅ Research guide (2026-11) |
| [`playbooks/brand-strategy-organic-content-2026/`](playbooks/brand-strategy-organic-content-2026/00-START-HERE.md) | Brand Strategy & Organic Content | ✅ Research guide (2026-11) |
| [`playbooks/marketing-planning-budget-allocation-2026/`](playbooks/marketing-planning-budget-allocation-2026/00-START-HERE.md) | Marketing Planning & Budget Allocation | ✅ Research guide (2026-11) |
| [`playbooks/7m-ai-content-affiliate-automation-2026/`](playbooks/7m-ai-content-affiliate-automation-2026/00-START-HERE.md) | AI content, affiliate automation และ 7M | Research guide (2026-11) |
| [`playbooks/sector-business-2026/`](playbooks/sector-business-2026/00-START-HERE.md) | 20 sector business starter guides · 7M, safety, measurement (TH) | ✅ Starter research (2026-11) |

[Marketing Loop — ลำดับและการเชื่อมต่อ](playbooks/MARKETING-LOOP.md)

## How to use a playbook

1. **Humans** → read `00-START-HERE.md`, then the numbered chapters in order.
2. **AI agents / LLMs** → load `AGENTS.md` (repo-wide rules) + the playbook's `playbook.json` (machine-readable rules) + `benchmarks.json` (numbers). Prose chapters are the *why*; the JSON is the *what to do*.

Some older chapters use the following shape; starter guides and Meta have different structures:

```
TL;DR  →  หลักการ (principles)  →  ตัวเลข/benchmark  →  วิธีทำ (steps)  →  ตาราง decision  →  กับดัก  →  แหล่งอ้างอิง
```

## Conventions

- **Currency/locale:** THB + TH market first, USD/global second. Every number is tagged with market + date.
- **Numbers are dated.** Any figure older than 90 days must be re-verified before it drives a budget decision. See `benchmarks.json → freshness_rule`.
- **Vendor claims are labelled.** `[vendor]` = claim from an agency/blog. `[tiktok]` = TikTok's own documentation. `[est]` = triangulated estimate. Never present `[vendor]` numbers as fact.
- **Sources** อยู่ในไฟล์ sources ของแต่ละชุดหรือ sources ส่วนกลาง; Meta ใช้ `sources.md`.

## Repo rules for AI agents

See [`AGENTS.md`](AGENTS.md). Short version: no fabricated benchmarks, no un-dated numbers, no compliance advice that contradicts local law, and every recommendation must be traceable to a chapter + source.
