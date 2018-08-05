from functools import reduce


class Node:

    def __init__(self, id='', threshold=0.5):
        self._id = id
        self._activation_values = []
        self._dissapation_multiplier = 0.6
        self._activation_threshold = threshold
        self._is_active = False
        self._input_nodes = set()
        self._output_nodes = set()

    def tick(self):
        self.degrade_activation(self._dissapation_multiplier)
        self.evaluate()

    def milli_tick(self):
        self.degrade_activation(0.98)
        self.evaluate()

    def degrade_activation(self, dissapation_factor):
        self._activation_values = list(filter(lambda act_val: act_val > 0,
                                              map(lambda act_val: round(act_val * dissapation_factor, 2),
                                                  self._activation_values)))
        # print('aftr', self._id, self._activation_values)

    def evaluate(self, param=None):
        #print('eval node', self._id, type(self))
        prev_active_state = self._is_active
        self._is_active = self.activation_level() > self._activation_threshold
        if self._is_active != prev_active_state:
            #print(self._id, self._is_active)
            self.evaluate_output_nodes(param)

    def is_active(self):
        return self._is_active

    def activate(self, value=1):
        self._activation_values.append(value)
        print('Activated ', self._id, self.activation_level())

    def activation_level(self):
        return reduce(lambda x, y: x+y, self._activation_values, 0)

    def publish_state(self, listner):
        listner(self, self.activation_level(), None)

    def add_input_nodes(self, nodes):
        self._input_nodes.update(nodes)

    def add_output_nodes(self, nodes):
        self._output_nodes.update(nodes)

    def evaluate_output_nodes(self, param):
        map(lambda node: node.evaluate(param), self._output_nodes)
