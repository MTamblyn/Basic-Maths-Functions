from time import time
def factorial(n):
    """
    Returns the factorial of n (n!).
    """
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
    

def multiply(a,b):
    """
    Returns a*b using only addition.
    """
    if a == 1:
        return b
    elif b == 1:
        return a
    return a + multiply(a,b-1)


def powers(a,b):
    """
    Returns a**b using only multiplication.
    """
    if b == 0:
        return 1
    else:
        return a*powers(a,b-1)
    
def fib(n):
    """
    Returns nth term in fibonacci sequence or Fn.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
    
    
def main():
    
    print("3! = ", factorial(3))#Equivalent to 3!
    print("3*2 = ", multiply(3,2))
    print("6**1 = ", powers(6,1))#Equivalent to 6**1 (6^1).
    
    print("Fibonacci Sequence")
    for i in range(10):#This creates the fibonacci sequence up to 10.
        print(fib(i))

main()