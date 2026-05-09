# nh-stock-analyzer Skill - Implementation Notes

## Overview

The `nh-stock-analyzer` skill provides comprehensive stock analysis dashboards with analyst consensus, price targets, and buy/hold/sell recommendations. It uses web search to gather current market data and renders an interactive HTML dashboard alongside prose analysis.

## How It Works

### Input
- Stock ticker (e.g., "MSFT", "AAPL")
- Company name (e.g., "Microsoft", "Apple")
- Casual inquiry (e.g., "How is Apple doing?")
- Investment decision prompt (e.g., "Should I buy Tesla for a 1-year hold?")

### Processing
1. **Search A** (price & momentum): Searches for `{TICKER} stock price analysis {current month} {current year}`
2. **Search B** (analyst targets): Searches for `{TICKER} stock analyst price target forecast {current year}`
3. **Data extraction**: Captures current price, performance metrics, consensus, targets, growth rates, risks, catalysts
4. **Signal calculation**: Applies scoring rubric to determine BUY/HOLD/SELL recommendation
5. **Dashboard rendering**: Generates interactive HTML widget with 6 sections

### Output
- **Dashboard widget** (100% width, responsive):
  - 4 metric cards (current price, 1-week %, 1-month %, 52-week high)
  - Analyst consensus bar chart
  - Price targets table
  - Trend strength indicators
  - Risk assessment with badges
  - Signal box with colored border and rationale
- **Prose summary** (4-6 paragraphs):
  - Price & momentum
  - What's driving it
  - Analyst view
  - 1-year outlook
  - Key risks
  - Signal rationale
- **Disclaimer**: "Not financial advice — please consult a licensed financial advisor for personalized guidance."

## Signal Generation Logic

The skill applies a **soft signal** rubric based on:

| Factor | Bullish | Neutral | Bearish |
|--------|---------|---------|---------|
| Analyst consensus | >70% Buy/Strong Buy | 40-70% | <40% |
| 1-month price vs. target | <90% of target | 90-105% | >105% |
| Revenue growth (YoY) | >20% | 5-20% | <5% |
| EPS growth | >20% | 0-20% | Declining |
| Institutional flows | Net inflows | Mixed | Net outflows |
| Macro/sector trend | Tailwind | Neutral | Headwind |

**Score thresholds**:
- ≥3 → BUY
- 1-2 → HOLD / cautious BUY
- 0 → HOLD
- ≤-1 → HOLD / cautious SELL or SELL

## Key Design Decisions

### Why Two Parallel Searches?
- Search A captures real-time momentum and price action
- Search B captures analyst consensus and fundamental targets
- Together, they provide complete picture for trading decision

### Why HTML Dashboard + Prose?
- **Dashboard** is fast to scan, visual, and actionable
- **Prose** provides context, citations, and nuance
- Combination serves both visual and analytical learners

### Why "Soft" Signal Language?
- Avoids overstating certainty ("cautious BUY" not "STRONG BUY")
- Acknowledges that past performance ≠ future results
- Encourages user to consult financial advisor
- Reduces liability for financial harm

### Why Cite Web Search Results?
- All quantitative claims (price, analyst targets, growth metrics) are traced to real sources
- Builds trust and allows users to verify claims
- Complies with copyright best practices (paraphrase with attribution)

## Common Issues & Solutions

### Issue: "Skill doesn't trigger on my stock query"
**Root cause**: Skill description may need optimization. Claude decides whether to trigger based on description + query fit.
**Solution**: Run description optimizer script (in skill-creator SKILL.md) to improve triggering language.

### Issue: "Dashboard doesn't render all elements"
**Root cause**: CSS variables not matching host environment, or widget code streaming incompletely.
**Solution**: Verify all colors use `var(--color-*)` CSS variables. Test in both light/dark modes.

### Issue: "Analyst targets are outdated"
**Root cause**: Search results returning stale data from aggregators.
**Solution**: Adjust search query to prioritize recent analyst notes (e.g., add "latest" or current month).

### Issue: "Stock price is wrong"
**Root cause**: Search data is delayed, or user ran query after market close.
**Solution**: Note in prose that prices are delayed by ~2 hours from market close. Suggest checking real-time tickers for live data.

## Technical Dependencies

- **Web Search Tool**: Required to fetch current market data
- **HTML/CSS**: For dashboard rendering (uses Tailwind + CSS variables)
- **Chart.js** (optional future enhancement): For trend visualization
- **Anthropic API**: The skill itself calls the API internally when creating Artifacts

## Performance Characteristics

- **Search latency**: ~5 seconds total (2 parallel searches, each ~2.5 seconds)
- **Dashboard render**: <1 second (HTML streaming)
- **Total response time**: 5-7 seconds from query to full output

## Limitations & Known Issues

### Data Scope
- Limited to stocks with analyst coverage (typically US-listed companies with market cap >$500M)
- Small-cap stocks may have sparse or missing analyst consensus
- Crypto, forex, commodities are outside scope (but could be extended)

### Timing
- Analyst targets are typically 3+ months old
- Price data is delayed ~2 hours from market close
- Earnings guidance may be outdated if company issues new guidance between analyst updates

### Geographic
- Primarily US stock market (NASDAQ, NYSE)
- Limited coverage of international exchanges

### Analyst Consensus
- Consensus reflects historical analyst ratings, may lag market sentiment
- Short-term momentum not reflected in longer-term targets

## Future Enhancement Ideas

1. **Intraday charts** — Add TradingView embed or Chart.js chart of intraday price action
2. **Options data** — Show call/put implied volatility, unusual activity
3. **Insider trading** — SEC Form 4 filings summary
4. **Short interest** — Track short volume, covering pressure
5. **Earnings calendar** — Next earnings date, expected EPS, historical beats
6. **Sector comparison** — How stock performs vs. peers and index
7. **ESG metrics** — Environmental, social, governance scores
8. **Dividend analysis** — Yield, payout ratio, coverage, growth history
9. **Valuation multiples** — P/E, P/B, P/S, PEG comparisons
10. **Earnings revisions** — Track if analysts are raising or lowering estimates

## Maintenance & Versioning

**Current Version**: 1.1 (May 2026)

**Change Log**:
- v1.0 — Initial release with 6-section dashboard and prose summary
- v1.1 — Dark mode, skills.sh publishing, prompt injection guardrails
- v1.2 (planned) — Sector comparison, ESG metrics

**Testing**: See `/testing/` directory for test suite, test cases, and evaluation framework.

## Attribution & Licensing

**Skill Author**: Navneet Hegde
**Skill Name**: nh-stock-analyzer
**Description**: Stock analysis with analyst consensus, price targets, and buy/hold/sell signals

For questions or to suggest improvements, refer to the `/testing/TESTING_QUICK_START.md` for validation approach and `/mnt/skills/examples/skill-creator/SKILL.md` for skill creation/modification framework.
