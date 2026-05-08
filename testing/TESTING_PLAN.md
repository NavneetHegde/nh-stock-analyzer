# nh-stock-analyzer Skill Testing Plan

## Overview
This document outlines the recommended testing approach for validating the `nh-stock-analyzer` skill before making it public. The skill provides stock analysis dashboards with analyst consensus, price targets, and buy/hold/sell recommendations.

---

## Phase 1: Unit Testing (Individual Components)

### 1.1 Web Search Data Collection
**Objective**: Verify that the skill successfully gathers all required data points

**Test Steps**:
- [ ] Run two parallel searches for a stock (price/momentum + analyst targets)
- [ ] Verify data extraction captures:
  - Current price and daily % change
  - 1-week, 1-month, 1-year performance
  - 52-week high/low
  - Analyst consensus breakdown (Strong Buy %, Buy %, Hold %, Sell %)
  - Average price target and range (bull/base/bear)
  - Revenue and EPS growth projections
  - Key catalysts and risks

**Success Criteria**:
- All 8+ data points extracted for each test stock
- Data is current (within 24 hours for price, within 3 months for analyst targets)
- No missing or null values for critical fields

---

### 1.2 Dashboard Widget Rendering
**Objective**: Verify the HTML dashboard renders correctly with all elements

**Test Steps**:
- [ ] Check that 4 metric cards render (current price, 1-week, 1-month, 52-week)
- [ ] Verify analyst consensus bars display percentages correctly
- [ ] Confirm price targets table shows all rows (avg, bull, base, bear, upside)
- [ ] Validate trend strength indicators appear with appropriate badges
- [ ] Confirm risk factors render with severity badges (green/amber/red)
- [ ] Check signal box displays with correct border color per recommendation

**Success Criteria**:
- All visual elements render in both light and dark modes
- Font sizes and spacing follow design system
- Numbers display with appropriate precision (no floating point artifacts)
- Colors use CSS variables (no hardcoded hex)

---

### 1.3 Signal Generation Logic
**Objective**: Verify the buy/hold/sell signal is correctly calculated

**Test Steps**:
- [ ] For stocks with >70% analyst buy consensus + growing revenue + positive momentum → Signal = BUY
- [ ] For stocks with 40-70% buy consensus + mixed signals → Signal = HOLD
- [ ] For stocks with <40% buy consensus + declining fundamentals → Signal = SELL or HOLD
- [ ] Check that signal rationale (1-2 sentences) explains the reasoning

**Success Criteria**:
- Signal aligns with rubric (page 6 of SKILL.md)
- Rationale references specific metrics shown on dashboard
- Signal is appropriate for the holding period mentioned (if applicable)

---

## Phase 2: Integration Testing (Skill Triggering)

### 2.1 Triggering on Stock Queries
**Objective**: Verify skill activates on relevant user inputs

**Test Prompts**:
```
1. "Analyze Apple stock (AAPL)"
2. "Should I buy Tesla?"
3. "Is Microsoft a good long-term hold?"
4. "Give me a breakdown of NVIDIA, AMD, and QCOM"
5. "How is the S&P 500 doing?"
6. "What's the current price of Bitcoin?"  [Should NOT trigger]
7. "Help me understand stock market investing" [Should NOT trigger]
```

**Success Criteria**:
- Skill triggers on queries 1-5 (stock-specific analysis)
- Skill does NOT trigger on queries 6-7 (general finance, no specific stock)
- Skill correctly identifies ticker from company name

---

### 2.2 Ticker Identification
**Objective**: Verify the skill correctly identifies stock tickers

**Test Prompts**:
```
1. "Apple" → AAPL ✓
2. "Microsoft" → MSFT ✓
3. "Tesla" → TSLA ✓
4. "Google" → GOOGL ✓
5. "Amazon" → AMZN ✓
6. "Meta" → META ✓
7. "Berkshire Hathaway" → BRK.A or BRK.B [Confirm handling]
8. "3M Company" → MMM ✓
9. "Best Buy" → BBY ✓
10. "Unknown Corp" → [Should indicate ticker not recognized]
```

**Success Criteria**:
- 90%+ accuracy on common company names
- Handles class A/B shares (BRK.A vs BRK.B)
- Gracefully handles unknown/ambiguous names

---

## Phase 3: Functional Testing (End-to-End Scenarios)

### 3.1 Critical Path Tests
Run these 3 tests and score on the evaluation framework (page 4 of test_cases.json):

**Test A: Basic Analysis (MSFT)**
```
User: "Analyze Microsoft stock (MSFT)"
Expected: Full dashboard + prose summary
Scoring: Dashboard Completeness (25), Data Accuracy (25), Signal Quality (20), Prose (15), Trigger (15)
Target Score: ≥85/100
```

**Test B: Investment Decision (TSLA)**
```
User: "I'm thinking about buying Tesla for a 1-year hold. Should I?"
Expected: Analysis tailored to 1-year outlook, risk assessment
Scoring: Same framework
Target Score: ≥85/100
```

