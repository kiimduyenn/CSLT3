M1=int(input('M1=')) #Don gia thu nhat
M2=int(input('M2='))
M3=int(input('M3='))
S=int(input('S=')) #Dien nang tieu thu
if 1<=S<=100:
    print('Phai tra=',M1*S,sep='')
elif 101<=S<=150:
    print('Phai tra=',M1*100+(S-100)*M2,sep='')
elif S>= 151:
    print('Phai tra=',M1*100+M2*50+(S-150)*M3,sep='')