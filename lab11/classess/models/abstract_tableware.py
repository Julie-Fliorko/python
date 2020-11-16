from abc import ABC

import self as self

from classess.models.how_to_wash import how_to_wash
from classess.models.tableware_type import TablewareType


class abstract_tableware:

    def __init__(self, garantee_in_days: int, style: str, wieght_in_grams: int,
                 ability_to_microwave: bool,
                 manufacturer: str, colour: str, dessigned_for: str, material: str,
                 price: int) -> None:
        self.garantee_in_days = garantee_in_days
        self.style = style
        self.wieght_in_grams = wieght_in_grams
        self.ability_to_microwave = ability_to_microwave
        self.manufacturer = manufacturer
        self.colour = colour
        self.dessigned_for = dessigned_for
        self.material = material
        self.price = price

    def __int__(self, style: str, wieght_in_grams: int, colour: str, price: int):
        self.style = style
        self.wieght_in_grams = wieght_in_grams
        self.colour = colour
        self.price = price


    def __str__(self):
        garantee_in_days = "Garantee in days: {0}\n".format(self.garantee_in_days)
        style = "Style: {0}\n".format(self.style)
        wieght_in_grams = "Wieght in grams: {0}\n".format(self.wieght_in_grams)
        ability_to_microwave = "Ability to microwave: {0}\n".format(self.ability_to_microwave)
        manufacturer = "Manufacturer: {0}\n".format(self.manufacturer)
        colour = "colour: {0}\n".format(self.colour)
        dessigned_for = "Dessigned for: {0}\n".format(self.dessigned_for)
        material = "Material: {0}\n".format(self.material)
        price = "price: {0}\n".format(self.price)

    @property
    def garantee_in_days(self):
        return self.garantee_in_days

    @garantee_in_days.setter
    def garantee_in_days(self, garantee_in_days):
        self.garantee_in_days = garantee_in_days

    @property
    def style(self):
        return self.style

    @style.setter
    def garantee_in_days(self, style):
        self.style = style

    @property
    def wieght_in_grams(self):
        return self.wieght_in_grams

    @wieght_in_grams.setter
    def wieght_in_grams(self, wieght_in_grams):
        self.wieght_in_grams = wieght_in_grams

    @property
    def ability_to_microwave(self):
        return self.ability_to_microwave

    @ability_to_microwave.setter
    def ability_to_microwave(self, ability_to_microwave):
        self.ability_to_microwave = ability_to_microwave

    @property
    def manufacturer(self):
        return self.manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    @property
    def colour(self):
        return self.colour

    @colour.setter
    def colour(self, colour):
        self.colour = colour

    @property
    def dessigned_for(self):
        return self.dessigned_for

    @dessigned_for.setter
    def dessigned_for(self, dessigned_for):
        self.dessigned_for = dessigned_for

    @property
    def material(self):
        return self.material

    @material.setter
    def material(self, material):
        self.material = material

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, price):
        self.price = price