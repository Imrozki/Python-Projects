def prime(number):
    is_prime = True
    for i in range(2 , number):

        if number % i == 0:
            is_prime = False
    if is_prime == True:
        print("Its a Prime number")
    else:
        print("Not a prime number")


n = int(input("Enter a number"))

prime(number=n)

