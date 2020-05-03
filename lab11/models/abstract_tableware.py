from abc import ABC
from models.how_to_wash import How_to_wash


class abstract_tableware(ABC):

    def __init__(self, garantee_in_days: int, style: str, How_to_wash: How_to_wash, wieght_in_grams: int, ability_to_microwave: bool,
                 manufacturer: str, colour: str, dessigned_for: str, material: str, tableware_type: str, price: int) -> None:
        self.garantee_in_days = garantee_in_days
        self.style = style
        self.How_to_wash = How_to_wash
        self.wieght_in_grams = wieght_in_grams
        self.ability_to_microwave = ability_to_microwave
        self.manufacturer = manufacturer
        self.colour = colour
        self.dessigned_for = dessigned_for
        self.material = material
        self.tableware_type = tableware_type
        self.price = price
