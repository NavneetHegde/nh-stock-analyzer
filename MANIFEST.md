# nh-stock-analyzer Skill Package - File Manifest

## Directory Structure

```
nh-stock-analyzer/
│
├── SKILL.md
│   └── Main skill definition
│       - YAML frontmatter (name, description, etc.)
│       - Workflow: 5 steps (identify ticker, search, data extract, signal, render)
│       - Signal generation rubric
│       - Widget design rules
│       - Edge cases (unknown ticker, small-cap, crypto, etc.)
│       ~ 370 lines
│
├── README.md
│   └── User-facing overview
│       - Quick start (30 seconds)
│       - What you get (dashboard + prose)
│       - Testing instructions (45 min quick path)
│       - 5-point evaluation framework
│       - Workflow from package to public release
│       - Checklist before publishing
│       ~ 300 lines
│
├── testing/
│   │
│   ├── TESTING_QUICK_START.md ⭐ START HERE
│   │   └── 45-minute quick-start guide for validation
│   │       - Run 3 critical tests (MSFT, TSLA, NVDA)
│   │       - Scoring examples (95/100 vs 70/100)
│   │       - Release decision tree
│   │       - Key decision points & blockers
│   │       - Next steps after testing
│   │       ~ 400 lines
│   │
│   ├── TESTING_PLAN.md
│   │   └── Comprehensive 5-phase testing workflow
│   │       - Phase 1: Unit testing (web search, dashboard, signal logic)
│   │       - Phase 2: Integration testing (skill triggering, ticker ID)
│   │       - Phase 3: Functional testing (end-to-end scenarios)
│   │       - Phase 4: Quality assurance (data currency, citations, disclaimers)
│   │       - Phase 5: Benchmark testing (optional, advanced)
│   │       - Pre-release checklist
│   │       ~ 300 lines
│   │
│   ├── test_cases.json
│   │   └── 10 test scenarios in JSON format
│   │       - Test 001: Basic analysis (AAPL)
│   │       - Test 002: Company name recognition (TSLA)
│   │       - Test 003: 1-year hold decision (NVDA)
│   │       - Test 004: Casual inquiry (MSFT)
│   │       - Test 005: Comparison (META vs AMZN)
│   │       - Test 006: Earnings context (GOOG)
│   │       - Test 007: Sector analysis (NVDA, AMD, QCOM)
│   │       - Test 008: Unknown ticker edge case
│   │       - Test 009: Small-cap analysis
│   │       - Test 010: ETF analysis (QQQ)
│   │       - Evaluation framework (5 categories x 25 weights)
│   │       - Scoring rubric (excellent/good/acceptable/needs improvement)
│   │       ~ 200 lines
│   │
│   ├── test_results_template.json
│   │   └── Template for recording test scores
│   │       - Test ID, name, prompt, status
│   │       - 5-point scores: dashboard (25), accuracy (25), signal (20), prose (15), trigger (15)
│   │       - Total score, grade, observations, issues, improvements
│   │       - Summary metrics (tests run, passed/failed, average, median, min, max)
│   │       - Sign-off section (tester approved, date, notes)
│   │       ~ 120 lines
│   │
│   └── evaluate_skill.py
│       └── Python evaluation script (template)
│           - SkillEvaluator class with 5 validator methods
│           - validate_dashboard_completeness()
│           - validate_data_accuracy()
│           - validate_signal_quality()
│           - validate_prose_quality()
│           - validate_trigger_accuracy()
│           - evaluate_test_case() — comprehensive scoring
│           - generate_report() — summary statistics
│           - print_result() — formatted output
│           - CLI interface (--test-case, --all-tests, --generate-report)
│           ~ 350 lines
│
└── references/
    │
    ├── IMPLEMENTATION_NOTES.md
    │   └── Technical deep-dive
    │       - How it works (5-step process)
    │       - Input/output specification
    │       - Signal generation logic (rubric table)
    │       - Key design decisions (why two searches, why HTML+prose, etc.)
    │       - Common issues & solutions (troubleshooting)
    │       - Technical dependencies (Web Search, HTML/CSS, Anthropic API)
    │       - Performance characteristics (latency, render time)
    │       - Limitations (data scope, timing, geographic, analyst consensus)
    │       - Future enhancement ideas (10 ideas: charts, options, insider trading, etc.)
    │       - Maintenance & versioning (v1.0, v1.1 planned)
    │       - Attribution & licensing
    │       ~ 250 lines
    │
    └── [Future] references/ can include:
        - WORKFLOW.md — detailed step-by-step process
        - TROUBLESHOOTING.md — common errors and fixes
        - EXAMPLES.md — sample outputs for different stocks
        - API_SCHEMA.md — input/output format specification
```

