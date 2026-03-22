import time
inp = input("Enter number: ")
if inp.isdigit():
    start = time.perf_counter()
    s = sum(int(d) for d in inp)
    res = 0 if s == 0 else 1 + (s - 1) % 9
    print(f"Result: {res} | Time: {(time.perf_counter()-start)*1000:.6f} ms")