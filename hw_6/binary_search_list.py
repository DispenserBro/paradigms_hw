from typing import TypeVar
from unittest import result


T = TypeVar('T')


class BinarySearchList[T](list):
    def __init__(self, *args, **kwargs):
        super(BinarySearchList, self).__init__(args)
        self.sort()

    def binary_search(self, item: T, last: int, first: int = 0) -> int:
        if last >= first:
            middle = (first + last) // 2

            if self[middle] == item:
                return middle
            elif self[middle] > item:
                return self.binary_search(item, middle - 1, first)
            else:
                return self.binary_search(item, last, middle + 1)
        else:
            return -1

    def verbose_binary_search(self, item: T, last: int, first: int = 0) -> int:
        result = self.binary_search(item, last, first)
        
        if result == -1:
            print(f"Элемент {item} не найден в списке")
        else:
            print(f"Элемент {item} найден на индексе {result}")

        return result