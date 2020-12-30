print("Sprawdź, czy słowo to palindrom.")
string = input("Wpisz słowo: ")

def reverse_string(string):
    reverse = ""

    for s in string:
        reverse = s + reverse

    return reverse


def check_if_palindrome(string, reverse):
    if string.lower() == reverse.lower():
        return True
    else:
        return False

reverse = reverse_string(string)
is_palindrome = check_if_palindrome(string, reverse)

(print(f"{string.capitalize()} to palindrom.") if is_palindrome == True 
    else print(f"{string.capitalize()} to nie palindrom."))