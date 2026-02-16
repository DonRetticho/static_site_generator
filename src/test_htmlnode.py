import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
        expected = ' href="https://google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_none(self):
        node = HTMLNode()
        expected = ""
        self.assertEqual(node.props_to_html(), expected)

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(props={"href": "https://google.com", "target": "blank"})
        self.assertEqual(
            "HTMLNode(None, None, None, {'href': 'https://google.com', 'target': 'blank'})", repr(node)
        )

if __name__ == "__main__":
    unittest.main()