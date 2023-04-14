x=float(input('x=')) #So thuc thu nhat
y=float(input('y='))
Kytu=input('Phep toan:')
if Kytu=='+':
    print(str(x),'+',str(y),'=',x+y,sep='')
elif Kytu=='-':
    print(str(x),'-',str(y),'=',x-y,sep='')
elif Kytu=='*':
    print(str(x),'*',str(y),'=',x*y,sep='')
elif Kytu=='/':
    print(str(x),'/',str(y),'=',x/y,sep='')
elif Kytu!='+' or '-' or '/' or '*':
    print('Khong hop le')
elif Kytu=='/' and y==0:
    print('Khong hop le')