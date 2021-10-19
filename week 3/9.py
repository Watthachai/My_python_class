n = input('Enter Number : ')
result = 0

if n>='a' and n<='z':
    print('Input number only !')
    exit()
if n>='A' and n<='Z':
    print('Input number only !')
    exit()

for i in range(1,5):
    result = result+int(str(i*n))
print(f'Output : {result} (={n}+{n*2}+{n*3}+{n*4})')