#1.check factorial number...
def factorial(num):
    if num==1:
        return 1
    else:
        return num * factorial(num-1)
num = int(input('Enter the number:'))
print(factorial(num))

#2. check fibonacci series
def fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
n = int(input('Enter the number:'))
for i in range(n):
    print(fibonacci(i),end=' ')
fibonacci(n)

