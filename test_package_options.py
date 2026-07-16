import pathlib
import unittest

HTML = pathlib.Path('calculator/index.html').read_text()

class PackageOptionsTest(unittest.TestCase):
    def test_package_controls_exist(self):
        self.assertIn('id="packageMode"', HTML)
        self.assertIn('value="both"', HTML)
        self.assertIn('value="concierge_only"', HTML)
        self.assertIn('id="selfSteerPrice"', HTML)
        self.assertIn('id="conciergePrice"', HTML)

    def test_results_can_show_concierge_only_without_self_steer(self):
        self.assertIn('function buildPackageRecommendation', HTML)
        self.assertIn("packageMode === 'concierge_only'", HTML)
        self.assertIn('We hold your hand through establishing the companies', HTML)
        concierge_only_block = HTML.split("if (packageMode === 'concierge_only')", 1)[1].split('return `', 2)[1].split('`;', 1)[0]
        self.assertNotIn('Self-Steer', concierge_only_block)
        self.assertNotIn('2+ entities', concierge_only_block)
        self.assertIn('High-touch implementation support', concierge_only_block)
        self.assertIn('Co-ordinate with your current home accountant', concierge_only_block)
        self.assertIn('Payment provider set ups', concierge_only_block)
        self.assertIn('Assist with guiding on intercompany / transfer pricing arrangements', concierge_only_block)
        self.assertIn('Assist with local services such as insurance, license and visa', concierge_only_block)

    def test_custom_prices_drive_fee_and_payload(self):
        self.assertIn('function getPackagePrices', HTML)
        self.assertIn("parseMoneyInput('selfSteerPrice', 8000)", HTML)
        self.assertIn("parseMoneyInput('conciergePrice', 12000)", HTML)
        self.assertIn('selectedPackageFee', HTML)
        self.assertIn('Recommended package mode:', HTML)

if __name__ == '__main__':
    unittest.main()
