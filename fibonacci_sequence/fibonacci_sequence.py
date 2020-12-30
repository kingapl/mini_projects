try:
    number = int(input("Ile liczb ciągu Fibonacciego wyświetlić? "))

    fib_0 = 0
    fib_1 = 1

    if number == 1:
        print(fib_0)
    elif number >= 2:
        print(fib_0)
        print(fib_1)
        for i in range(2, number):
            fib_n = fib_1 + fib_0
            print(fib_n)
            fib_0 = fib_1
            fib_1 = fib_n
    else:
        print("Niepoprawna liczba")

except ValueError:
    print("Nie wpisano liczby.")