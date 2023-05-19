import sys
import libnum

a=0
b=7
p=115792089237316195423570985008687907853269984665640564039457584007908834671663 # prime number
n=57896044618658097711785492504343953926418782139537452191302581570759080747168 # number of points to show
x=55066263022277343669578718895168534326250603453777594175500187360389116729240 # starting point

if (len(sys.argv)>1):
    x=int(sys.argv[1])

if (len(sys.argv)>2):
    p=int(sys.argv[2])
if (len(sys.argv)>3):
    a=int(sys.argv[3])
if (len(sys.argv)>4):
    b=int(sys.argv[4])
if (len(sys.argv)>5):
    n=int(sys.argv[5])


print("a=",a)
print("b=",b)
print("p=",p)
print("n=",n)
print("x-point=",x)


z=(x**3 + a*x +b) % p
if (libnum.has_sqrtmod(z,{p:1} )):
  y=next(libnum.sqrtmod(z,{p:1}))

print("P\t(%d,%d)" % (x,y), end=' ')

if ((y**2 % p) == ((x**3+a*x+b) %p)): print("  \tPoint is on curve")
else:
    print("  \tPoint is not on curve")
    sys.exit()

s=((3*x**2)+a) * libnum.invmod(2*y,p) 

x1=(s**2-2*x) % p

y1=((s*(x-x1))-y) % p

x3=x1
y3=y1
x2=0
y2=0
counter=1

for i in range(2, n+1):
    counter=counter+1
    if (counter>n): sys.exit()

    print("%dP\t(%d,%d)" % (counter,x1,y1), end=' ')
    if ((y1**2 % p) == ((x1**3+a*x1+b) %p)): print("  \tPoint is on curve")

    rtn=libnum.invmod(x1-x,p) 
    if (rtn==0): 
        print("%dP=0" % (counter+1))
        counter=counter+2
        s=((3*x**2)+a) *  libnum.invmod(2*y,p) 

        x1=(s**2-2*x) % p

        y1=((s*(x-x1))-y) % p
        print("%dP\t(%d,%d)" % (counter,x,y), end=' ')
        if ((y**2 % p) == ((x**3+a*x+b) %p)): print("  \tPoint is on curve")


    else:   
        s=(y1-y)* rtn

        x2=(s**2-x1-x) % p

        y2=((s*(x1-x2)-y1)) % p

        x1=x2
        y1=y2
       
