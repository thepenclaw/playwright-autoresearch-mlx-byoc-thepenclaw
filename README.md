# Playwright Autoresearch (BYOC) - ThePenclaw

BYOC (Bring Your Own Compute) autoresearch for Playwright scraping experiments on Apple Silicon.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: macOS](https://img.shields.io/badge/Platform-macOS-blue.svg)](https://www.apple.com/macos/)
[![MLX](https://img.shields.io/badge/MLX-Apple%20Silicon-orange.svg)](https://github.com/ml-explore/mlx)

## Scope

This repository is intentionally scoped to Playwright autoresearch only:
- Playwright scraping optimization loops
- Repeatable cycle-based benchmarking
- BYOC execution on local Apple Silicon

## Current Experiment

| Date | Experiment | Status | Summary |
|------|------------|--------|---------|
| 2026-03-10 | [Playwright M4 Optimization](experiments/2026-03-10-playwright-m4-optimization/) | Complete | 10-cycle baseline optimization and config convergence |

## Quick Start

```bash
git clone https://github.com/thepenclaw/playwright-autoresearch-mlx-byoc-thepenclaw.git
cd playwright-autoresearch-mlx-byoc-thepenclaw

cd experiments/2026-03-10-playwright-m4-optimization
python3 scraper.py
```

## 10-Cycle Workflow

Use these docs for repeatable iteration:
- [10-cycle protocol](docs/PLAYWRIGHT_10_CYCLE_PROTOCOL.md)
- [report template](docs/PLAYWRIGHT_RESEARCH_REPORT_TEMPLATE.md)
- [add experiment guide](docs/ADD_EXPERIMENT.md)

The current cycle plan covers **100 unique websites** (10 per cycle). Each cycle runs every 15 minutes with the same desktop-focused Playwright config, so the agent observes performance variability across a wide spectrum of content, including OpenClaw memory/context discussions documented below.

## OpenClaw Context & Memory

The experiment also captures OpenClaw-relevant signal (memory pressure via `openclaw.ai`, latency `openai.com`, and related research links). See [docs/OPENCLAW_MEMORY_CONTEXT.md](docs/OPENCLAW_MEMORY_CONTEXT.md) for the issues we monitor and suggested mitigation strategies.

## Repository Layout

```text
playwright-autoresearch-mlx-byoc-thepenclaw/
├── README.md
├── ARCHITECTURE.md
├── docs/
│   ├── ADD_EXPERIMENT.md
│   ├── PLAYWRIGHT_10_CYCLE_PROTOCOL.md
│   └── PLAYWRIGHT_RESEARCH_REPORT_TEMPLATE.md
└── experiments/
    └── 2026-03-10-playwright-m4-optimization/
        ├── scraper.py
        ├── auto_run.sh
        ├── program.md
        ├── RESEARCH_REPORT.md
        └── results/
```

## Principles

- Keep test URL sets fixed per experiment.
- Change one variable class per cycle.
- Use score-driven decisions (`completeness / time`).
- Commit each cycle with a clear hypothesis.

## License

MIT - see [LICENSE](LICENSE).
