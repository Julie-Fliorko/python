from abc import ABC

from classess.models import abstract_tableware
from classess.models.how_to_wash import how_to_wash
from classess.models.tableware_type import TablewareType


class knife(abstract_tableware, ABC):
    def __init__(self, garantee_in_days: int, style: str, How_to_wash: how_to_wash, wieght_in_grams: int, ability_to_microwave: bool,
                 manufacturer: str, colour: str, dessigned_for: str, material: str, tableware_type: TablewareType, price: int, diameter_in_cm: int, blade_type: str, sharpness: str, blade_leangth_in_cm: int) -> None:
        abstract_tableware.__init__(self, garantee_in_days, style, How_to_wash, wieght_in_grams, ability_to_microwave,
                 manufacturer, colour, dessigned_for, material, tableware_type, price)
        self.blade_type = blade_type
        self.sharpness = sharpness
        self.blade_leangth_in_cm = blade_leangth_in_cm