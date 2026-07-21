import unittest
from pathlib import Path

ROOT = Path(__file__).parent
PUBLIC_PAGES = [
    "index.html",
    "about.html",
    "workwithme.html",
    "borderlessfounders.html",
    "thanks.html",
    "fact-find.html",
]
ENTITY = "COSTANZA AND SON LIMITED"
ADDRESS = "UNIT 1603, 16/F THE L. PLAZA, 367–375 QUEEN'S RD CENTRAL, SHEUNG WAN, HONG KONG"


class FooterLegalEntityTests(unittest.TestCase):
    def test_all_public_pages_show_exact_hong_kong_entity_and_address(self):
        for page in PUBLIC_PAGES:
            with self.subTest(page=page):
                html = (ROOT / page).read_text(encoding="utf-8")
                self.assertIn('class="footer-legal"', html)
                self.assertIn(ENTITY, html)
                self.assertIn(ADDRESS, html)

    def test_footer_legal_style_is_present(self):
        css = (ROOT / "css" / "style.css").read_text(encoding="utf-8")
        self.assertIn(".footer-legal", css)


if __name__ == "__main__":
    unittest.main()
