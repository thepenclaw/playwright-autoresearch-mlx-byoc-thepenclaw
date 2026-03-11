#!/bin/bash
# Autoresearch Playwright - 10 Cycles
# Runs on M4 Mac automatically

cd "$(dirname "$0")"
REPO_DIR="$(pwd)"

echo "========================================"
echo "Autoresearch Playwright - Starting"
echo "Time: $(date)"
echo "Directory: $REPO_DIR"
echo "========================================"

# Check dependencies
if ! command -v python3 &> /dev/null; then
    echo "ERROR: python3 not found"
    exit 1
fi

# Install/check dependencies
echo "Checking dependencies..."
pip3 install -q playwright trafilatura requests 2>/dev/null || echo "Note: pip install may require user action"

# Check if playwright browsers are installed
if ! python3 -c "from playwright.sync_api import sync_playwright" 2>/dev/null; then
    echo "Installing Playwright browsers (one-time)..."
    python3 -m playwright install chromium
fi

# Sleep duration between cycles (default: 15 minutes)
CYCLE_SLEEP_SECONDS="${CYCLE_SLEEP_SECONDS:-900}"

# Run 10 cycles
for i in {1..10}; do
    echo ""
    echo "========================================"
    echo "CYCLE $i/10"
    echo "Started: $(date)"
    echo "========================================"
    
    # Pull latest code (in case Kimi pushed new config)
    echo "Pulling latest code..."
    git pull origin main
    
    # Run experiment
    echo "Running scraper.py (cycle $i)..."
    python3 scraper.py --cycle "$i"
    
    # Push results
    echo "Pushing results..."
    git add results/ scraper.py
    git commit -m "Cycle-$i results: $(date +%Y%m%d-%H%M%S)"
    git push origin main
    
    echo "Cycle $i complete!"
    
    # If not last cycle, sleep before the next cycle
    if [ $i -lt 10 ]; then
        NEXT_START="$(date -v+${CYCLE_SLEEP_SECONDS}S)"
        echo ""
        echo "Sleeping ${CYCLE_SLEEP_SECONDS}s until next cycle..."
        echo "Next cycle starts at: ${NEXT_START}"
        sleep "${CYCLE_SLEEP_SECONDS}"
    fi
done

echo ""
echo "========================================"
echo "ALL 10 CYCLES COMPLETE!"
echo "Finished: $(date)"
echo "========================================"
echo ""
echo "Final results in: results/results.tsv"
echo "Individual cycles in: results/"
