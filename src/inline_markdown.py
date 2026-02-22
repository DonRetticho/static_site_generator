from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for nodes in old_nodes:
        if nodes.text_type != TextType.TEXT:
            new_list.append(nodes)
        else:
            split_result = nodes.text.split(delimiter)

            if len(split_result) % 2 == 0:
                raise Exception("no valid markdown syntax")
            
            else:
                for i in range(len(split_result)):
                    if i % 2 == 0:
                        if split_result[i]:
                            new_list.append(TextNode(split_result[i], TextType.TEXT))
                    else:
                        if split_result[i]:
                            new_list.append(TextNode(split_result[i], text_type))

    return new_list

def split_nodes_image(old_nodes):
    new_list = []

    for nodes in old_nodes:
        if nodes.text_type != TextType.TEXT:
            new_list.append(nodes)
            continue

        else:
            extracted = extract_markdown_images(nodes.text)

            if len(extracted) == 0:
                new_list.append(nodes)
                continue
            else:
                original_text = nodes.text
                for image in extracted:
                    sections = original_text.split(f"![{image[0]}]({image[1]})", 1)

                    if sections[0] != "":
                        new_list.append(TextNode(sections[0], TextType.TEXT))
                    new_list.append(TextNode(image[0], TextType.IMAGE, image[1]))
                    original_text = sections[1]
                
                if original_text:
                    new_list.append(TextNode(original_text, TextType.TEXT))

    return new_list


    
def split_nodes_link(old_nodes):
    new_list = []

    for nodes in old_nodes:
        if nodes.text_type != TextType.TEXT:
            new_list.append(nodes)
            continue

        else:
            extracted = extract_markdown_links(nodes.text)

            if len(extracted) == 0:
                new_list.append(nodes)
                continue
            else:
                original_text = nodes.text
                for link in extracted:
                    sections = original_text.split(f"[{link[0]}]({link[1]})", 1)

                    if sections[0] != "":
                        new_list.append(TextNode(sections[0], TextType.TEXT))
                    new_list.append(TextNode(link[0], TextType.LINK, link[1]))
                    original_text = sections[1]
                
                if original_text:
                    new_list.append(TextNode(original_text, TextType.TEXT))

    return new_list

def text_to_textnodes(text):
    new_list = [TextNode(text, TextType.TEXT)]

    new_list = split_nodes_delimiter(new_list, "`", TextType.CODE)
    new_list = split_nodes_delimiter(new_list, "**", TextType.BOLD)
    new_list = split_nodes_delimiter(new_list, "_", TextType.ITALIC)
    new_list = split_nodes_image(new_list)
    new_list = split_nodes_link(new_list)

    return new_list

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"

    matches = re.findall(pattern, text)

    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

    matches = re.findall(pattern, text)

    return matches