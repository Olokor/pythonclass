print("this is a prime number checker")

number = int(input("enter a number"))

for num in range(2, 11):
    
    if number <= 2:
        print(f"{number} is not a prime number")
        
    
    elif number % num == 0 and number != num:
        print(f"{number} is  not a prime number {num} can divide {number}")
        
    
    else:
        print(f"{number} is a prime number")
        
        