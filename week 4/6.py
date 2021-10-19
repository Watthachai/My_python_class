sosq = 0
sqos = 0

for i in range(1,101):
    sosq += (i*i)

for n in range(1,101):
    sqos = sqos+n

num2 = (sqos)**2

total = num2-sosq
result = abs(total)

print(f'square of the sum is {num2}  sum of the squares {sosq} differnt is {num2} - {sosq} = {result}')