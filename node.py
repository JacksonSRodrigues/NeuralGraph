from threading import Timer


class Node:

    def __init__(self):
        self.data = None
        self.activation_value = 0
        self._timer = None
        self._timeout = 3  # millisecond
        self._activation_increment = 1
        self.input_nodes = []
        self.output_nodes = []
        self.active_till = None  # Mico/Mill Second after previous activation
        self.activation_condtions = []

    def activate_node(self, value):
        print('activating node {}'.format(self.data))
        if self._timer is not None:
            self._timer.cancel()
        self.activation_value += value
        self._timer = Timer(self._timeout, self.deactivate_node)
        self._timer.start()

    def deactivate_node(self):
        print('deactivating node {}'.format(self.data))
        self.activation_value = 0
        self._timer = None

    def is_active(self):
        return self.activation_value > 0

    def check_activation(self, has_match=False):
        # print('checking activation for {}'.format(self.data))
        # if activation conditions based on input node is activated then
        # value = map(lambda i: self.output_nodes[i].activation_value * self.output_weights[i], range(len(self.output_nodes)))
        if has_match:
            self.activate_node(self._activation_increment)
            self.transmit_state()
        elif self.has_any_triggerable_combination():
            self.activate_node(self._activation_increment)
            self.transmit_state()
        # else do nothing

    def has_any_triggerable_combination(self):
        return False

    def transmit_state(self):
        print('transmitting state from {}'.format(self.data))
        map(lambda node: node.check_activation(), self.output_nodes)

    def is_relative_match(self, data):
        if(Node.acess_match(self.data, data)):
            self.active_till
            return True, self.output_nodes
        else:
            return False, self.output_nodes

    @staticmethod
    def acess_match(data_1, data_2):
        return data_1 == data_2
