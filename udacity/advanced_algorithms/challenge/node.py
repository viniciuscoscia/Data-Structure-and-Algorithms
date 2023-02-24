from udacity.advanced_algorithms.challenge.road import Road


class Node:
    def __init__(self, value, g=0, h=0):
        self.parent = None
        self.value = value
        self.g = g
        """distance from start to current node"""
        self.h = h
        """distance from current node to goal"""
        self.roads: set[Road] = set()

    def add_road(self, road: Road):
        self.roads.add(road)

    def f(self):
        return self.g + self.h
