k = int (input("Introduire k svp : "))
n = int (input("Introduire n svp : "))
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
        
result = fact(n) / (fact(k) * fact(n - k))

print("Result using Recursive function is:", result)