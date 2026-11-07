# AGENTS.md — rules for AI agents working in this repo

This repo is a **knowledge base for AI agents** as much as for humans. If you are an LLM reading this to produce marketing plans, follow these rules.

---

## 1. What this repo is

- `playbooks/<name>/NN-*.md` — reasoning-oriented chapters (Thai, with English jargon).
- `playbooks/<name>/playbook.json` — machine-readable decision rules (triggers → actions).
- `playbooks/<name>/benchmarks.json` — numeric benchmarks with `market`, `as_of`, `source_type`.
- `playbooks/<name>/SOURCES.md` — full source list with URLs.

## 2. Epistemic rules (non-negotiable)

1. **Never invent a benchmark.** If a number is not in `benchmarks.json` or a cited chapter, say "ไม่มีข้อมูล — ต้องวัดเอง" and propose the measurement.
2. **Every number carries a date and a market.** "CPM ถูก" is useless. "CPM ไทย ฿50–200 (พ.ย. 2026, vendor range)" is usable.
3. **Respect source_type:**
   - `tiktok` — TikTok Help Center / official blog. Cite as platform guidance, still not a guarantee.
   - `vendor` — agency or SaaS blog. Directionally useful, treat as hypothesis.
   - `est` — triangulated. Label as estimate.
   - `primary` — measured in an account you operate. Highest trust.
4. **Platform docs beat vendor blogs** when they conflict. Vendor claims of "+52% ROAS" are marketing, not forecasts.
5. **Say when data is stale.** Anything `as_of` older than 90 days must be re-verified before a budget decision.

## 3. Decision and evidence rules (reviewed 2026-11-07)

- คำแนะนำ TikTok ในบทเก่าเรื่อง learning, conversions, budget และ no-edit เป็น heuristic ไม่ใช่เกณฑ์สากลหรือเงื่อนไขรับรอง performance; ตรวจเอกสารปัจจุบันตาม objective, product และ account ก่อนใช้ และหยุดได้ทันทีเมื่อมี safety/cash/tracking incident
- วัด creative, offer, tracking, auction และ audience ตามหลักฐาน ไม่บังคับลำดับวินิจฉัยเดียวทุกบัญชี; platform ROAS ไม่ใช่ incremental ROAS
- Profit: คำนวณ CM เป็นบาทตามนิยามใน `03-cm-ladder.md`, แล้วหารด้วย revenue หลังส่วนลด; กำหนด floor จากต้นทุน, CAC, overhead, cash และ risk ของกิจการ ไม่ใช้ 18% เป็น universal floor
- COD refusal, ค่าธรรมเนียม, attribution overlap และมาตรการ GP cut ต้องตรวจ statement, contract และแหล่งทางการปัจจุบันก่อนใช้; รายงานผ่าน vendor ไม่เท่ากับยืนยัน official และห้ามสมมติว่าใช้ได้กับทุกบัญชี
- คำนวณโปรโมชันใหม่ตามฐานรายได้และ fee จริง ดู [วิธีแก้ discount](playbooks/profit-unit-economics-2026/07-promo-voucher-math.md); อย่าใช้สูตรลัดเดิม
- Profit CM1/CM2/CM3 คือขั้นหักต้นทุน แต่ LINE CM₁/CM₂ หมายถึง first/second order: ระบุความหมายทุกครั้ง
- ข้อความเก่าใน profit, TikTok, LINE และ Meta เป็น research snapshot ไม่ใช่ verified rates หรือผลทดสอบ: อ่าน [audit](REPO-REVIEW-2026-11-07.md) และ re-verify ก่อนดำเนินการ; กฎนี้มี precedence เหนือ heuristic เก่าที่ขัดกันใน prose/JSON

## 4. Output rules

When producing a plan for a user, always return:

1. **Baseline assumption block** — budget, AOV, margin, target CPA/ROAS, category, market. If missing, state the assumption explicitly.
2. **The numbers you will be judged on** — one primary KPI, two guardrails.
3. **Structure** — campaign/ad group counts and budget split.
4. **Creative plan** — number of concepts, hooks, formats, refresh cadence.
5. **Measurement plan** — what instrumentation must exist before spend.
6. **Kill criteria** — dates and thresholds, decided *before* launch.

Never output a plan without kill criteria.

## 5. Formatting rules

- Thai prose, English for platform nouns (Smart+, GMV Max, Spark Ads, Events API, EMQ…).
- Tables for comparisons; numbered steps for procedures.
- Use ฿ for THB, $ for USD. Always state which.
- Keep code/JSON valid — `playbook.json` and `benchmarks.json` are parsed by tools.
