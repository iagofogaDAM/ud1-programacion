n = int(input("Dame un numero! : " ))

for i in range(1,n+1):
    for j in range(1,i+1):
        print (j, end="")
    print ("")



for i in range(1,n+1):
    s = ""
    for j in range(1,i+1):
        s = s + str(j)
    print (s)


for i in range(n):
    s = ""
    for j in range(i+1):
        s = s + str(j+1)
    print (s)

