min = int(input("Enter a min number: "))
max = int(input("Enter a max number: "))

for num in range (min, max +1):
    if num > 1:
        for i in range (2,num):
            if num % i == 0:
                break

        else:
            print(num)