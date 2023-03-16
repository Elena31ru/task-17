def selection_sort(alist):
    for i in range(0, len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]
    return alist


def binary_search(data, elem):
    low = 0
    data_len = len(data)
    high = data_len - 1

    while low <= high:
        middle = (low + high) // 2

        if (middle < data_len - 1) and data[middle] < elem <= data[middle + 1]:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1

    return -1


def main():
    arr = list(map(int, input().split()))

    digit = input()
    if digit.isdigit():
        digit = int(digit)
    else:
        print('Необходимо ввести число!')
        return

    arr = selection_sort(arr)
    print('Отсортированный массив:', arr)
    index = binary_search(arr, digit)

    if index == -1:
        print(f'Число {digit} не соответствует заданному условию')
    else:
        print(index)


if __name__ == '__main__':
    main()

