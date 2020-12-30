import random

secret_number = random.randint(1, 100)

print("Myślę o pewnej liczbie z zakresu 1-100.")
number = 0

while number != secret_number:
    number = int(input("Zgadnij jaka to liczba.\n"))

    if number == secret_number:
        print("Tak! To właśnie ta liczba. Gratulacje!")
    elif number < secret_number:
        print(f"Liczba, o której myślę jest większa niż {number}.\n")
    elif number > secret_number:
        print(f"Liczba, o której myślę jest mniejsza niż {number}.\n")