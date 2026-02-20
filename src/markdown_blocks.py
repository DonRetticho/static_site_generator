from enum import Enum
from htmlnode import HTMLNode, ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
from inline_markdown import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    new_list = []

    raw_blocks = markdown.split("\n\n")

    for b in raw_blocks:
        b = b.strip()
        if b != "":
            new_list.append(b)

    return new_list

def block_to_block_type(markdown_block):

    if markdown_block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if markdown_block.startswith("```\n") and markdown_block.endswith("```"):
        return BlockType.CODE

    lines = markdown_block.split("\n")
    
    is_quote = True
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
    if is_quote:
        return BlockType.QUOTE
    
    if markdown_block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    
    if markdown_block.startswith(f"1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

def text_to_children(text):
    html_nodes = []
    textnode_list = text_to_textnodes(text)

    for node in textnode_list:
        html_nodes.append(text_node_to_html_node(node))

    return html_nodes
    
def markdown_to_html_node(markdown):
    everything = []
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            children = text_to_children(block)
            everything.append(ParentNode("p", children))

        if block_type == BlockType.HEADING:
            parts = block.split(" ")
            tag_string = f"h{len(parts[0])}"
            text_content = " ".join(parts[1:])
            children = text_to_children(text_content)
            everything.append(ParentNode(tag_string, children))

        if block_type == BlockType.QUOTE:
            lines = block.split("\n")
            stripped_lines = []
            for line in lines:
                stripped_lines.append(line.lstrip("> "))

            joined = " ".join(stripped_lines)

            children = text_to_children(joined)
            everything.append(ParentNode("blockquote", children))

        if block_type == BlockType.CODE:
            stripped = block[3:-3]
            text_node = TextNode(stripped, TextType.TEXT)
            html_node = text_node_to_html_node(text_node)
            code_node = ParentNode("code", [html_node])
            pre_node = ParentNode("pre", [code_node])
            everything.append(pre_node)

        if block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            li_nodes = []
            for line in lines:
                text = line[2:]
                children = text_to_children(text)
                li_nodes.append(ParentNode("li", children))
            everything.append(ParentNode("ul", li_nodes))

        if block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            li_nodes = []
            for line in lines:
                text = line.split(". ", 1)[1]
                children = text_to_children(text)
                li_nodes.append(ParentNode("li", children))
            everything.append(ParentNode("ol", li_nodes))

    return ParentNode("div", everything)