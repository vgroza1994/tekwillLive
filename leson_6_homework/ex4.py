def calculate_sum(numbers):
    number_list = [int(num) for num in numbers.split(",")]
    even_sum = sum(filter(lambda x: x % 2 == 0, number_list))
    odd_sum = sum(filter(lambda x: x % 2 != 0, number_list))
    print("Suma numerelor pare:", even_sum)
    print("Suma numerelor impare:", odd_sum)

numbers_input = input("Introduceți numerele separate prin virgulă: ")
calculate_sum(numbers_input)