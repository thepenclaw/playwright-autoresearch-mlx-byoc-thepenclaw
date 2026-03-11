#!/usr/bin/env python3
"""
Autoresearch Playwright - Scraping Experiment
Tests Playwright configurations for optimal speed/quality tradeoff
Modified by LLM agent each cycle
"""

import argparse
import time
import json
import sys
from datetime import datetime

# =============================================================================
# CONFIG - MODIFY THIS SECTION (Agent edits here)
# =============================================================================

CONFIG = {
    "wait_until": "domcontentloaded",  # FINAL: Best wait strategy
    "timeout": 60000,                   # FINAL: 60s optimal
    "headless": True,                   # FINAL: Headless is faster
    "viewport": {"width": 1280, "height": 720},  # FINAL: Desktop viewport
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.0",
}

# =============================================================================
# WEBSITE CORPUS
# =============================================================================

WEBSITE_CORPUS = [
    ("static_doc", "https://docs.python.org/3/"),
    ("react_spa", "https://react.dev/learn/"),
    ("forum", "https://news.ycombinator.com/"),
    ("productivity", "https://www.notion.com/"),
    ("ecommerce", "https://www.shopify.com/"),
    ("vue_docs", "https://vuejs.org/guide/"),
    ("social", "https://www.reddit.com/r/MachineLearning/"),
    ("api_docs", "https://stripe.com/docs"),
    ("github", "https://github.com/torvalds/linux"),
    ("blog", "https://blog.mozilla.org/en/mozilla/"),
    ("openclaw_home", "https://openclaw.ai/"),
    ("apple", "https://www.apple.com/"),
    ("microsoft", "https://www.microsoft.com/"),
    ("google", "https://www.google.com/"),
    ("openai", "https://openai.com/"),
    ("intel", "https://www.intel.com/"),
    ("nvidia", "https://www.nvidia.com/"),
    ("amd", "https://www.amd.com/"),
    ("arm", "https://www.arm.com/"),
    ("oracle", "https://www.oracle.com/"),
    ("nytimes", "https://www.nytimes.com/"),
    ("guardian", "https://www.theguardian.com/international"),
    ("bbc", "https://www.bbc.com/"),
    ("wsj", "https://www.wsj.com/"),
    ("reuters", "https://www.reuters.com/"),
    ("bloomberg", "https://www.bloomberg.com/"),
    ("cnn", "https://www.cnn.com/"),
    ("aljazeera", "https://www.aljazeera.com/"),
    ("techcrunch", "https://techcrunch.com/"),
    ("theverge", "https://www.theverge.com/"),
    ("wikipedia", "https://en.wikipedia.org/wiki/Main_Page"),
    ("arxiv_ai", "https://arxiv.org/list/cs.AI/recent"),
    ("paperswithcode", "https://paperswithcode.com/"),
    ("acl", "https://aclanthology.org/"),
    ("neurips", "https://nips.cc/"),
    ("icml", "https://icml.cc/"),
    ("sigkdd", "https://www.kdd.org/"),
    ("ieee", "https://ieeexplore.ieee.org/Xplore/home.jsp"),
    ("stackoverflow_playwright", "https://stackoverflow.com/questions/tagged/playwright"),
    ("github_actions", "https://github.com/actions"),
    ("docker", "https://www.docker.com/"),
    ("kubernetes", "https://kubernetes.io/"),
    ("aws", "https://aws.amazon.com/"),
    ("azure", "https://azure.microsoft.com/"),
    ("gcp", "https://cloud.google.com/"),
    ("digitalocean", "https://www.digitalocean.com/"),
    ("linode", "https://www.linode.com/"),
    ("kaggle", "https://www.kaggle.com/"),
    ("medium", "https://medium.com/"),
    ("github_docs", "https://docs.github.com/"),
    ("playwright_docs", "https://playwright.dev/docs/intro"),
    ("python_org", "https://www.python.org/"),
    ("ruby", "https://www.ruby-lang.org/en/"),
    ("rust", "https://www.rust-lang.org/"),
    ("golang", "https://golang.org/"),
    ("java", "https://www.java.com/en/"),
    ("dotnet", "https://dotnet.microsoft.com/"),
    ("tensorflow", "https://www.tensorflow.org/"),
    ("pytorch", "https://pytorch.org/"),
    ("huggingface", "https://huggingface.co/"),
    ("fastai", "https://www.fast.ai/"),
    ("designer_news", "https://www.designernews.co/"),
    ("product_hunt", "https://www.producthunt.com/"),
    ("indiegogo", "https://www.indiegogo.com/"),
    ("kickstarter", "https://www.kickstarter.com/"),
    ("etsy", "https://www.etsy.com/"),
    ("ebay", "https://www.ebay.com/"),
    ("amazon", "https://www.amazon.com/"),
    ("walmart", "https://www.walmart.com/"),
    ("target", "https://www.target.com/"),
    ("alibaba", "https://www.alibaba.com/"),
    ("tesla", "https://www.tesla.com/"),
    ("ford", "https://www.ford.com/"),
    ("gm", "https://www.gm.com/"),
    ("cisa", "https://www.cisa.gov/"),
    ("nasa", "https://www.nasa.gov/"),
    ("spacex", "https://www.spacex.com/"),
    ("blue_origin", "https://www.blueorigin.com/"),
    ("mit", "https://www.mit.edu/"),
    ("stanford", "https://www.stanford.edu/"),
    ("harvard", "https://www.harvard.edu/"),
    ("caltech", "https://www.caltech.edu/"),
    ("cambridge", "https://www.cam.ac.uk/"),
    ("oxford", "https://www.ox.ac.uk/"),
    ("khan_academy", "https://www.khanacademy.org/"),
    ("coursera", "https://www.coursera.org/"),
    ("edx", "https://www.edx.org/"),
    ("udacity", "https://www.udacity.com/"),
    ("linkedin", "https://www.linkedin.com/"),
    ("twitter", "https://twitter.com/"),
    ("github_trending", "https://github.com/trending"),
    ("devto", "https://dev.to/"),
    ("css_tricks", "https://css-tricks.com/"),
    ("smashingmag", "https://www.smashingmagazine.com/"),
    ("ars_technica", "https://arstechnica.com/"),
    ("wired", "https://www.wired.com/")
]

