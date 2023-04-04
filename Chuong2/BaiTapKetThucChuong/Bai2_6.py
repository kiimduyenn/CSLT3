HoTen=input('Ho ten: ')
SoNgayCong=int(input('So ngay cong: '))
DonGia=int(input('Don gia ngay cong: '))
PhuCap=float(input('He so phu cap: '))
TamUng=int(input('Tam ung: '))
Luong=DonGia*SoNgayCong*PhuCap
print('Nhan vien ',HoTen,', Co tien Luong=',round(Luong,1),', Tam ung=',TamUng,' va Thuc linh=',round(Luong-TamUng,1),sep='')