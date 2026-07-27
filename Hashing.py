n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 1]
m = [10, 111, 1, 9, 5, 67, 2]

for num in m:
    count = 0

    for x in n:
        if x == num:
            count += 1

    print(f"{num} -> {count}")