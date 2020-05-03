from abc import ABC

from models.abstract_plate import abstract_plate
from models.how_to_wash import How_to_wash


class plane_plate(abstract_plate, ABC):
    def __init__(self, garantee_in_days: int, style: str, How_to_wash: How_to_wash, wieght_in_grams: int, ability_to_microwave: bool,
                 manufacturer: str, colour: str, dessigned_for: str, material: str, tableware_type: str, price: int, diameter_in_cm: int ) -> None:
        abstract_plate.__init__(self, garantee_in_days, style, How_to_wash, wieght_in_grams, ability_to_microwave,
                 manufacturer, colour, dessigned_for, material, tableware_type, price, diameter_in_cm)