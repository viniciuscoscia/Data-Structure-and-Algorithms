class Road:
    def __init__(self, destination, distance: float):
        self.destination = destination
        self.distance = distance

    def __repr__(self):
        return f"Road(destination={self.destination.value}, distance={self.distance})"

    def __str__(self):
        return self.__repr__()
