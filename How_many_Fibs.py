


import _bisect
def fib(a, b):
    while b < 10**100:
        yield a
        a, b = b, a+b
Fib = list(fib(1, 2))

while True:
    l, h = map(int, input().split())
    if l == 0 and h == 0:
        break
    left = _bisect.bisect_left(Fib, l)
    right = _bisect.bisect_right(Fib, h)
    print(right - left)
    


