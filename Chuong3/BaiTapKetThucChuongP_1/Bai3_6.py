a=int(input()) #Canh thu nhat cua tam giac
b=int(input())
c=int(input())
if (a+b)>c and (a+c)>b and (b+c)>a and a>0 and b>0 and c>0:
    if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
        print('Tam giac vuong')
    elif a==b and b==c and a==c:
        print('Tam giac deu')
    else: print('Tam giac loai khac')
else: print('Khong hop le')