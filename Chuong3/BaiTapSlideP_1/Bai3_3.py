TieuThu=int(input('Tieu thu='))
if 1<= TieuThu<= 100:
    print('Phai tra=',TieuThu*550+0.1*TieuThu*550,sep='')
elif 101<=TieuThu<=150:
    print('Phai tra=',100*550+0.1*100*550+(TieuThu-100)*750+0.1*(TieuThu-100)*750,sep='')
elif 151<=TieuThu<=200:
    print('Phai tra=',100*550+0.1*100*550+50*750+0.1*50*750+(TieuThu-150)*950+0.1*(TieuThu-150)*950,sep='')
elif 201<=TieuThu:
    print('Phai tra=',100*550+0.1*100*550+50*750+0.1*50*750+50*950+0.1*50*950+(TieuThu-200)*1350+0.1*(TieuThu-200)*1350,sep='')