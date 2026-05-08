#!/usr/bin/env python3
"""
Automated testing and evaluation script for nh-stock-analyzer skill.

Usage:
    python evaluate_skill.py --test-case test_001 --stock MSFT
    python evaluate_skill.py --all-tests
    python evaluate_skill.py --generate-report
"""

import json
import sys
import argparse
from datetime import datetime
from typing import Dict, List, Any, Optional

class SkillEvaluator:
    def __init__(self, test_cases_file: str = "test_cases.json"):
        """Initialize evaluator with test cases."""
        with open(test_cases_file, 'r') as f:
            self.test_suite = json.load(f)
        self.results = []
    
    def validate_dashboard_completeness(self, output: Dict[str, Any]) -> tuple[int, List[str]]:
        """
        Evaluate dashboard widget completeness.
        Returns: (score out of 25, list of findings)
        """
        score = 0
        findings = []
        
        # Check metric cards
        metric_cards = output.get('metric_cards', [])
        if len(metric_cards) == 4:
            score += 5
            findings.append("✓ 4 metric cards present")
        else:
            findings.append(f"✗ Expected 4 metric cards, found {len(metric_cards)}")
        
        # Check analyst consensus bars
        if output.get('analyst_consensus_bars'):
            score += 5
            findings.append("✓ Analyst consensus bars rendered")
        else:
            findings.append("✗ Analyst consensus bars missing")
        
        # Check price targets table
        if output.get('price_targets_table'):
            score += 5
            findings.append("✓ Price targets table present")
        else:
            findings.append("✗ Price targets table missing")
        
        # Check trend indicators
        if output.get('trend_indicators'):
            score += 5
            findings.append("✓ Trend strength indicators present")
        else:
            findings.append("✗ Trend indicators missing")
        
        # Check risk assessment
        if output.get('risk_factors'):
            score += 3
            findings.append("✓ Risk factors identified")
        else:
            findings.append("✗ Risk factors missing")
        
        # Check signal box
        if output.get('signal_box'):
            score += 2
            findings.append("✓ Signal box with colored border")
        else:
            findings.append("✗ Signal box missing")
        
        return min(score, 25), findings
    
    def validate_data_accuracy(self, output: Dict[str, Any], ticker: str) -> tuple[int, List[str]]:
        """
        Evaluate data accuracy and currency.
        Returns: (score out of 25, list of findings)
        """
        score = 0
        findings = []
        
        # Check current price
        if output.get('current_price'):
            score += 5
            findings.append(f"✓ Current price retrieved: ${output['current_price']}")
        else:
            findings.append("✗ Current price missing")
        
        # Check analyst consensus
        consensus = output.get('analyst_consensus', {})
        if consensus and sum(consensus.values()) > 0:
            score += 5
            findings.append(f"✓ Analyst consensus data: {consensus}")
        else:
            findings.append("✗ Analyst consensus data missing or invalid")
        
        # Check price targets
        targets = output.get('price_targets', {})
        if targets.get('average_target'):
            score += 5
            findings.append(f"✓ Price targets found (avg: ${targets['average_target']})")
        else:
            findings.append("✗ Price target data missing")
        
        # Check growth metrics
        metrics = output.get('growth_metrics', {})
        if metrics.get('revenue_growth') or metrics.get('eps_growth'):
            score += 5
            findings.append(f"✓ Growth metrics present: {metrics}")
        else:
            findings.append("✗ Growth metrics missing")
        
        # Check risk assessment
        if output.get('risk_assessment'):
            score += 5
            findings.append("✓ Risk assessment provided")
        else:
            findings.append("✗ Risk assessment missing")
        
        return min(score, 25), findings
    
    def validate_signal_quality(self, output: Dict[str, Any]) -> tuple[int, List[str]]:
        """
        Evaluate signal recommendation quality.
        Returns: (score out of 20, list of findings)
        """
        score = 0
        findings = []
        
        signal = output.get('signal', {})
        
        # Check signal recommendation
        valid_signals = ['BUY', 'HOLD', 'SELL']
        if signal.get('recommendation') in valid_signals:
            score += 7
            findings.append(f"✓ Valid signal: {signal['recommendation']}")
        else:
            findings.append(f"✗ Invalid or missing signal recommendation")
        
        # Check rationale length and quality
        rationale = signal.get('rationale', '')
        rationale_sentences = len([s for s in rationale.split('.') if s.strip()])
        
        if 1 <= rationale_sentences <= 3:
            score += 6
            findings.append(f"✓ Rationale is concise ({rationale_sentences} sentences)")
        else:
            findings.append(f"✗ Rationale should be 1-2 sentences (found {rationale_sentences})")
        
        # Check if signal is supported by data
        if signal.get('rationale') and (signal.get('recommendation') in output.get('analyst_consensus', {}) or 
                                        output.get('price_targets')):
            score += 7
            findings.append("✓ Signal rationale references dashboard data")
        else:
            findings.append("✗ Signal not clearly supported by shown data")
        
        return min(score, 20), findings
    
    def validate_prose_quality(self, output: Dict[str, Any]) -> tuple[int, List[str]]:
        """
        Evaluate prose summary quality.
        Returns: (score out of 15, list of findings)
        """
        score = 0
        findings = []
        
        prose = output.get('prose_summary', '')
        paragraphs = [p.strip() for p in prose.split('\n\n') if p.strip()]
        
        # Check paragraph count
        if 4 <= len(paragraphs) <= 6:
            score += 5
            findings.append(f"✓ Prose length appropriate ({len(paragraphs)} paragraphs)")
        else:
            findings.append(f"✗ Expected 4-6 paragraphs, found {len(paragraphs)}")
        
        # Check for citations
        citations = prose.count('= 3:
            score += 5
            findings.append(f"✓ Prose well-cited ({citations} citations)")
        else:
            findings.append(f"✗ Insufficient citations ({citations} found, ≥3 recommended)")
        
        # Check for disclaimer
        if 'financial advice' in prose.lower() or 'consult' in prose.lower():
            score += 5
            findings.append("✓ Financial advice disclaimer present")
        else:
            findings.append("✗ Missing financial advice disclaimer")
        
        return min(score, 15), findings
    
    def validate_trigger_accuracy(self, prompt: str, skill_triggered: bool, ticker_identified: Optional[str]) -> tuple[int, List[str]]:
        """
        Evaluate skill triggering and ticker identification.
        Returns: (score out of 15, list of findings)
        """
        score = 0
        findings = []
        
        # Check if skill triggered appropriately
        stock_related = any(word in prompt.lower() for word in ['stock', 'buy', 'sell', 'analyze', 'holding'])
        
        if stock_related and skill_triggered:
            score += 7
            findings.append("✓ Skill triggered on stock query")
        elif not stock_related and not skill_triggered:
            score += 7
            findings.append("✓ Skill correctly did not trigger on non-stock query")
        else:
            findings.append(f"✗ Incorrect trigger behavior (stock_query={stock_related}, triggered={skill_triggered})")
        
        # Check ticker identification
        if ticker_identified:
            score += 8
            findings.append(f"✓ Ticker correctly identified: {ticker_identified}")
        else:
            findings.append("✗ Ticker identification failed")
        
        return min(score, 15), findings
    
    def evaluate_test_case(self, test_id: str, output: Dict[str, Any], 
                          skill_triggered: bool = True, ticker_identified: Optional[str] = None) -> Dict[str, Any]:
        """
        Comprehensive evaluation of a test case.
        """
        test_case = next((t for t in self.test_suite['test_cases'] if t['id'] == test_id), None)
        if not test_case:
            return {"error": f"Test case {test_id} not found"}
        
        # Run all validators
        dashboard_score, dashboard_findings = self.validate_dashboard_completeness(output)
        accuracy_score, accuracy_findings = self.validate_data_accuracy(output, ticker_identified or "")
        signal_score, signal_findings = self.validate_signal_quality(output)
        prose_score, prose_findings = self.validate_prose_quality(output)
        trigger_score, trigger_findings = self.validate_trigger_accuracy(test_case['prompt'], skill_triggered, ticker_identified)
        
        # Calculate totals
        total_score = dashboard_score + accuracy_score + signal_score + prose_score + trigger_score
        
        # Determine grade
        if total_score >= 90:
            grade = "EXCELLENT"
        elif total_score >= 75:
            grade = "GOOD"
        elif total_score >= 60:
            grade = "ACCEPTABLE"
        else:
            grade = "NEEDS IMPROVEMENT"
        
        result = {
            "test_id": test_id,
            "test_name": test_case['category'],
            "timestamp": datetime.now().isoformat(),
            "scores": {
                "dashboard_completeness": dashboard_score,
                "data_accuracy": accuracy_score,
                "signal_quality": signal_score,
                "prose_quality": prose_score,
                "trigger_accuracy": trigger_score
            },
            "total_score": total_score,
            "grade": grade,
            "findings": {
                "dashboard": dashboard_findings,
                "accuracy": accuracy_findings,
                "signal": signal_findings,
                "prose": prose_findings,
                "trigger": trigger_findings
            }
        }
        
        self.results.append(result)
        return result
    
    def generate_report(self) -> Dict[str, Any]:
        """Generate comprehensive test report."""
        if not self.results:
            return {"error": "No results to report. Run tests first."}
        
        scores = [r['total_score'] for r in self.results]
        
        return {
            "report_date": datetime.now().isoformat(),
            "total_tests_run": len(self.results),
            "average_score": sum(scores) / len(scores) if scores else 0,
            "median_score": sorted(scores)[len(scores)//2] if scores else 0,
            "min_score": min(scores) if scores else 0,
            "max_score": max(scores) if scores else 0,
            "grades": {
                "EXCELLENT": len([r for r in self.results if r['grade'] == 'EXCELLENT']),
                "GOOD": len([r for r in self.results if r['grade'] == 'GOOD']),
                "ACCEPTABLE": len([r for r in self.results if r['grade'] == 'ACCEPTABLE']),
                "NEEDS IMPROVEMENT": len([r for r in self.results if r['grade'] == 'NEEDS IMPROVEMENT'])
            },
            "test_results": self.results,
            "ready_for_release": sum(scores) / len(scores) >= 85 if scores else False
        }
    
    def print_result(self, result: Dict[str, Any]):
        """Pretty print a test result."""
        print(f"\n{'='*60}")
        print(f"Test: {result['test_id']} - {result['test_name']}")
        print(f"{'='*60}")
        print(f"Dashboard Completeness: {result['scores']['dashboard_completeness']}/25")
        print(f"Data Accuracy:          {result['scores']['data_accuracy']}/25")
        print(f"Signal Quality:         {result['scores']['signal_quality']}/20")
        print(f"Prose Quality:          {result['scores']['prose_quality']}/15")
        print(f"Trigger Accuracy:       {result['scores']['trigger_accuracy']}/15")
        print(f"-" * 60)
        print(f"TOTAL SCORE: {result['total_score']}/100 [{result['grade']}]")
        print(f"{'='*60}")
        
        for category, findings in result['findings'].items():
            print(f"\n{category.upper()}:")
            for finding in findings:
                print(f"  {finding}")


def main():
    parser = argparse.ArgumentParser(description="Evaluate nh-stock-analyzer skill")
    parser.add_argument('--test-case', help='Specific test case ID to run')
    parser.add_argument('--all-tests', action='store_true', help='Run all test cases')
    parser.add_argument('--generate-report', action='store_true', help='Generate summary report')
    
    args = parser.parse_args()
    
    evaluator = SkillEvaluator()
    
    if args.test_case:
        print(f"Running test case: {args.test_case}")
        # Example: You would call the skill and capture output here
        # For now, just a placeholder
        print("This script is a template. Add actual API calls to evaluate the skill.")
    elif args.all_tests:
        print("Running all test cases...")
        print("This script is a template. Add actual API calls to evaluate the skill.")
    elif args.generate_report:
        if evaluator.results:
            report = evaluator.generate_report()
            print(json.dumps(report, indent=2))
        else:
            print("No test results available. Run tests first.")
    else:
        print("Usage: python evaluate_skill.py [--test-case ID | --all-tests | --generate-report]")


if __name__ == '__main__':
    main()
