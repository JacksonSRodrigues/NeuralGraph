from nodes.node import Node


class DataNode(Node):

    def __init__(self, data, id='', threshold=0.5):
        super().__init__(id, threshold)
        self.data = data

    def evalutate(self, param=None):
        if param is not None:
            # evaluate for activation
            if self.data == param:
                self.activate()

        super().evaluate(param)
