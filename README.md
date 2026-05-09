also add # nh-stock-analyzer Skill Package

A comprehensive stock analysis skill for Claude that delivers interactive dashboards with analyst consensus, price targets, and buy/hold/sell recommendations.

## 📦 Package Contents

```
nh-stock-analyzer/
├── SKILL.md                          # Main skill definition
├── README.md                         # This file
├── testing/                          # Testing framework & materials
│   ├── TESTING_QUICK_START.md       # 45-minute quick-start guide
│   ├── TESTING_PLAN.md              # 5-phase detailed testing workflow
│   ├── test_cases.json              # 10 test scenarios with rubric
│   ├── test_results_template.json   # Score tracking template
│   └── evaluate_skill.py            # Automated evaluation script
└── references/                       # Reference documentation
    └── IMPLEMENTATION_NOTES.md      # Technical deep-dive, limitations, future ideas
```

## 🚀 Quick Start (30 seconds)

### Install
1. Copy this entire directory to `/mnt/skills/user/nh-stock-analyzer/`
2. Claude will auto-discover it next chat

### Use
```
/nh-stock-analyzer MSFT
```
or naturally:
```
"Should I buy Microsoft?"
"How is Apple doing?"
"Is NVDA worth holding for a year?"
```

## 📊 What You Get

**Interactive dashboard** with:
- Current price & 52-week performance
- Analyst consensus breakdown (% Strong Buy / Buy / Hold / Sell)
- Price target range (bull/base/bear cases)
- Trend strength indicators (earnings, growth, momentum)
- Risk assessment with severity badges
- Buy/Hold/Sell signal with rationale

**Prose summary** with:
- 4-6 paragraphs covering momentum, drivers, analyst view, outlook, risks
- 3+ citations to market data sources
- Financial advice disclaimer

## ✅ Testing Before Public Release

This package includes a **complete testing framework** for validation.

### Option 1: Quick Validation (45 minutes)
1. Run the 3 critical tests in `testing/TESTING_QUICK_START.md`
2. Score each out of 100 using the 5-point rubric
3. Decision:
   - ≥85/100 average → **Ready for public release** ✅
   - 75-84/100 → Release with documented limitations
   - <75/100 → Iterate and retest

### Option 2: Full Test Suite (3-4 hours)
1. Follow the 5-phase plan in `testing/TESTING_PLAN.md`
2. Run all 10 test cases from `testing/test_cases.json`
3. Use `testing/test_results_template.json` to track scores
4. Generate report with `testing/evaluate_skill.py`

### Test Cases Include
- Basic stock analysis (explicit ticker)
- Company name recognition (e.g., "Should I buy Tesla?")
- Time-bound decisions (1-year hold assessment)
- Comparison queries (META vs AMZN)
- Earnings context analysis
- Small-cap/edge case handling

## 🎯 Evaluation Framework

The skill is scored on **5 categories** (100 points total):

| Category | Points | What It Measures |
|----------|--------|------------------|
| Dashboard Completeness | 25 | All UI elements render (metrics, consensus, targets, indicators, risks, signal) |
| Data Accuracy | 25 | Price current, analyst targets verified, growth metrics valid |
| Signal Quality | 20 | BUY/HOLD/SELL well-reasoned and supported by shown data |
| Prose Quality | 15 | 4-6 paragraphs with ≥3 citations + financial advice disclaimer |
| Trigger Accuracy | 15 | Activates on stock queries, correctly identifies ticker |

**Scoring rubric** and detailed criteria are in each test phase document.

## 🔍 Key Features

### Intelligent Ticker Recognition
- Identifies tickers from company names ("Apple" → AAPL, "Tesla" → TSLA)
- Handles ambiguous inputs gracefully
- Works with variations ("Berkshire Hathaway" → BRK.A/B)

### Context-Aware Analysis
- 1-year outlook for "hold" queries
- Risk assessment for small-cap stocks
- Earnings impact analysis for post-earnings context
- Sector comparison for multi-stock queries

### Data-Driven Recommendations
- Analyst consensus breakdown
- Institutional flows & momentum
- Revenue/EPS growth metrics
- Valuation relative to price targets

### Transparent Sourcing
- Every quantitative claim is cited
- Links to original sources (MarketBeat, TipRanks, Yahoo Finance, etc.)
- Paraphrased in own words (respects copyright)

## ⚙️ Technical Details

### Dependencies
- Web Search tool (required)
- HTML/CSS rendering (built-in)
- Anthropic API for internal Artifact calls

### Performance
- Search latency: ~5 seconds
- Dashboard render: <1 second
- Total response: 5-7 seconds

### Scope
- US-listed stocks with analyst coverage
- Market cap typically >$500M for good data
- Limited coverage for small-cap, crypto, forex

See `references/IMPLEMENTATION_NOTES.md` for limitations and future enhancements.

## 📝 Known Limitations

- **Data currency**: Analyst targets are 3+ months old, prices delayed ~2 hours
- **Coverage**: Limited to stocks with analyst consensus; small-cap stocks sparse
- **Timing**: Earnings guidance may be outdated if company issues new guidance
- **Scope**: US markets primarily; international limited

See full discussion in `references/IMPLEMENTATION_NOTES.md`.

## 🔄 Workflow: From Package to Public Release

### Step 1: Copy Files
```bash
cp -r nh-stock-analyzer /mnt/skills/user/
```

### Step 2: Run Tests (45 min)
```bash
# Follow TESTING_QUICK_START.md
# Run 3 critical tests (MSFT, TSLA, NVDA)
# Score each out of 100
# Average score ≥85? → Ready to release
```

### Step 3: Document Improvements (optional)
If score 75-84, add limitations to SKILL.md description:
```markdown
---
name: nh-stock-analyzer
description: >
  Stock analysis with analyst consensus and price targets.
  KNOWN LIMITATIONS:
  - Small-cap stocks (<$2B market cap) may have limited coverage
  - Data delayed ~2 hours from market close
  - Analyst targets are 3+ months old
---
```

### Step 4: Update Metadata
Edit the version number in SKILL.md frontmatter:
```yaml
---
name: nh-stock-analyzer
description: >
  Your improved description here
author: Navneet Hegde
version: 1.1
---
```

### Step 5: Package & Release
```bash
python build_skill.py
```


## 📚 Additional Resources

- **Skill-Creator Framework**: See `/mnt/skills/examples/skill-creator/SKILL.md` for best practices in creating & improving skills
- **Web Search Tool**: Anthropic docs on using web_search for current data
- **Anthropic Prompt Engineering**: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview


## ✨ Final Checklist Before Publishing

- [ ] All 3 critical tests (MSFT, TSLA, NVDA) scored ≥85/100
- [ ] No test scored <70/100
- [ ] Dashboard renders in light AND dark modes
- [ ] Every financial claim has a citation
- [ ] Disclaimer present on every output
- [ ] Stock prices <2 hours old
- [ ] Analyst targets from last 3 months
- [ ] SKILL.md has version number and author attribution

---

*nh-stock-analyzer v1.1 - May 2026*
