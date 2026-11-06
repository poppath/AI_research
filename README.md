# AI_research

Deep-research playbooks written so that **an AI agent can read, reason with, and execute them** — not just humans.

## Playbooks

| Playbook | Scope | Status |
|---|---|---|
| [`playbooks/tiktok-performance-marketing/`](playbooks/tiktok-performance-marketing/00-START-HERE.md) | TikTok Performance Marketing 2026 — paid, Shop/GMV Max, affiliate, LIVE, creative system, measurement, TH compliance | ✅ Live (2026-11) |
| `playbooks/meta-ads-ai-2026/` | Meta Ads × AI (FB / IG / Reels / Threads) | 🔗 Lives in Notion: [Meta Ads × AI Playbook 2026](https://app.notion.com/p/Meta-Ads-AI-Playbook-2026-Facebook-IG-Reels-Threads-41076ada3488814c953eccd33af83ca3) |

## How to use a playbook

1. **Humans** → read `00-START-HERE.md`, then the numbered chapters in order.
2. **AI agents / LLMs** → load `AGENTS.md` (repo-wide rules) + the playbook's `playbook.json` (machine-readable rules) + `benchmarks.json` (numbers). Prose chapters are the *why*; the JSON is the *what to do*.

Every chapter follows the same shape:

```
TL;DR  →  หลักการ (principles)  →  ตัวเลข/benchmark  →  วิธีทำ (steps)  →  ตาราง decision  →  กับดัก  →  แหล่งอ้างอิง
```

## Conventions

- **Currency/locale:** THB + TH market first, USD/global second. Every number is tagged with market + date.
- **Numbers are dated.** Any figure older than 90 days must be re-verified before it drives a budget decision. See `benchmarks.json → freshness_rule`.
- **Vendor claims are labelled.** `[vendor]` = claim from an agency/blog. `[tiktok]` = TikTok's own documentation. `[est]` = triangulated estimate. Never present `[vendor]` numbers as fact.
- **Sources** live in each playbook's `SOURCES.md`.

## Repo rules for AI agents

See [`AGENTS.md`](AGENTS.md). Short version: no fabricated benchmarks, no un-dated numbers, no compliance advice that contradicts local law, and every recommendation must be traceable to a chapter + source.
