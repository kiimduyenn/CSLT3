a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
max=a
min=a
if a<b:
    max=b
if b<c:
    max=c
if a>b:
    min=b
if b>c:
    min=c
print('SLN=',max,sep="")
print('SBN=',min,sep="")