**Test C: Casual Inquiry (AAPL)**
```
User: "How is Apple doing?"
Expected: Trend analysis, recent catalysts
Scoring: Same framework
Target Score: ≥80/100
```

---

### 3.2 Edge Cases
**Test**: Small-cap stock with limited analyst coverage (e.g., CRSP)
- Dashboard should note limited coverage
- Risk weighting should increase appropriately
- Signal should include caveats

**Test**: Pre-earnings stock
- Earnings date should be prominent in signal box
- Analysis should note upcoming catalyst
- Guidance should influence bull/base/bear scenarios

**Test**: Stock in major correction (>30% down in 1-month)
- Dashboard should show momentum accurately
- Risks should be highlighted
- Signal should reflect valuation opportunity or continued weakness

---

## Phase 4: Quality Assurance

### 4.1 Data Currency Check
For each test stock, verify:
- [ ] Price data is <2 hours old
- [ ] Analyst targets are from the past 3 months
- [ ] EPS/revenue estimates reflect latest guidance
- [ ] No stale data (e.g., citing 2025 as current year if test runs in 2026+)

### 4.2 Citation Accuracy
For each prose paragraph:
- [ ] Every quantitative claim is cited (e.g., "Azure grew 40% YoY" → linked to source)
- [ ] No unsourced assertions
- [ ] Quotes are <15 words and attributed correctly
- [ ] Sources are authoritative (company IR, major financial news, analyst reports)

### 4.3 Disclaimer Compliance
- [ ] Every output ends with: "Not financial advice — please consult a licensed financial advisor for personalized guidance."
- [ ] Soft signal language used ("cautious BUY" not "STRONG BUY")
- [ ] No guarantee language ("likely to" not "will")

---

## Phase 5: Benchmark Testing (Optional, Advanced)

### 5.1 Quantitative Comparison
If running with a baseline (older skill version or manual analysis):
```
Metric                          Target
─────────────────────────────────────────
Dashboard render time           <3 seconds
Data search latency             <5 seconds total
Widget loads in under 1 sec     100%
Signal matches analyst consensus >80%
Prose readability (Flesch-Kincaid) 8th grade level
Citation accuracy               >95%
```

### 5.2 Iteration Scoring
Track scores across test phases:

| Phase | Test Stock | Dashboard | Accuracy | Signal | Prose | Trigger | **Avg** |
|-------|-----------|-----------|----------|--------|-------|---------|--------|
| Phase 3A | MSFT | 25/25 | 24/25 | 19/20 | 14/15 | 15/15 | **97/100** |
| Phase 3B | TSLA | 24/25 | 23/25 | 18/20 | 14/15 | 15/15 | **94/100** |
| Phase 3C | AAPL | 25/25 | 25/25 | 20/20 | 15/15 | 15/15 | **100/100** |
| **Overall** | | | | | | | **≥90/100** |

**Decision Rule**: 
- Score ≥90/100 overall → Ready for public release
- Score 80-89/100 → Release with known limitations documented
- Score <80/100 → Return for iteration

---

## Checklist: Before Public Release

- [ ] All Phase 3 critical path tests scored ≥85/100
- [ ] No Phase 3A/B/C test scored <75/100
- [ ] Trigger accuracy verified on 10+ diverse prompts
- [ ] Data currency validated (price <2hr, targets <3mo, guidance <6mo)
- [ ] All citations verified and accurate
- [ ] Disclaimer present on every output
- [ ] Dashboard renders in both light and dark modes
- [ ] Skill description optimized for triggering (if using description-optimizer script)
- [ ] Edge cases documented (small-cap limitations, pre-earnings, etc.)
- [ ] User feedback incorporated (if beta testing)

---

## Running Tests in Practice

### Option A: Manual Testing (recommended for Claude.ai)
1. Copy the SKILL.md to your workspace
2. For each test prompt, run it with the skill
3. Review output against success criteria
4. Take screenshots of dashboard widget
5. Paste results into a spreadsheet with scores

### Option B: Automated Testing (requires Claude Code)
1. Create a Python script that:
   - Loads test_cases.json
   - Calls the Anthropic API with the skill context
   - Runs each test prompt
   - Evaluates output against criteria
   - Generates a report.json with scores

2. Run: `python evaluate_skill.py --skill nh-stock-analyzer --output report.json`

---

## Sign-Off Criteria

**Recommended by**: [Your name]
**Date Tested**: [Date]
**Overall Score**: [Final average across all critical tests]
**Status**: 
- [ ] Approved for public release
- [ ] Approved with documented limitations
- [ ] Requires further iteration

**Known Limitations**:
- [List any edge cases, missing features, or data limitations]

**Next Steps**:
- Package the skill and submit to Anthropic's registry
- Maintain version history (v1.0, v1.1, etc.) for future improvements
- Collect user feedback and log improvement requests

---

*This testing plan ensures the nh-stock-analyzer skill meets quality standards before public release.*
