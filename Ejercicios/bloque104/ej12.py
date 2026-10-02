n = int(input("Dame un número: "))

for i in range(2, n + 1):
    primo = True

    for j in range(2, i):
        if i % j == 0:
            primo = False
            break

    if primo:
        print(i)