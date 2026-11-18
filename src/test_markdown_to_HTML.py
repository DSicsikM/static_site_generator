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

    def test_unordered_list_renders_each_item(self):
        markdown = "- First item\n- **Second** item"

        self.assertEqual(
            markdown_to_html_node(markdown).to_html(),
            "<div><ul><li>First item</li><li><b>Second</b> item</li></ul></div>",
        )

    def test_ordered_list_renders_each_item(self):
        markdown = "1. First item\n2. **Second** item"

        self.assertEqual(
            markdown_to_html_node(markdown).to_html(),
            "<div><ol><li>First item</li><li><b>Second</b> item</li></ol></div>",
        )

    def test_quote_renders_as_blockquote(self):
        markdown = "> A quoted **statement**."

        self.assertEqual(
            markdown_to_html_node(markdown).to_html(),
            "<div><blockquote>A quoted <b>statement</b>.</blockquote></div>",
        )

    def test_heading_levels_one_through_six(self):
        markdown = (
            "# Heading one\n\n"
            "## Heading two\n\n"
            "### Heading three\n\n"
            "#### Heading four\n\n"
            "##### Heading five\n\n"
            "###### Heading six"
        )

        self.assertEqual(
            markdown_to_html_node(markdown).to_html(),
            "<div><h1>Heading one</h1><h2>Heading two</h2>"
            "<h3>Heading three</h3><h4>Heading four</h4>"
            "<h5>Heading five</h5><h6>Heading six</h6></div>",
        )


if __name__ == "__main__":
    unittest.main()
