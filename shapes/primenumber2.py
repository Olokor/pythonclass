print("this is a prime number cheker! and it also checks for odd and even numbers")
number = int(input("enter a number"))

def odd_and_even_checker(number):
    if number % 2 == 0:
        print(f"{number} is even")

    elif number % 2 !=0:
        print(f"{number} is odd!")
    
if number <= 2:
    print(f"{number} is not prime")
    odd_and_even_checker(number)


elif (number % 2 == 0 or number % 3 == 0 or number % 5== 0) and number !=3 and number !=5:
    print(f"{number} is not a prime number")
    odd_and_even_checker(number)

else:
    print(f"{number} is prime")
    odd_and_even_checker(number)