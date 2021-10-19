result_list = []

for i in range(100,1000):
  for n in range(100,1000):
    s = i*n
    n = str(s)
    numtxt =[]
    for num in n :
      numtxt.append(num)
    numtxt.reverse()
    num_char =int(''.join(numtxt))
    if s==num_char:
      result_list.append(s)

max = 0
for i in result_list:
  if i>max:
    max=i
print(f"ANs: {max}")