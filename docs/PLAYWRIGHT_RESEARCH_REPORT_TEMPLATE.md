# Playwright Autoresearch Report Template

## 1. Experiment Metadata

- Experiment: `YYYY-MM-DD-name`
- Date range: `YYYY-MM-DD to YYYY-MM-DD`
- Host machine: `Apple Silicon model + RAM`
- Python: `version`
- Playwright: `version`

## 2. Objective

State the optimization objective and primary metric.

## 3. Fixed Conditions

- URL corpus:
- Score function:
- Non-editable constraints:

## 4. Tested Configuration Space

List variables tested and allowed values.

## 5. Cycle Results Table

| Cycle | Change | Score | Avg Time (s) | Avg Completeness | Success/Total | Decision |
|------|--------|-------|--------------|------------------|---------------|----------|
| 1 |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |
| 6 |  |  |  |  |  |  |
| 7 |  |  |  |  |  |  |
| 8 |  |  |  |  |  |  |
| 9 |  |  |  |  |  |  |
| 10 |  |  |  |  |  |  |

## 6. Best Configuration

```python
CONFIG = {
    "wait_until": "",
    "timeout": 0,
    "headless": True,
    "viewport": {"width": 0, "height": 0},
    "user_agent": "",
}
```

## 7. Key Findings

- Finding 1:
- Finding 2:
- Finding 3:

## 8. Failure Analysis

List failed runs, outliers, and root-cause hypotheses.

## 9. Repro Steps

```bash
cd experiments/YYYY-MM-DD-name
python3 scraper.py
```

## 10. Conclusion

Summarize final recommendation and expected tradeoffs.
