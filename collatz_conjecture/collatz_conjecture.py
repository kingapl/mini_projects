number = int(input("Podaj dodatnią liczbę naturalną: "))

def collatz(number):
    print(number)
    
    while number > 1:
        if number%2 == 0:
            number = number//2
        else:
            number = number*3 + 1
        print(number)

collatz(number)