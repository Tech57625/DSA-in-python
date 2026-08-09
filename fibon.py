n = int(input("Enter number: "))

a = 0
b = 1

print(a, end=" ")
print(b, end=" ")

for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c
    # Yahan last ki 2 lines tum likho