# Functions in Python
def simpleInterest(p, r, t):
    si = (p*r*t)/100
    print(f"Simple Interest is: Rs.", si)


prinicipal = int(input("Enter Prinicipal Amount : "))
rate = int(input("Enter rate of Interest : "))
time = int(input("Enter time in years : "))
simpleInterest(prinicipal, rate, time)
