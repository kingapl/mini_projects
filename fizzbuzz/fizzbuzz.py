def fizzbuzz(limit):
    for number in range(1, limit+1):
        if number % 15 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


fizzbuzz(int(input('Podaj liczbę: ')))
