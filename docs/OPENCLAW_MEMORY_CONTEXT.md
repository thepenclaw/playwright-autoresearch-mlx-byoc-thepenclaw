# OpenClaw Memory & Context Notes

This experiment targets desktop Playwright scraping but also tracks the kinds of memory/context challenges frequently reported by OpenClaw deployments. Each cycle visits 10 distinct websites (100 total across the run), surfacing:

- **Memory pressure spikes** when fetching feature-rich JavaScript-heavy pages (Stripe, Netflix-style dashboards, large docs). These mimic OpenClaw agents hitting large context windows.
- **Context drift** when the same config fetches wildly different DOM sizes (tiny docs vs. media-heavy landing pages). OpenClaw agents can suffer from stale context between cycles.

## Observed Behaviors
- The current config (`domcontentloaded`, 60s timeout, headless, desktop viewport) keeps Playwright working datasets within a narrow RAM footprint while still extracting ~67% completeness on average.
- Stripe `docs` and similar endpoints occasionally double the average cycle time (9–11s) without increasing completeness, highlighting that context growth is not proportional to useful data.

## Suggested mitigations
1. **Limit page scope per cycle**: keeping each cycle to 10 sites bounds the peak memory usage; analogous OpenClaw jobs can partition requests into batches that fit an available context window.
2. **Tune memory-heavy hooks**: avoid lengthy `wait_until` strategies that accumulate unused resource handles—in desktop Playwright we stick with `domcontentloaded`, which shortens resource retention and mirrors the memory-conscious OpenClaw scheduling mode.
3. **Monitor fetch latencies**: high-latency pages (Stripe) can provide early warning of context thrash. Logging their times (as `results/cycle_XX.json` does) lets the agent throttle or drop large payloads dynamically.
4. **Reuse contexts carefully**: when OpenClaw agents reuse a context for multiple URLs, make sure to `context.close()`/`browser.close()` between runs (the scraper already closes the browser after each URL, so the OS releases handles before the next cycle).

This document, the 10-cycle protocol, and the Playwright experiment results combine to give you both the operational data and the discussion points needed to diagnose OpenClaw-style memory/context issues in a BYOC environment.
