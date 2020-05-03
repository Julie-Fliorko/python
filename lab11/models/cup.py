from abc import ABC

from models.abstract_drinking_equipment import abstract_drinking_eqipment
from models.how_to_wash import How_to_wash


class cup(abstract_drinking_eqipment, ABC):
    def __init__(self,  garantee_in_days: int, style: str, How_to_wash: How_to_wash, wieght_in_grams: int, ability_to_microwave: bool,
                 manufacturer: str, colour: str, dessigned_for: str, material: str, tableware_type: str, price: int, size_in_ml: int, diameter_in_cm: int, heandles_type: str) -> None:
        abstract_drinking_eqipment.__init__(self, garantee_in_days, style, How_to_wash, wieght_in_grams, ability_to_microwave,
                 manufacturer, colour, dessigned_for, material, tableware_type, price, size_in_ml, diameter_in_cm)
        self.heandles_type = heandles_type