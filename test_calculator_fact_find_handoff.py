import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CALC = (ROOT / 'calculator' / 'index.html').read_text()
FACT = (ROOT / 'fact-find.html').read_text()


class CalculatorFactFindHandoffTests(unittest.TestCase):
    def test_calculator_builds_prefilled_fact_find_link(self):
        self.assertIn('function buildFactFindPayload(result)', CALC)
        self.assertIn("source: 'exit_tax_calculator'", CALC)
        self.assertIn('business_location: jurisdictionToBusinessLocation(jurisdiction)', CALC)
        self.assertIn('business_structure: structureToFactFind(structure)', CALC)
        self.assertIn('profit: cleanNumber(ebitda)', CALC)
        self.assertIn('business_value: cleanNumber(businessValue)', CALC)
        self.assertIn('cgt_exposure: cleanNumber(exitTax)', CALC)
        self.assertIn('fact-find.html?prefill=', CALC)

    def test_calculator_shows_cta_after_calculation(self):
        self.assertIn('id="factFindCta"', CALC)
        self.assertIn('id="factFindLink"', CALC)
        self.assertIn('updateFactFindLink({ businessValue, capitalGain, exitTax });', CALC)

    def test_fact_find_accepts_and_applies_prefill_payload(self):
        self.assertIn('function getCalculatorPrefill()', FACT)
        self.assertIn('function applyCalculatorPrefill()', FACT)
        self.assertIn("params.get('prefill')", FACT)
        self.assertIn('base64UrlDecode(encoded)', FACT)
        self.assertIn('Object.entries(prefill).forEach(([name, value]) => setField(name, value));', FACT)
        self.assertIn('id="ff-prefill-banner"', FACT)


if __name__ == '__main__':
    unittest.main()
