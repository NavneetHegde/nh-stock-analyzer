# nh-stock-analyzer Skill - Testing Implementation Guide

## Executive Summary

This guide provides a **recommended testing approach** for the `nh-stock-analyzer` stock analysis skill before making it publicly available under your name.

**Key Deliverables**:
- ✅ 10 structured test cases covering critical, high, and edge scenarios
- ✅ 5-point evaluation framework (dashboard, accuracy, signal, prose, triggering)
- ✅ 5-phase testing plan (unit → integration → functional → QA → benchmarking)
- ✅ Scoring rubric with pass/fail criteria
- ✅ Python evaluation script template
- ✅ Test execution tracker

---

## Quick Start: Run These 3 Tests

If you only have 30 minutes, run these critical tests and score them:

### Test 1: MSFT Basic Analysis
```
Prompt: "Analyze Microsoft stock (MSFT)"
Time: ~2 minutes
Expected: Full dashboard + 6 paragraphs with 3+ citations
Scoring: Use the 5-point framework below
Target: ≥85/100
```

### Test 2: TSLA Investment Decision  
```
Prompt: "I'm thinking about buying Tesla for a 1-year hold. Should I?"
Time: ~2 minutes
Expected: Dashboard tailored to 1-year outlook with risk callouts
Scoring: Use the 5-point framework
Target: ≥85/100
```

### Test 3: AAPL Casual Inquiry
```
Prompt: "How is Apple doing?"
Time: ~2 minutes
Expected: Trend analysis, recent momentum, signal aligned
Scoring: Use the 5-point framework
Target: ≥80/100
```

**Release Decision**:
- If all 3 tests average ≥85/100 → Ready for public release
- If 2/3 average ≥85/100 → Release with limitations documented
- If fewer → Return for iteration

---

## Evaluation Framework (5 Categories)

Use this scoring rubric for every test. Each category is worth a certain percentage.

### 1. Dashboard Completeness (25 points)
Checks whether all visual elements render correctly.

- **Metric cards** (5 pts): Current price, 1-week %, 1-month %, 52-week high
- **Analyst consensus bars** (5 pts): Strong Buy %, Buy %, Hold %, Sell %
- **Price targets table** (5 pts): Average, bull, base, bear cases with upside
- **Trend indicators** (5 pts): Growth rates, earnings surprises, momentum badges
- **Risk factors** (3 pts): Key risks with severity badges (red/amber/green)
- **Signal box** (2 pts): Colored border matching recommendation, 1-2 sentence rationale

**Scoring**:
- All 6 elements present → 25/25
- 5 elements present → 20/25
- 4 elements present → 15/25
- 3 or fewer → 10/25

---

### 2. Data Accuracy (25 points)
Checks whether the data shown is correct and current.

- **Current price** (5 pts): Within ±0.5% of market price, <2 hours old
- **Analyst consensus** (5 pts): Percentages add to 100%, >90% accuracy
- **Price targets** (5 pts): Sourced from real analyst firms, within last 3 months
- **Growth metrics** (5 pts): Revenue/EPS YoY accurate, matches published guidance
- **Risk assessment** (5 pts): Reflects recent news, competitive landscape, macro trends

**Scoring**:
- 5/5 data points accurate → 25/25
- 4/5 accurate → 20/25
- 3/5 accurate → 15/25
- 2 or fewer accurate → 10/25 or less

---

### 3. Signal Quality (20 points)
Checks whether the buy/hold/sell recommendation is sound and well-reasoned.

- **Signal validity** (7 pts): Recommendation is BUY, HOLD, SELL, or SELL+BUY combination
- **Rationale** (6 pts): 1-2 sentences, clear logic, no longer (conciseness counts)
- **Data support** (7 pts): References analyst consensus, valuation, catalysts shown on dashboard

**Scoring**:
- Valid signal + concise rationale + full data support → 20/20
- Valid signal + rationale but weak support → 15/20
- Signal present but rationale vague or unsupported → 10/20
- Missing or invalid signal → 0-5/20

