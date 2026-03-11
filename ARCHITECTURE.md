# BYOC Architecture (Playwright Only)

## Overview

This system runs autonomous Playwright research loops using local compute (Apple Silicon) and Git-based coordination.

## Components

| Component | Role | Location |
|-----------|------|----------|
| LLM Agent | Proposes next-cycle config changes | Cloud/local agent runtime |
| Git Remote | Synchronization and history | GitHub |
| Apple Silicon Host | Executes benchmark cycle | Local macOS |

## Data Flow

```text
Agent proposes change -> commit/push -> local host pulls
local host runs cycle -> writes results -> commit/push -> agent analyzes
```

## Experiment Contract

- `program.md`: mutation guardrails and objective.
- `scraper.py`: benchmark + scoring logic.
- `results/cycle_XX.json`: cycle-level detailed output.
- `results.tsv`: compact trend log for all cycles.
- `RESEARCH_REPORT.md`: final synthesis.

## Cycle Cadence

Default cadence in automation script is 15 minutes between cycles (configurable).

## Invariants

- Keep fixed URL corpus inside an experiment for comparability.
- Keep score function stable across cycles.
- Keep one commit per cycle for traceability.
