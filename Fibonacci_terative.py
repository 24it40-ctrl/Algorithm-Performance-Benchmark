import time

n = int(input("Enter number: "))

if n < 0:
    print("Invalid Input")
else:
    start = time.perf_counter()
    
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    
    end = time.perf_counter()
    
    print("Result:", a)
    print("Time taken (ms):", (end - start) * 1000)
    print("Digits in result:", len(str(a)))