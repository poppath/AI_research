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
