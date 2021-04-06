print("Sprawdź, czy słowo to palindrom.")
text = input("Wpisz słowo: ")

(print(f"{text.capitalize()} to palindrom.") if text.lower() == text[::-1].lower() 
    else print(f"{text.capitalize()} to nie palindrom."))
