import random


class Node:
    def __init__(self, name=None, initial_state: bin = None):
        self.name = name
        self.state = initial_state or random.randint(0, 1)
        self.__peers = []

    @property
    def peers(self):
        return self.__peers

    def connect(self, peers: list):
        for peer in peers:
            self.__peers.append(peer)

    @property
    def current_state(self):
        state = [p.state for p in self.__peers]

        return sum(state)
