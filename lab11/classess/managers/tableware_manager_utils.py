import doctest

from classess.models import abstract_tableware
from classess.models.how_to_wash import how_to_wash
from classess.models.tableware_type import TablewareType


class tableware_manager_utils:
    @staticmethod
    def sort_by_price_DECS(tableware_list, reverse=True):
        """
        Test of correct founding tableware by type
        >>> first_item = abstract_tableware(120, "minimalist", how_to_wash.LIGHT_HAND_WASH, 450, True, "cutePlates", "white", "salad", "ceramics", TablewareType.PLATE, 100)
        >>> second_item = abstract_tableware(125, "minimalist", how_to_wash.LIGHT_HAND_WASH, 450, True, "cutePlates", "black", "soup", "ceramics", TablewareType.SPOON, 150)
        >>> third_item = abstract_tableware(120, "minimalist", how_to_wash.WASHING_MACHINE, 45, True, "cutePlates", "white", "salad", "metal", TablewareType.FORK, 200)

        >>> print(str(tableware_manager_utils.sort_by_price_DECS(([first_item, second_item, third_item])))) #doctest: +ELLIPSIS
        [AbstractTableware(...price=200...), AbstractTableware(...price=150...), AbstractTableware(...price=100...)]
        """
        return sorted(tableware_list, key=lambda product: product.price, reverse=reverse)

    @staticmethod
    def sort_by_price_acs(tableware_list, reverse=False):
        """
        Test of correct founding tableware by type
        >>> first_item = abstract_tableware(120, "minimalist", how_to_wash.LIGHT_HAND_WASH, 450, True, "cutePlates", "white", "salad", "ceramics", TablewareType.PLATE, 100)
        >>> second_item = abstract_tableware(125, "minimalist", how_to_wash.LIGHT_HAND_WASH, 450, True, "cutePlates", "black", "soup", "ceramics", TablewareType.SPOON, 150)
        >>> third_item = abstract_tableware(120, "minimalist", how_to_wash.WASHING_MACHINE, 45, True, "cutePlates", "white", "salad", "metal", TablewareType.FORK, 200)

        >>> print(str(tableware_manager_utils.sort_by_price_acs(([first_item, second_item, third_item])))) #doctest: +ELLIPSIS
        [AbstractTableware(...price=100...), AbstractTableware(...price=150...), AbstractTableware(...price=200...)]
        """
        return sorted(tableware_list, key=lambda product: product.price, reverse=reverse)

    @staticmethod
    def sort_by_weight_in_grams(tableware_list, reverse=True):
        """
        Test of correct founding tableware by type
        >>> first_item = abstract_tableware(120, "minimalist", how_to_wash.LIGHT_HAND_WASH, 450, True, "cutePlates", "white", "salad", "ceramics", TablewareType.PLATE, 100)
        >>> second_item = abstract_tableware(125, "minimalist", how_to_wash.LIGHT_HAND_WASH, 500, True, "cutePlates", "black", "soup", "ceramics", TablewareType.SPOON, 150)
        >>> third_item = abstract_tableware(130, "minimalist", how_to_wash.WASHING_MACHINE, 550, True, "cutePlates", "white", "salad", "metal", TablewareType.FORK, 200)

        >>> print(str(tableware_manager_utils.sort_by_weight_in_grams(([first_item, second_item, third_item])))) #doctest: +ELLIPSIS
        [AbstractTableware(...wieght_in_grams=550...), AbstractTableware(...wieght_in_grams=500...), AbstractTableware(...wieght_in_grams=450...)]
        """
        return sorted(tableware_list, key=lambda product: product.wieght_in_grams, reverse=reverse)


if __name__ == '__main__':

    doctest.testmod(verbose=True)
