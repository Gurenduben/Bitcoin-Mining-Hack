from ecdsa import ellipticcurve
from multiprocessing import Pool

a = 0
b = 7
p = 115792089237316195423570985008687907853269984665640564039457584007908834671663  # prime number

x = int(input("Enter the x-coordinate to search from: "))
y = int(input("Enter the y-coordinate to search from: "))
n = int(input("Enter the number of points to compute: "))

print("a =", a)
print("b =", b)
print("p =", p)
print("Starting point: (%d,%d)" % (x, y))

curve = ellipticcurve.CurveFp(p, a, b)

if (y ** 2 % p) == ((x ** 3 + a * x + b) % p):
    print("Starting point is on curve")
else:
    print("Starting point is not on curve")
    exit()

def compute_point(counter):
    global x, y, curve, p
    if x == x:
        s = (3 * x ** 2 + a) * pow(2 * y, p - 2, p)
    else:
        s = (y - y) * pow(x - x, p - 2, p)

    x2 = (s ** 2 - x - x) % p
    y2 = (s * (x - x2) - y) % p

    return x2, y2

if __name__ == "__main__":
    pool = Pool()  # Use all available CPU cores
    results = pool.map(compute_point, range(1, n+1))

    for counter, (x1, y1) in enumerate(results, start=1):
        print("%dP\t(%d,%d)" % (counter, x1, y1))
