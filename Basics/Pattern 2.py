#prime between 1 to n
a = int(input("please enter a number for pattern \n"))
for i in range (2 , a + 1):
    is_prime = True
    for j in range (2, i) :
        if i % j == 0 :
            is_prime = False
            break

    if is_prime == True :
        print(i, end=" ")

    