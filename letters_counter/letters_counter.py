text = input("Wpisz tekst: ")
letter = input("Którą literę policzyć? ")

def letters_counter(letter):
    counter = 0

    for t in text.lower():
        if t == letter.lower():
            counter += 1

    return counter


counter = letters_counter(letter)

print(f"\nLitera '{letter}' wystąpiła {counter} razy w tekście.")