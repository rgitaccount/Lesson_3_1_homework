list1 = [1, 2, 3, 4]
list2 = [8, 12, 45, 67, 89, 45]
list3 = [78, 90, 65]


# Problem 1. The function returns new list
def list_adder(input_list: list):
    return input_list+input_list


# Problem 1. The function modifies existing list
def list_extender(input_list: list):
    input_list.extend(input_list)


# Extra problem
def find_sum_components(input_list: list, sum_value: int):
    list_of_pairs = []
    for i in range(len(input_list)-1):
        if input_list[i] + input_list[i+1] == sum_value:
            list_of_pairs.append([i, i+1])
    if list_of_pairs:
        for pair in list_of_pairs:
            print(pair)


if __name__ == "__main__":
    print(list_adder(list1))
    list_extender(list2)
    print(list2)

    numbers = [2, 7, 11, 15, 1, 8]
    find_sum_components(numbers, 9)
