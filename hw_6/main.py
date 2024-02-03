from binary_search_list import BinarySearchList


def main():
    bin_list = BinarySearchList(2, 1, 9, 4, 5, 6, 3)
    indexes = [str(i) for i in range(len(bin_list))]

    print()
    print('\tv Индексы')
    print('', '  '.join(indexes), '')
    print(bin_list)
    print('\t^ Список\n')

    index = bin_list.verbose_binary_search(5, len(bin_list) - 1)
    print(index)

    index = bin_list.verbose_binary_search(7, len(bin_list) - 1)
    print(index)

    bin_list_float = BinarySearchList(1.2, 10.5, 4.3, 8.2, 9.5, 12.6, 4.7, 3.12, 10.0)
    indexes = [f'{str(i).ljust(len(str(bin_list_float[i])))}' for i in range(len(bin_list_float))]

    print()
    print('\tv Индексы')
    print('', '  '.join(indexes), '')
    print(bin_list_float)
    print('\t^ Список\n')

    index = bin_list_float.verbose_binary_search(8.2, len(bin_list_float) - 1)
    print(index)

    index = bin_list_float.verbose_binary_search(10, len(bin_list_float) - 1)
    print(index)

    index = bin_list_float.verbose_binary_search(12, len(bin_list_float) - 1)
    print(index)


if __name__ == "__main__":
    main()