---

### 4. Prose Quality (15 points)
Checks the written summary paragraphs.

- **Structure** (5 pts): 4-6 paragraphs covering: momentum, drivers, analyst view, outlook, risks, signal
- **Citations** (5 pts): Every quantitative claim cited (≥3 citations minimum)
- **Disclaimer** (5 pts): Ends with "Not financial advice — consult a licensed advisor"

**Scoring**:
- Well-structured + 3+ good citations + disclaimer → 15/15
- Good structure + 2 citations + disclaimer → 12/15
- Adequate structure + 1 citation + no disclaimer → 8/15
- Poor structure or missing key elements → 5/15 or less

---

### 5. Trigger Accuracy (15 points)
Checks whether the skill activates appropriately and identifies tickers.

- **Appropriate triggering** (7 pts): Skill triggers on "buy/sell/analyze stock" queries, NOT on "what is the stock market?"
- **Ticker ID** (8 pts): Correctly identifies AAPL from "Apple", TSLA from "Tesla", etc.

**Scoring**:
- Correct trigger + accurate ticker ID → 15/15
- Correct trigger + ambiguous ticker handling → 12/15
- Trigger but wrong ticker → 8/15
- Doesn't trigger when it should → 0/15

---

## Test Case Library (10 Cases)

### Category: Basic Analysis
**Test 001** — Explicit ticker
```
Prompt: "Analyze Apple stock (AAPL)"
Expected: Full dashboard, all metrics, 6-paragraph summary, BUY/HOLD signal
Priority: CRITICAL
```

### Category: Company Name Recognition
**Test 002** — Company name only
```
Prompt: "Should I buy Tesla?"
Expected: Correctly identifies TSLA, provides investment decision framework
Priority: CRITICAL
```

### Category: Time-Bound Decision
**Test 003** — 1-year outlook
```
Prompt: "I'm thinking about investing in NVIDIA for a 1-year hold. Should I pull the trigger?"
Expected: Addresses 1-year bull/base/bear cases, highlights key risks for holding period
Priority: CRITICAL
```

### Category: Casual Inquiry
**Test 004** — Conversational tone
```
Prompt: "How is Microsoft doing?"
Expected: Trend analysis, recent catalysts, momentum assessment
Priority: HIGH
```

### Category: Comparison
**Test 005** — Two-stock comparison
```
Prompt: "Is Meta a better buy than Amazon right now?"
Expected: Side-by-side analysis of META vs AMZN, relative assessment
Priority: HIGH
```

### Category: Earnings Context
**Test 006** — Post-earnings analysis
```
Prompt: "Google just reported earnings. Is the stock fairly valued?"
Expected: Incorporates latest earnings, evaluates guidance impact, signals fairly valued/overvalued/undervalued
Priority: HIGH
```

### Category: Sector Analysis
**Test 007** — Multiple tickers
```
Prompt: "Give me a breakdown of the semiconductor stocks: NVIDIA, AMD, and QCOM"
Expected: Individual dashboards for all three, sector tailwind/headwind assessment
Priority: MEDIUM
```

### Category: Edge Case - Unknown Ticker
**Test 008** — Invalid/ambiguous ticker
```
Prompt: "What about XYZ123 stock?"
Expected: Gracefully indicates ticker not recognized, offers to search or clarify
Priority: MEDIUM
```

### Category: Small-Cap/Low Coverage
**Test 009** — Limited analyst coverage
```
Prompt: "Should I invest in a small biotech stock like CRSP?"
Expected: Notes limited analyst coverage, increases risk weighting, provides appropriate caveats
Priority: MEDIUM
```

### Category: ETF Analysis
**Test 010** — Index ETF
```
Prompt: "Is QQQ a good long-term hold?"
Expected: Provides analysis framework for ETF, notes composition and sector exposure
Priority: LOW
```

---

## Files Included

