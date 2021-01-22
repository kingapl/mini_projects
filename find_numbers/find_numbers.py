def enter_numbers():
    enter_number = True
    numbers = []

    print("Wpisz liczbę i wciśnij Enter. Aby zakończyć pozostaw puste pole.")
    while enter_number:
        number = input("Twoja liczba: ")
        try:
            if number != '':
                numbers.append(int(number))
            else:
                enter_number = False
        except ValueError:
            print("Nie wpisano liczby.")

    return numbers


def find_min_max_number(numbers):
    min_number = numbers[0]
    max_number = numbers[0]

    for number in numbers:
        if number < min_number:
            min_number = number
        elif number > max_number:
            max_number = number

    return min_number, max_number


numbers = enter_numbers()
min_number, max_number = find_min_max_number(numbers)

print(f"\nTwoje liczby: {numbers}.")
print(f"Najmniejsza liczba to: {min_number}.")
print(f"Największa liczba to: {max_number}.")