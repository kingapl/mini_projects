text = input("Wpisz tekst: ")

def count_words(text):
    words = text.split()

    return len(words)

words = count_words(text)
print(f"Liczba słów w tekście: {words}.")