| File | Purpose |
|------|---------|
| **test_cases.json** | 10 test cases with success criteria and scoring framework |
| **TESTING_PLAN.md** | 5-phase plan: unit → integration → functional → QA → benchmarking |
| **test_results_template.json** | Template for recording scores from each test run |
| **evaluate_skill.py** | Python script skeleton for automated evaluation |
| **THIS FILE** | Quick-start guide and reference |

---

## Manual Testing Steps (Recommended for Claude.ai)

### Step 1: Prepare (5 minutes)
1. Copy `/mnt/skills/user/nh-stock-analyzer/SKILL.md` to your workspace
2. Open test_cases.json to review the 10 test prompts
3. Create a spreadsheet or use test_results_template.json to track scores

### Step 2: Run Test 001 (MSFT) (10 minutes)
1. Paste this into Claude: `/nh-stock-analyzer MSFT`
2. Wait for dashboard + prose to render
3. Check each criterion from the 5-point framework:
   - Are all 6 dashboard elements present? (dashboard_completeness)
   - Is data current and accurate? (data_accuracy)
   - Is the signal (BUY/HOLD/SELL) well-reasoned? (signal_quality)
   - Are there 4-6 paragraphs with 3+ citations? (prose_quality)
   - Did the skill trigger appropriately? (trigger_accuracy)
4. Score each out of its max points. Total should be /100.
5. Record in spreadsheet or JSON.

### Step 3: Run Test 002 (TSLA) (10 minutes)
Repeat Step 2 with: `Should I buy Tesla?`

### Step 4: Run Test 003 (NVDA) (10 minutes)
Repeat Step 2 with: `I'm thinking about investing in NVIDIA for a 1-year hold. Should I pull the trigger?`

