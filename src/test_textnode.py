import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("test that the url is equal", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("test that the url is equal", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("test that they are not equal", TextType.CODE)
        node2 = TextNode("test that they are not equal", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("test that the url is equal", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("test that the url is equal", TextType.ITALIC)#, "https://www.google.com")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

if __name__ == "__main__":
    unittest.main()