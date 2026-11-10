import unittest
from regex_utilities import extract_markdown_images, extract_markdown_links

class TestRegexUtilities(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "![image1](url1) ![image2](url2)"
        expected_output = [("image1", "url1"), ("image2", "url2")]
        self.assertEqual(extract_markdown_images(text), expected_output)

    def test_extract_markdown_links(self):
        text = "[link1](url1) [link2](url2)"
        expected_output = [("link1", "url1"), ("link2", "url2")]
        self.assertEqual(extract_markdown_links(text), expected_output)

if __name__ == "__main__":
    unittest.main()