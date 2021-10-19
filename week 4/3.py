def gcd(n1, n2):
    if n2 == 0:
        return n1
    return gcd(n2, n1 % n2)

lcm = 1
for i in range(1,20):
    lcm = lcm * i // gcd(lcm, i)
    
print(lcm)