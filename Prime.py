#number = int(input("Enter any number: "))
number=6
if number > 1:
    for i in range(2,number):
        if number%i==0:
            print("not a prime")
            break
    else:
        print("prime")
else:
    print(number,":not a prime number")

