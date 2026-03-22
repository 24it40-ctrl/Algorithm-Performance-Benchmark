import time
def get_ds_rec(n):
    if len(str(n)) == 1: return int(n)
    s = sum(int(d) for d in str(n))
    return get_ds_rec(s)

inp = input("Enter number: ")
if inp.isdigit():
    start = time.perf_counter()
    res = get_ds_rec(inp)
    print(f"Result: {res} | Time: {(time.perf_counter()-start)*1000:.6f} ms")
else: print("Invalid Input!")