import logging
import random
import sys

from node import Node
from truth_table import TruthTable


class RandomBooleanNetwork:
    def __init__(self,
                 node_count: int = 20,
                 neighbor_count: int = 3,
                 truth_table: TruthTable = None,
                 seed: int = None):
        """
        Args:
            node_count (int):       Number of nodes
            neighbor_count (int):   Number of neighbor each node will have
        """


        self.seed = seed or random.randrange(sys.maxsize)
        random.seed(self.seed)
        logging.debug(f'SEED: {self.seed}')



        self.node_count = node_count
        self.neighbor_count = neighbor_count
        self.truth_table = truth_table or TruthTable(dimentions=neighbor_count)

        self.__nodes = []

    @property
    def nodes(self):
        return self.__nodes

    def setup(self):
        self.__nodes = []

        for i in range(self.node_count):
            node_id = str(i).rjust(len(str(self.node_count)), '0')
            _node = Node(name='node-' + node_id)
            self.__nodes.append(_node)

        for _node in self.__nodes:
            node_neighbors = random.choices(
                population=self.__nodes,
                k=self.neighbor_count,
            )
            _node.connect(node_neighbors)

    def iterate(self):
        current_states = {}
        for node in self.__nodes:
            current_states[node.name] = node.current_state

        for node in self.__nodes:
            new_state = self.truth_table[current_states[node.name]]['value']
            node.state = new_state

        del (current_states)
