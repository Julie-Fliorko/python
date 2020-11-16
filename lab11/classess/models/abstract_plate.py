from abc import ABC

from classess.models import abstract_tableware
from classess.models.how_to_wash import how_to_wash
from classess.models.tableware_type import TablewareType


class abstract_plate(abstract_tableware, ABC):
    def __init__(self, garantee_in_days: int, style: str, How_to_wash: how_to_wash, wieght_in_grams: int,
                 ability_to_microwave: bool,
                 manufacturer: str, colour: str, dessigned_for: str, material: str, tableware_type: TablewareType,
                 price: int, diameter_in_cm: int) -> None:
        abstract_tableware.__init__(self, garantee_in_days, style, How_to_wash, wieght_in_grams, ability_to_microwave,
                                    manufacturer, colour, dessigned_for, material, tableware_type, price)
        self.diameter_in_cm = diameter_in_cm

    def __init__(self, style: str, wieght_in_grams: int, colour: str, price: int, dessigned_for: str) -> None:
        abstract_tableware.__inint__(self, style, wieght_in_grams, colour, price, dessigned_for)
