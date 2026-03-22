import time

def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)

n = int(input("Enter number: "))

if n < 0:
    print("Invalid Input")
else:
    start = time.perf_counter()
    ans = fib_rec(n)
    end = time.perf_counter()
    
    print("Result:", ans)
    print("Time taken (ms):", (end - start) * 1000)
    print("Digits in result:", len(str(ans)))