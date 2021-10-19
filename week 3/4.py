s = str(input('Enter String : '))
c_lower = 0
c_upper = 0


for i in s:
    if i>='a' and i<='z':
        c_lower += 1
    elif i>='A' and i<='Z':
        c_upper += 1
if c_lower == 0:
    print('All is uppper letter!')     
elif c_upper ==0:
    print('All is lower letter!')
print(f'Lower Case {c_lower} and Upper case {c_upper}')