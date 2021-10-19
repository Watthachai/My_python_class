n1,n2 = [int(e) for e in input("Input : ").split()]

if n1 <= 0 or n2 <= 0:
    print('ERROR!')
    exit()
if n1 < 10000 or n2 < 10000:
    for i in range(1,n2+1):
      
          if n1 % i == 0 and n2 % i == 0:   
            result = i
print(result)