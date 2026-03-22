import time
def get_ds_iter(n):
    while len(n) > 1:
        n = str(sum(int(d) for d in n))
    return n

inp = input("Enter number: ")
if inp.isdigit():
    start = time.perf_counter()
    res = get_ds_iter(inp)
    print(f"Result: {res} | Time: {(time.perf_counter()-start)*1000:.6f} ms")