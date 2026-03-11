# Playwright M4 Optimization Experiment

## Objective

Find the best Playwright scraping configuration on Apple Silicon M4 by maximizing:

`score = avg_completeness / avg_time_seconds`

## Files

- `scraper.py`: benchmark harness and score calculation.
- `program.md`: agent instructions and allowed edits.
- `auto_run.sh`: 10-cycle automation runner.
- `results/`: per-cycle JSON outputs.
- `results.tsv`: cycle summary log.
- `RESEARCH_REPORT.md`: final findings.

## Run One Trial

```bash
python3 scraper.py
```

## Run Full Loop

```bash
./auto_run.sh
```

Set `CYCLE_SLEEP_SECONDS` in shell to change cycle gap duration.
