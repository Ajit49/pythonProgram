#num = int(input("Enter a number: "))
#fact = 1
#if num < 0:
#    print("factorial of below zero does not exit")
#if num == 0:
   # print("factorial of zero is",1)
#if num > 0:
 #   for i in range (1,num+1):
#        fact = fact * i
  #  print("factorial of given number is",fact)

# Using recursion method
def fact(a):
    if a == 0:
        return 1
    else:
        return ((a)*fact(a-1))
num = int(input("Enter a number: "))
result = fact(num)
print("factorial of given number is",result)