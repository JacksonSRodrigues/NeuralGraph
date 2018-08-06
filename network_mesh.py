from nodes.node import Node
from nodes.data_node import DataNode
from nodes.association_node import AssociationNode
from stack import Stack


all_nodes = []
data_node_map = {}


def get_data_node(data):
    global data_node_map

    node = data_node_map.get(data)
    if node is None:
        node = DataNode(data, data)
        node.data = data
        data_node_map[data] = node
        all_nodes.append(node)

    return node


def get_association_node(input_nodes, output_nodes):
    print('new decision node')
    node = AssociationNode()
    node.add_input_nodes(input_nodes)
    node.add_output_nodes(output_nodes)
    all_nodes.append(node)
    return node


# node_1 = get_node('1')
# is_match, connected_nodes = node_1.is_relative_match('+')
# print(is_match)
# node_1.check_activation(False)
# print('-----------')


train_data = [[['1', '+', '2'], ['3']],
              [['1', '+', '3'], ['4']],
              [['2', '+', '3'], ['5']],
              [['2', '+', '4'], ['6']],
              [['3', '+', '4'], ['7']],
              [['1', '+', '2', '+', '4']]]
test = ['1', '+', '2']

train_letters = [[['1', 'in letters'], ['One']],
                 [['2', 'in letters'], ['Two']]]


def train_mesh(trainings):
    global all_nodes

    for training in trainings:
        print('===============================')
        previous_state = []
        for state in training:
            # do something
            for node in all_nodes:
                node.tick()
            # map(lambda node: node.tick(), all_nodes)
            previous_data = []
            is_new_data_active = True
            print('State =>', state)
            for data in state:
                for node in all_nodes:
                    node.milli_tick()
                # map(lambda node: node.milli_tick(), previous_data)
                data_node = get_data_node(data)
                is_new_data_active &= data_node.is_active()

                data_node.evalutate(data)

                previous_data.append(data_node)

            # decision node has not yet been made.
            if (not is_new_data_active) & len(previous_state) > 0:
                get_association_node(previous_state, previous_data)

            previous_state = previous_data

    for node in all_nodes:
        node.tick()


train_mesh(train_data)

# def reset_previous_nodes():
#     global previous_nodes
#     previous_nodes = []


# def reset_all_impulse():
#     global node_map
#     map(lambda node: node.deactivate_node(), node_map.values())


# activations = []


# def broadcast_firing(node, activation_strength, data):
#     global activations
#     activations.append(node)


# state_stack = Stack()
# train_data.reverse()
# state_stack.push_all(train_data)

# while not state_stack.isEmpty():
#     character = state_stack.pop()
#     node = get_node(character)
#     node.add_input_nodes(previous_nodes)
#     for prev_node in previous_nodes:
#         prev_node.add_output_nodes([node])

#     is_match, connected_nodes = node.is_relative_match(character)
#     if is_match:
#         node.check_activation(has_match=is_match)

#     previous_nodes.append(node)


# is_match, connected_nodes = node_1.is_relative_match('1')
# print(is_match)

# if is_match:
#    node_1.check_activation(has_match=is_match)
