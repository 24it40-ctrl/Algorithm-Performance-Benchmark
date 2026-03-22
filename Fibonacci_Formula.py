import time
import math

n = int(input("Enter number: "))

if n < 0:
    print("Invalid Input")
else:
    start = time.perf_counter()
    
    # Simple Binet's Formula
    phi = (1 + math.sqrt(5)) / 2
    ans = round((phi**n) / math.sqrt(5))
    
    end = time.perf_counter()
    
    print("Result:", ans)
    print("Time taken (ms):", (end - start) * 1000)
    print("Digits in result:", len(str(ans)))