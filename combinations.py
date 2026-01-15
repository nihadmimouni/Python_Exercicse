k = int (input("Introduire k svp : "))
n = int (input("Introduire n svp : "))
f1=1
for i in range(2,n+1):
    f1 = f1 * i
print(f1)
f2=1
for i in range(2,k+1):
    f2 = f2 * i
print(f2)
f3=1
for i in range(2,n-k+1):
    f3 = f3 * i
print(f3)

print("comb de ", k, ",", n," = ", f1//(f2 * f3))