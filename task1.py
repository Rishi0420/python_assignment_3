# Task 1: Calculate Factorial Using a Function
num = int(input("Enter a number: "))
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n - 1)
ans = fact(num)
print("factorial of",num,"is",ans)
