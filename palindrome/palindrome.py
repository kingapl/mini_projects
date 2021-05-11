def check_if_palindrome(text: str):
    if text.lower() == text[::-1].lower():
        return f'{text} to palindrom.'
    return f'{text} nie jest palindromem.'


print("Sprawdź, czy słowo to palindrom.")
print(check_if_palindrome(input("Wpisz słowo: ")))
