def count_words(text):
    return len(text.split())


text = input("Wpisz tekst: ")

words = count_words(text)
print(f"Liczba słów w tekście: {words}.")
