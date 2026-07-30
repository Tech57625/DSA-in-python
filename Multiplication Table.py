# program to print table of a number

# First Method Iterative approach

# def printTable(n):
#     for i in range(1, 11):

#         # multiples from 1 to 10

#         print("%d * %d = %d" % (n, i, n * i))


# if __name__ == "__main__":
#     n = 5
#     printTable(n)


# Second Method is Recursive approach

def printTable(n, i=1):
    if(i == 11): # base case
        return
    print(n, "*", i, "=", n * i)
    i += 1
    printTable(n, i)


if __name__ == "__main__":
    n = 5
    printTable(n)



