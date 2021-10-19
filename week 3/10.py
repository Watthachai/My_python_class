num = input('Enter number covert : ')

latin = {
           'I':1,
           'V':5,
           'X':10,
           'L':50,
           'C':100,
           'D':500,
           'M':1000
        }

covert = 0
for i in range(len(num)):
        if i+1 != len(num) and latin[num[i]]<latin[num[i+1]]:
                covert = covert - latin[num[i]]
        else:
                covert = covert+ latin[num[i]]
print(covert)