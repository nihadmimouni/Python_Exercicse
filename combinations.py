k = int (input("Introduire k svp : "))
n = int (input("Introduire n svp : "))
def fact(n):
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res
result = fact(n) / (fact(k) * fact(n - k))

print("Result using Iterative function is:", result)