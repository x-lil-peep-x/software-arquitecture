from FloatingFloorBuilder import FloatingFloorBuilder
from MelamineFloor import MelamineFloor
from Price import Price
from Thickness import Thickness

class MelamineFloorBuilder(FloatingFloorBuilder):

    def __init__(self, millimetre, placement, color):
        super().__init__(millimetre, placement, color)

    def create_floor(self):
        self.floor = MelamineFloor()

    def build_thickness(self):
        thickness = Thickness(self.millimetre, Price(10))
        self.floor.set_thickness(thickness)

