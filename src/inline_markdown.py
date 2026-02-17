from textnode import TextNode, TextType

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