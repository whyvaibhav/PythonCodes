from Signature_folder.Signature import sign

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))

sign()