RESULTS_DIR = "results"
TSV_PATH = f"{RESULTS_DIR}/results.tsv"
WEBSITES_PER_CYCLE = 10

# =============================================================================
# SCRAPING FUNCTIONS
# =============================================================================

def scrape_with_playwright(url, config):
    """Scrape URL using Playwright with given config"""
    from playwright.sync_api import sync_playwright
    
    start_time = time.time()
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=config["headless"])
            context = browser.new_context(
                viewport=config["viewport"],
                user_agent=config["user_agent"]
            )
            page = context.new_page()
            
            page.goto(url, wait_until=config["wait_until"], timeout=config["timeout"])
            
            # Get full HTML
            html = page.content()
            
            browser.close()
            
            elapsed = time.time() - start_time
            return {"success": True, "html": html, "time": elapsed}
    
    except Exception as e:
        elapsed = time.time() - start_time
        return {"success": False, "error": str(e), "time": elapsed}

def extract_content(html):
    """Extract clean content from HTML using trafilatura"""
    try:
        import trafilatura
        text = trafilatura.extract(html, output_format="txt") or ""
        return len(text)
    except:
        # Fallback: simple text extraction
        import re
        text = re.sub(r'<[^>]+>', '', html)
        return len(text)

def estimate_full_content_size(url):
    """Estimate what 'complete' content looks like for this URL type"""
    # Static fetch gives us baseline
    import requests
    try:
        r = requests.get(url, timeout=10, headers={"User-Agent": CONFIG["user_agent"]})
        static_text = extract_content(r.text)
        return static_text * 1.5  # Assume JS adds ~50% more content
    except:
        return 5000  # Default estimate

def get_sites_for_cycle(cycle_index: int):
    """Return the ten sites assigned to a specific cycle."""
    start = (cycle_index - 1) * WEBSITES_PER_CYCLE
    end = start + WEBSITES_PER_CYCLE
    return WEBSITE_CORPUS[start:end]


