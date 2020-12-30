string = input("Wpisz tekst: ")

def reverse(string):
    reverse_string = ""

    for s in string:
        reverse_string = s + reverse_string

    return reverse_string

reverse_string = reverse(string)

print(f"Odwrócony ciąg: {reverse_string}.")