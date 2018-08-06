from nodes.node import Node
from functools import reduce


class AssociationNode(Node):

    def __init__(self, id='', threshold=0.5):
        super().__init__(id, threshold)

    def evaluate(self, param=None):
        prev_active_state = self._is_active
        self._is_active = reduce(lambda x, y: x & y,
                                 map(lambda node: node.is_active(),
                                     self._input_nodes), True)

        if prev_active_state != self._is_active & self._is_active:
            self.trigger_output_nodes()

    def trigger_output_nodes(self):
        #print('triggering output nodes')
        for node in self._output_nodes:
            node.activate()
        #map(lambda node: node.activate(), self._output_nodes)
