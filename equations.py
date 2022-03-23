import math
a=int(input("the value of a="))
b=int(input("the balue of b="))
c=int(input("enter the value of c="))
w=4*a*c
x=b*b-w
y=math.sqrt(x)
z=2*a
o=(-b+y)/z
p=(-b-y)/z
#print("the value of x be ",  p ",",o)
print(f"thevalue of x be {o},{p}")

