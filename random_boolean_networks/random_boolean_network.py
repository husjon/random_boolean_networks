import logging
import random
import sys

from .node import Node
from .truth_table import TruthTable


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

        self.node_count = node_count
        self.neighbor_count = neighbor_count
        self.truth_table = truth_table or TruthTable(dimentions=neighbor_count)

        self.__nodes = []

        logging.debug(f'SEED:           {self.seed}')
        logging.debug(f'NODE COUNT:     {self.node_count}')
        logging.debug(f'NEIGHBOR_COUNT: {self.neighbor_count}')

    @property
    def nodes(self):
        return self.__nodes

    def setup(self):
        self.__nodes = []

        # Create nodes
        for i in range(self.node_count):
            node_id = str(i).rjust(len(str(self.node_count)), '0')
            _node = Node(name='node-' + node_id)
            self.__nodes.append(_node)

        # Give each node a set of neighboring nodes
        for _node in self.__nodes:
            node_neighbors = random.choices(
                population=self.__nodes,
                k=self.neighbor_count,
            )
            _node.connect(node_neighbors)

    def iterate(self):
        for node in self.__nodes:
            node.state = self.truth_table[node.current_state]['value']
