numbers = [1, 3, 7, 11, 2, -6, 0]


def find_min_max_number(numbers):
    min_number = numbers[0]
    max_number = numbers[0]

    for number in numbers:
        if number < min_number:
            min_number = number
        elif number > max_number:
            max_number = number

    return min_number, max_number


min_number, max_number = find_min_max_number(numbers)

print(f"Najmniejsza liczba to: {min_number}.")
print(f"Największa liczba to: {max_number}.")