### Step 5: Analyze Results (5 minutes)
- Average the three scores. Do you get ≥85/100 overall?
- Check if any score is <75/100 (that's a blocker for release).
- Note any bugs, missing data, or formatting issues.

### Step 6: Decide (1 minute)
- **≥85/100 average** → Ready to package and release publicly
- **75-84/100 average** → Document known limitations, release with caveats
- **<75/100** → Iterate on the skill, re-test, then release

---

## Scoring Examples

### Example: Score of 95/100 (EXCELLENT)
```
Test: MSFT Analysis
Dashboard:     25/25 ✓ (all 6 elements, perfect rendering)
Accuracy:      24/25 ✓ (price current, targets verified, 1 minor outdated guidance)
Signal:        19/20 ✓ (BUY signal well-reasoned, 2-sentence rationale)
Prose:         15/15 ✓ (6 paragraphs, 5 citations, strong disclaimer)
Trigger:       15/15 ✓ (appropriate trigger, MSFT correctly identified)
─────────────────────
TOTAL:         98/100 [EXCELLENT]
```

### Example: Score of 70/100 (NEEDS IMPROVEMENT)
```
Test: TSLA Analysis
Dashboard:     18/25 ✗ (missing trend indicators, signal box incomplete)
Accuracy:      20/25 ✓ (price good, analyst consensus correct, targets 2 months old)
Signal:        14/20 ~ (BUY signal valid but rationale unclear, no mention of 1-year outlook)
Prose:         11/15 ✗ (only 3 paragraphs, 1 citation, no disclaimer)
Trigger:       12/15 ~ (triggered correctly, but ticker ID showed ambiguity)
─────────────────────
TOTAL:         75/100 [ACCEPTABLE → Needs iteration]
```

---

## Key Decision Points

### Release Decision Tree

```
┌─ Run 3 Critical Tests (MSFT, TSLA, NVDA)
│
├─ Average Score ≥90?
│  └─ YES → EXCELLENT: Ready for public release ✅
│  └─ NO  → Continue...
│
├─ Average Score 80-89?
│  └─ YES → GOOD: Release with documented limitations ✅ (with caveats)
│  └─ NO  → Continue...
│
├─ Average Score 70-79?
│  └─ YES → ACCEPTABLE: Iterate on skill, retest, then release 🔄
│  └─ NO  → Continue...
│
└─ Average Score <70?
   └─ NEEDS IMPROVEMENT: Major revision required 🛑
```

### Release Blockers

If ANY test scores below 70/100, STOP and iterate. Specifically:
- **Data Accuracy <18/25**: Risk of providing false financial information
- **Signal Quality <12/20**: Recommendation logic is unsound
- **Prose Quality <10/15**: Missing disclaimer or citations = legal/compliance risk
- **Trigger <12/15**: Skill activates on wrong queries or misidentifies stocks

---

## Next Steps After Testing

### If Score ≥85/100 (Ready for Release)

1. **Package the skill**
   ```bash
   python /mnt/skills/examples/skill-creator/scripts/package_skill.py \
     /mnt/skills/user/nh-stock-analyzer
   ```

2. **Document attribution**
   - Add your name to SKILL.md frontmatter as `author: Your Name`
   - Add version info: `version: 1.0`

3. **Submit to Anthropic** (if they have a public registry)
   - Contact support@anthropic.com or check Anthropic docs
   - Provide packaged .skill file + test report

4. **Monitor and iterate**
   - Collect user feedback
   - Track bug reports
   - Plan v1.1 improvements

### If Score 75-84/100 (Conditional Release)

1. **Document limitations in SKILL.md description**
   ```markdown
   ---
   name: nh-stock-analyzer
   description: >
     Stock analysis skill. KNOWN LIMITATIONS:
     - Small-cap stocks (<$2B market cap) may have limited analyst coverage
     - Data is delayed by ~2 hours from market close
     - Pre-earnings stocks may not have forward guidance
   ---
   ```

2. **Add warning to output**
   - Include banner: "⚠️ This analysis is for educational purposes only."
   - Strengthen disclaimer language

3. **Plan for v1.1**
   - Track specific improvement requests
   - Schedule 2-week iteration cycle

### If Score <75/100 (Needs Iteration)

1. **Identify root causes**
   - Dashboard rendering: CSS/HTML issues?
   - Data accuracy: Search queries not retrieving latest data?
   - Signal logic: Rubric needs refinement?
   - Prose: Citation format, structure, tone?

2. **Prioritize fixes**
   - Fix blockers first (accuracy, disclaimer)
   - Then improve UI/UX (dashboard completeness)

3. **Retest key case (MSFT only)**
   - Should see immediate improvement
   - If still below 75, iterate again

---

## Estimated Time Investment

| Phase | Time | Effort |
|-------|------|--------|
| Quick start (3 tests) | 45 min | 👤 Manual |
| Full test suite (10 tests) | 3-4 hrs | 👤 Manual |
| Automated evaluation (Python) | 2-3 hrs | 👥 Setup |
| Description optimization | 30 min | 🤖 Script |
| Documentation & release prep | 1 hr | 👤 Admin |
| **TOTAL** | **6-8 hrs** | **Mixed** |

**Recommended approach**: Start with 3 critical tests (45 min). If score ≥85/100, go straight to release. If 75-84/100, run full 10 tests. Only use automated script if you run >20 tests.

---

## Support & Resources

- **Testing Plan**: See TESTING_PLAN.md for 5-phase detailed workflow
- **Test Cases**: See test_cases.json for all 10 test prompts
- **Evaluation Script**: See evaluate_skill.py (Python template)
- **Results Tracking**: Use test_results_template.json to record scores

---

## Final Checklist Before Publishing

Before you submit to Anthropic or make the skill public, verify:

- [ ] All 3 critical tests (001, 002, 003) scored ≥85/100
- [ ] No test scored <70/100
- [ ] Dashboard renders correctly in light AND dark modes
- [ ] Every financial claim has a citation (e.g., )
- [ ] Disclaimer present on every output
- [ ] Stock prices reflect data <2 hours old
- [ ] Analyst targets from last 3 months
- [ ] Signal logic documented and consistent with rubric
- [ ] Skill description optimized for triggering
- [ ] SKILL.md includes version number and author attribution

---