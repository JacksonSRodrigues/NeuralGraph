from node import Node

node_map = {}


def get_node(data):
    global node_map

    node = node_map.get(data)
    if node is None:
        node = Node()
        node.data = data
        node_map[data] = node

    return node


# node_1 = get_node('1')
# is_match, connected_nodes = node_1.is_relative_match('+')
# print(is_match)
# node_1.check_activation(False)
# print('-----------')

train_data = ['1', '+', '1', '=', '2']
test = ['1', '+', '1', '=']

previous_nodes = []
for character in train_data:
    node = get_node(character)
    node.input_nodes.extend(previous_nodes)
    for prev_node in previous_nodes:
        prev_node.output_nodes.append(node)

    is_match, connected_nodes = node.is_relative_match(character)
    if is_match:
        node.check_activation(has_match=is_match)

    previous_nodes.append(node)


# is_match, connected_nodes = node_1.is_relative_match('1')
# print(is_match)

# if is_match:
#    node_1.check_activation(has_match=is_match)
