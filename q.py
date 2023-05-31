from ecdsa import ellipticcurve

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

counter = 1
x1, y1 = x, y
x2, y2 = 0, 0

while counter < n:
    counter += 1
    if x1 == x:
        s = (3 * x ** 2 + a) * pow(2 * y, p - 2, p)
    else:
        s = (y1 - y) * pow(x1 - x, p - 2, p)

    x2 = (s ** 2 - x - x1) % p
    y2 = (s * (x1 - x2) - y1) % p

    x1, y1 = x2, y2
    print("%dP\t(%d,%d)" % (counter, x1, y1))
