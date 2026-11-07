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

## 3. Reasoning rules for TikTok plans

1. **Automation-first, but never automation-only.** Smart+ / GMV Max are the default for scaling; keep at least one manual/ABO channel alive for clean creative read-outs.
2. **Creative is the throttle.** When performance drops, diagnose in this order: (a) creative fatigue, (b) offer/price, (c) tracking breakage, (d) auction/bid, (e) audience. Changing audience first is almost always wrong on TikTok.
3. **Do not scale below signal thresholds.** Conversion campaigns need ≈50 conversions / 7 days per ad group, and budget ≈10× CPA, before "it doesn't work" is a valid conclusion.
4. **Never compare platforms on platform-reported ROAS.** Use blended + incrementality.
5. **Respect the learning phase.** No edits to bid/audience/creative inside the first 7 days (Smart+/GMV Max) or 3–5 days (manual), unless the campaign is broken (not spending, wrong event).
6. **Localise compliance before copy.** Health/beauty/finance claims in TH have hard legal limits. See chapter 10.

## 3b. Reasoning rules for profit / unit-economics plans

1. **CM before media.** Never recommend increasing ad budget before CM2 per order (in baht) is known and above the floor. CM2 < 18% means the problem is structural, not a media problem.
2. **Baht per order first, % second.** Compute CM as ฿/order per SKU per channel, then compare percentages on net revenue (after seller discount) — never on list price.
3. **Take rate, not commission.** Compare channels on total take rate (commission + transaction + infra + service fee + growth fee + affiliate). Commission alone understates by 5–8 pts.
4. **Land, not FOB.** COGS = landed cost (freight + duty + forwarder). Using FOB overstates CM by 5–10 pts.
5. **Provision refusals inside CM.** COD refusal (TH: 8–12%) must be a CM line item, split by SKU — never an "other cost" at the bottom.
6. **MER decides budget; platform ROAS decides creative.** Never compare channels on platform-reported ROAS (double-counts 20–40%).
7. **Check the GP cut window.** 1 Dec 2026 – 31 May 2027 Thai platform fees revert to 1 Jan 2026 rates, ad fees excluded. Compute two breakeven ROAS sets (during / after) and plan on the worse one. Never pass a fee cut on as a price cut.
8. **Cash is not profit.** Always pair CM with cash conversion cycle and cash runway. Profit with a 45-day CCC and 2-month runway is a solvency risk.
9. **Notation.** This repo uses `CM1/CM2/CM3` = cost-deduction order (before platform fee / before marketing / after marketing) in the profit playbook, and `CM₁/CM₂` = first-order / second-order in the LINE playbook. Never mix them; write the meaning in words.

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
