a=int(input('a=')) #Canh tam giac
b=int(input('b='))
c=int(input('c='))
p=(a+b+c)/2 #Nua chu vi
import math
if (a+b)>c and (a+c)>b and (b+c)>a:
    print('Dien tich=',round(math.sqrt((p*(p-a)*(p-b)*(p-c))),3))
else: print('Khong hop le')