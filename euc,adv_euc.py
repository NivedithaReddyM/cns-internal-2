a=int(input("Enter a:"))
b=int(input("Enter b:"))

def gcd(a,b):
    r=a%b
    if r==0:
        return b
    return gcd(b,r)
print(gcd(a,b))

def e_gcd(a,b):
 
    if b==0:
        return a,1,0
    else:
        
        gcd,x,y=e_gcd(b,a%b)
        return gcd,y,x-(a//b)*y
print(e_gcd(a,b))
