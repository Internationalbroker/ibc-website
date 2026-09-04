import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).parent
BOOKING_URL = "https://api.leadconnectorhq.com/widget/booking/luxhuhhTHzXwvUyxVUw0"


class BookingCutoverTests(unittest.TestCase):
    def test_no_tracked_file_uses_calendly_urls_or_assets(self):
        names = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
        offenders = []
        for name in names:
            if not name or name == Path(__file__).name:
                continue
            try:
                text = (ROOT / name).read_text()
            except (UnicodeDecodeError, IsADirectoryError):
                continue
            if "calendly.com" in text.lower():
                offenders.append(name)
        self.assertEqual(offenders, [])

    def test_thanks_page_embeds_verified_ghl_calendar(self):
        html = (ROOT / "thanks.html").read_text()
        self.assertIn(f'src="{BOOKING_URL}"', html)
        self.assertNotIn("assets.calendly.com", html)


if __name__ == "__main__":
    unittest.main()
