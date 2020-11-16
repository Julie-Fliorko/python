from abc import ABC

from classess.models.abstract_plate import abstract_plate
from classess.models.how_to_wash import how_to_wash
from classess.models.tableware_type import TablewareType


class bowl(abstract_plate, ABC):
    def __init__(self, style: str, wieght_in_grams: int, colour: str, price: int) -> None:
        abstract_plate.__init__(self, style, wieght_in_grams, colour, price)


"""

   def __init__(self, garantee_in_days: int, style: str, How_to_wash: how_to_wash, wieght_in_grams: int, ability_to_microwave: bool,
                 manufacturer: str, colour: str, dessigned_for: str, material: str, tableware_type: TablewareType, price: int, diameter_in_cm: int, depth_in_cm: int) -> None:
        abstract_plate.__init__(self, garantee_in_days, style, How_to_wash, wieght_in_grams, ability_to_microwave,
                 manufacturer, colour, dessigned_for, material, tableware_type, price, diameter_in_cm)
        self.depth_in_cm = depth_in_cm"""
