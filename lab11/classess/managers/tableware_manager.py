import doctest

from classess.models import how_to_wash
from classess.models import abstract_tableware
from classess.models.tableware_type import TablewareType
from classess.models.how_to_wash import how_to_wash


class tableware_manager:

    def __init__(self, tableware_list=[]):
        self.tableware_list = tableware_list

    def find_tableware_by_type(self, tableware_type: TablewareType):
        """
        Test of correct founding tableware by type
        >>> first_item = abstract_tableware(120, "minimalist", how_to_wash.LIGHT_HAND_WASH, 450, True, "cutePlates", "white", "salad", "ceramics", TablewareType.PLATE, 100)
        >>> second_item = abstract_tableware(125, "minimalist", how_to_wash.LIGHT_HAND_WASH, 450, True, "cutePlates", "black", "soup", "ceramics", TablewareType.SPOON, 150)
        >>> third_item = abstract_tableware(120, "minimalist", how_to_wash.WASHING_MACHINE, 45, True, "cutePlates", "white", "salad", "metal", TablewareType.FORK, 100)

        >>> print(str(tableware_manager([first_item, second_item, third_item]).find_tableware_by_type(TablewareType.PLATE))) #doctest: +ELLIPSIS
        [AbstractTableware(...tableware_type=TablewareType.PLATE...)]
        """
        return list(filter(lambda product: product.tableware_type == tableware_type, self.tableware_list))


if __name__ == '__main__':
    doctest.testmod(verbose=True)
