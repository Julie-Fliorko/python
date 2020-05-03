from abc import ABC

from models.abstract_tableware import abstract_tableware
from models.how_to_wash import How_to_wash


class abstract_plate(abstract_tableware, ABC):
    def __init__(self, garantee_in_days: int, style: str, How_to_wash: How_to_wash, wieght_in_grams: int, ability_to_microwave: bool,
                 manufacturer: str, colour: str, dessigned_for: str, material: str, tableware_type: str, price: int, diameter_in_cm: int ) -> None:
        abstract_tableware.__init__(self, garantee_in_days, style, How_to_wash, wieght_in_grams, ability_to_microwave,
                 manufacturer, colour, dessigned_for, material, tableware_type, price)
        self.diameter_in_cm = diameter_in_cm