def run_experiment(selected_sites, cycle_index):
    """Run scraping experiment on the selected subset (one cycle)."""
    results = []
    total_start = time.time()
    
    print("=" * 70)
    print(f"Playwright Autoresearch - Cycle {cycle_index} - {datetime.now().isoformat()}")
    print("=" * 70)
    print(f"\nConfig: {json.dumps(CONFIG, indent=2)}")
    print("\n" + "-" * 70)
    
    for i, (category, url) in enumerate(selected_sites):
        print(f"\n[{i+1}/{len(selected_sites)}] {category}: {url}")
        
        # Scrape with Playwright
        scrape_result = scrape_with_playwright(url, CONFIG)
        
        if not scrape_result["success"]:
            print(f"  ERROR: {scrape_result.get('error', 'Unknown')}")
            results.append({
                "category": category,
                "url": url,
                "success": False,
                "error": scrape_result.get("error")
            })
            continue
        
        # Extract content
        extracted_chars = extract_content(scrape_result["html"])
        estimated_full = estimate_full_content_size(url)
        
        # Calculate completeness (capped at 1.0)
        completeness = min(extracted_chars / max(estimated_full, 1), 1.0)
        
        # Calculate score for this URL
        url_score = completeness / max(scrape_result["time"], 0.1)
        
        result = {
            "category": category,
            "url": url,
            "success": True,
            "time_seconds": round(scrape_result["time"], 2),
            "html_size": len(scrape_result["html"]),
            "extracted_chars": extracted_chars,
            "completeness": round(completeness, 3),
            "score": round(url_score, 3)
        }
        
        results.append(result)
        
        print(f"  Time: {result['time_seconds']:.2f}s | "
              f"Chars: {result['extracted_chars']:,} | "
              f"Complete: {result['completeness']:.1%} | "
              f"Score: {result['score']:.3f}")
    
    total_time = time.time() - total_start
    
    # Calculate aggregate metrics
    successful = [r for r in results if r.get("success")]
    
    if successful:
        avg_time = sum(r["time_seconds"] for r in successful) / len(successful)
        avg_completeness = sum(r["completeness"] for r in successful) / len(successful)
        total_score = avg_completeness / max(avg_time, 0.1)
    else:
        avg_time = 0
        avg_completeness = 0
        total_score = 0
    
    summary = {
        "timestamp": datetime.now().isoformat(),
        "config": CONFIG,
        "total_urls": len(selected_sites),
        "successful": len(successful),
        "total_time": round(total_time, 2),
        "avg_time": round(avg_time, 2),
        "avg_completeness": round(avg_completeness, 3),
        "total_score": round(total_score, 3),
        "cycle_index": cycle_index,
        "results": results
    }
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Successful: {len(successful)}/{len(selected_sites)}")
    print(f"Total time: {total_time:.2f}s")
    print(f"Avg time per URL: {avg_time:.2f}s")
    print(f"Avg completeness: {avg_completeness:.1%}")
    print(f"TOTAL SCORE: {total_score:.3f}")
    
    # Save results
    cycle_num = len([f for f in __import__('os').listdir(RESULTS_DIR) if f.startswith('cycle_')]) + 1

    with open(f"{RESULTS_DIR}/cycle_{cycle_num:02d}.json", "w") as f:
        json.dump(summary, f, indent=2)

    # Append to TSV
    with open(TSV_PATH, "a") as f:
        if cycle_num == 1:
            f.write("cycle\ttimestamp\tscore\tavg_time\tcompleteness\tconfig\n")
        config_str = json.dumps(CONFIG)
        f.write(f"{cycle_num}\t{summary['timestamp']}\t{total_score:.3f}\t"
                f"{avg_time:.2f}\t{avg_completeness:.3f}\t{config_str}\n")
    
    print(f"\n✓ Results saved to results/cycle_{cycle_num:02d}.json")
    print(f"✓ Summary appended to results.tsv")
    
    return summary

def parse_args():
    parser = argparse.ArgumentParser(description="Playwright scraper cycle runner")
    parser.add_argument("--cycle", type=int, default=1,
                        help="Cycle index (1-10) to select the subset of websites")
    return parser.parse_args()


def main():
    args = parse_args()
    max_cycles = len(WEBSITE_CORPUS) // WEBSITES_PER_CYCLE
    if args.cycle < 1 or args.cycle > max_cycles:
        sys.exit(f"Cycle must be between 1 and {max_cycles}")

    selected_sites = get_sites_for_cycle(args.cycle)
    if not selected_sites:
        sys.exit("No websites configured for this cycle.")

    import os
    os.makedirs(RESULTS_DIR, exist_ok=True)
    run_experiment(selected_sites, args.cycle)


if __name__ == "__main__":
    main()
