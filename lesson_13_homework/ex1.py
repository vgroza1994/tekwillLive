def calculate_sum(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    return sum(lst)
my_list = [1, 2, 3, 4, 5]
print(calculate_sum(my_list))

not_a_list = "not a list"
print(calculate_sum(not_a_list))