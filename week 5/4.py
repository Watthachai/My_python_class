mylist = [  '*****',
            '*MM**',
            '*KIK*',
            '*IT**',
            '**L**',
            ]

kmitl = 0
k_list = []
m_list = []
i_list = []
t_list = []
l_list = []
result = []

for y in range(len(mylist)):
    if 'K' in mylist[y]:
        for x in range(len(mylist)):
            if mylist[y][x] == 'K':
                k_list.append(f'{y}{x}')


for k in range(len(k_list)):
    ky = int(k_list[k][0])
    kx = int(k_list[k][1])
    for y in range(1,-2,-1):
        for x in range(-1,2):
            if(mylist[y+ky][x+kx] == "M"):
                m_list.append(str(ky+y)+str(kx+x))
                result.append(f'{ky+1} {kx+1}')

for m in range(len(m_list)):
        my = int(m_list[m][0])
        mx = int(m_list[m][1])
        for y in range(1,-2,-1):
            for x in range(-1,2):
                if(mylist[y+my][x+mx] == "I"):
                    i_list.append(str(my+y)+str(mx+x))
                    result.append(f'{my+1} {mx+1}')

for i in range(len(i_list)):
        iy = int(i_list[i][0])
        ix = int(i_list[i][1])
        for y in range(1,-2,-1):
            for x in range(-1,2):
                if(mylist[y+iy][x+ix] == "T"):
                    t_list.append(str(iy+y)+str(ix+x))
                    result.append(f'{iy+1} {ix+1}')
                    

for t in range(len(t_list)):
        ty = int(t_list[t][0])
        tx = int(t_list[t][1])
        for y in range(1,-2,-1):
            for x in range(-1,2):
                if(mylist[y+ty][x+tx] == "L"):
                    l_list.append(str(ty+y)+str(tx+x))
                    result.append(f'{ty+1} {tx+1}')
                    kmitl += 1

for l in range(len(l_list)):
    ly = int(l_list[l][0])
    lx = int(l_list[l][1])
    result.append(f'{ly+1} {lx+1}')


for j in range(0,kmitl):
   print(f'K : {result[j]} M: {result[j+3]} I: {result[j+6]} T: {result[j+9]} L: {result[j+12]}')

print(f"KMITL COUNT : {kmitl}")


