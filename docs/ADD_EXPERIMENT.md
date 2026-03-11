# Add a New Playwright Experiment

## 1. Create a dated folder

```bash
mkdir -p experiments/YYYY-MM-DD-your-experiment
cd experiments/YYYY-MM-DD-your-experiment
```

## 2. Add required files

- `scraper.py`: executable benchmark and scoring logic.
- `program.md`: agent mutation boundaries and objective.
- `auto_run.sh`: loop runner for multi-cycle execution.
- `RESEARCH_REPORT.md`: final write-up.
- `results/`: cycle JSON outputs.
- `results.tsv`: cycle summary table.

## 3. Reuse protocol and template

- Copy process from `docs/PLAYWRIGHT_10_CYCLE_PROTOCOL.md`.
- Start report from `docs/PLAYWRIGHT_RESEARCH_REPORT_TEMPLATE.md`.

## 4. Validate locally

```bash
python3 scraper.py
```

Ensure one cycle runs successfully before starting automated loops.
The prefab `scraper.py` already divides the 100-site corpus into 10-cycle batches; reuse or extend `WEBSITE_CORPUS` carefully so each cycle stays within 10 URLs (desktop, headless, `domcontentloaded`).

## 5. Commit and push

```bash
git add .
git commit -m "Add experiment: YYYY-MM-DD-your-experiment"
git push origin main
```
