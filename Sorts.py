counter = 0

def QuickSorts(input_list):
    global counter
    counter =+ 1
    if len(input_list) <= 1:
        return input_list

    p = input_list.pop(len(input_list) / 2)
    # p = input_list.pop(0)
    less = [i for i in input_list if i < p]
    greater = [i for i in input_list if i >= p]

    return QuickSorts(less) + [p] + QuickSorts(greater)


def main():
    sorted_list = [1, 2, 3, 3, 4, 5]
    random_list = [2, 1, 4, 3, 5, 3]

    global counter

    print "QuickSort"
    print QuickSorts(sorted_list)
    print counter
    counter = 0

if __name__ == '__main__':
    main()