import unittest

from markdown_to_HTML import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_empty_markdown_returns_empty_div(self):
        self.assertEqual(markdown_to_html_node("").to_html(), "<div></div>")

    def test_multiple_paragraphs_are_separate_and_trimmed(self):
        markdown = "\nFirst paragraph.\n\nSecond paragraph.\n"

        self.assertEqual(
            markdown_to_html_node(markdown).to_html(),
            "<div><p>First paragraph.</p><p>Second paragraph.</p></div>",
        )

    def test_paragraph_converts_multiple_inline_formats(self):
        markdown = "**bold** and _italic_ with `code`."

        self.assertEqual(
            markdown_to_html_node(markdown).to_html(),
            "<div><p><b>bold</b> and <i>italic</i> with <code>code</code>.</p></div>",
        )

    def test_multiline_code_block_is_preserved(self):
        markdown = """```
This is text that _should_ remain
the **same** even with inline stuff
```"""
        expected = (
            "<div><pre><code>This is text that _should_ remain\n"
            "the **same** even with inline stuff\n</code></pre></div>"
        )

        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_paragraphs_before_and_after_code_block_remain_separate(self):
        markdown = "Before.\n\n```\nraw *code*\n```\n\nAfter."

        self.assertEqual(
            markdown_to_html_node(markdown).to_html(),
            "<div><p>Before.</p><pre><code>raw *code*\n</code></pre>"
            "<p>After.</p></div>",
        )

    def test_empty_code_block_renders_empty_code_element(self):
        markdown = "```\n```"

        self.assertEqual(
            markdown_to_html_node(markdown).to_html(),
            "<div><pre><code></code></pre></div>",
        )

    def test_inline_code_remains_an_inline_code_element(self):
        markdown = "A `code` span"

        self.assertEqual(
            markdown_to_html_node(markdown).to_html(),
            "<div><p>A <code>code</code> span</p></div>",
        )


if __name__ == "__main__":
    unittest.main()