## File Sizes & Purpose

| File | Size | Purpose | Audience |
|------|------|---------|----------|
| SKILL.md | 6 KB | Main skill definition | Claude engine |
| README.md | 8 KB | Overview & quick start | End users, testers |
| TESTING_QUICK_START.md | 15 KB | 45-min validation guide | Testers, skill owner |
| TESTING_PLAN.md | 9 KB | 5-phase detailed plan | QA engineers |
| test_cases.json | 7 KB | Test scenarios + rubric | Automated testing |
| test_results_template.json | 5 KB | Score tracking | Manual testing |
| evaluate_skill.py | 14 KB | Evaluation script | Automation experts |
| IMPLEMENTATION_NOTES.md | 8 KB | Technical reference | Developers, maintainers |

**Total package size**: ~72 KB (all text, no binaries)

## Key Files by Use Case

### I want to test this skill quickly (30 min)
1. Start with: `testing/TESTING_QUICK_START.md`
2. Run 3 tests from: `testing/test_cases.json`
3. Score with rubric in: `testing/TESTING_QUICK_START.md`
4. Make release decision

### I want comprehensive validation (3-4 hours)
1. Follow: `testing/TESTING_PLAN.md` (5 phases)
2. Use test cases: `testing/test_cases.json` (10 scenarios)
3. Track scores: `testing/test_results_template.json`
4. Analyze with: `testing/evaluate_skill.py`

### I want to understand how it works
1. Start with: `README.md` (features overview)
2. Deep dive: `references/IMPLEMENTATION_NOTES.md` (how it works, limitations, ideas)
3. Extend with: `references/` directory (future reference docs)

### I want to improve the skill
1. Read: `SKILL.md` (current implementation)
2. Check limitations: `references/IMPLEMENTATION_NOTES.md`
3. Plan improvements: Listed in IMPLEMENTATION_NOTES.md
4. Test changes: Use `testing/` framework

### I want to publish this skill
1. Run tests: `testing/TESTING_QUICK_START.md`
2. Update metadata: `SKILL.md` frontmatter
3. Add author: `SKILL.md` + `README.md`
4. Document limitations: `SKILL.md` description
5. Package: `package_skill.py` (external script)
6. Submit to Anthropic or distribute to users

## Progressive Disclosure Strategy

The package uses **3-level loading**:

1. **Level 1 — Metadata** (always in context)
   - File: SKILL.md frontmatter (name, description)
   - Size: <200 words
   - Purpose: Help Claude decide whether to trigger skill

2. **Level 2 — Main instructions** (loaded when skill triggers)
   - File: SKILL.md body
   - Size: <500 lines
   - Purpose: Guide Claude through the workflow

3. **Level 3 — Bundled resources** (as needed)
   - Folder: `testing/`, `references/`
   - Size: unlimited
   - Purpose: User reference, testing, improvement planning

This ensures:
- Skill description is concise and searchable
- SKILL.md is focused on core workflow
- Testing & reference materials available but not cluttering main skill
- Easy to extend with additional resources later

## Version History

- **v1.0** (May 2026)
  - Initial release with dashboard + prose
  - 10 test cases, 5-phase testing plan
  - Python evaluation script template
  - Comprehensive documentation

- **v1.1** (Planned)
  - Intraday price chart (Chart.js)
  - Earnings calendar
  - Improved data currency (real-time prices)

- **v1.2** (Planned)
  - Sector peer comparison
  - ESG metrics & dividend analysis
  - Options implied volatility

## How to Extend This Package

### Add a new test case
1. Add entry to `test_cases.json` with id, category, prompt, success criteria
2. Update test count in TESTING_QUICK_START.md
3. Document new test in TESTING_PLAN.md if applicable

### Add a new reference document
1. Create `references/NEW_TOPIC.md`
2. Link from README.md & SKILL.md
3. Update this MANIFEST.md

### Improve the evaluation script
1. Edit `testing/evaluate_skill.py`
2. Add new validator method (e.g., `validate_response_time()`)
3. Update scoring framework in script + test_cases.json

### Publish a new version
1. Bump version in `SKILL.md` frontmatter
2. Update `IMPLEMENTATION_NOTES.md` changelog
3. Add version note to `README.md`
4. Re-run test suite to ensure quality
5. Package with `package_skill.py`

---

**Total lines of documentation**: ~2,000 lines (guides, rubrics, reference)
**Estimated reading time**: 2-3 hours (skim), 6-8 hours (deep dive)
**Estimated testing time**: 45 min (quick), 3-4 hours (full suite)

This is a production-ready skill package with comprehensive testing framework and documentation.
