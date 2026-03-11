# Playwright 10-Cycle Protocol

## Purpose

Provide a repeatable loop to optimize Playwright scraping config while keeping measurements comparable cycle to cycle.

## Preconditions

- macOS host with Python 3.
- `playwright`, `trafilatura`, `requests` installed.
- Experiment folder contains fixed URL corpus and score logic.

Each run iterates through a predetermined corpus of **100 websites**, with `scraper.py --cycle <1-10>` picking 10 sites per cycle. This keeps the Workloads consistent, desktop-only, and easy to track in the OpenClaw memory/context log (see `docs/OPENCLAW_MEMORY_CONTEXT.md` for the reasoning).

## Cycle Rules

- Run exactly 10 cycles.
- Change one variable class per cycle (wait strategy, timeout, headless, viewport, extraction logic).
- Do not modify URL list or score formula during a 10-cycle run.
- Create one commit per cycle.

## Cycle Procedure

1. Pull latest branch state.
2. Read prior cycle score and failure modes.
3. Define one hypothesis.
4. Apply targeted config/code change.
5. Execute one benchmark cycle.
6. Record result to `results/cycle_XX.json` and `results.tsv`.
7. Decide keep/revert direction based on score and reliability.
8. Commit with hypothesis + outcome.

## Phase Plan (10 cycles)

- Cycles 1-3: broad exploration of major knobs.
- Cycles 4-7: exploit best region and tune numeric values.
- Cycles 8-9: robustness checks against prior best.
- Cycle 10: final confirmation run.

## Commit Message Format

```text
Cycle-X: short change title

Hypothesis: ...
Change: ...
Result: score=..., avg_time=..., completeness=..., success=.../10
Decision: keep|revert|branch
```

## Stop Conditions

- Abort cycle if benchmark cannot run to completion.
- Document blocking error in cycle JSON and continue next cycle only after fix.

## Deliverables After Cycle 10

- Updated `results.tsv` with 10 rows.
- `RESEARCH_REPORT.md` filled from template.
- Final best config captured in report.
