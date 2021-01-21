text = input("Wpisz tekst: ")


def letters_in_text(text):
    number_of_letters = 0

    for letter in text.lower():
        if letter != ' ':
            number_of_letters += 1

    return number_of_letters


def letter_frequency(text):
    letters = {}

    for letter in text.lower():
        if letter == ' ':
            continue
        elif letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1

    return letters


number_of_letters = letters_in_text(text)
letters = letter_frequency(text)

print(f"\nTekst zawiera {number_of_letters} liter.\n")
print("Częstotliwość występowania liter:")

for key, value in letters.items():
    print(f"{key.upper()} - {value}")