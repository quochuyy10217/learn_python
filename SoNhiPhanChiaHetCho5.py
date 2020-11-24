def decimalconverter(sonhiphan):
    newarr = list(sonhiphan)
    sophantu = len(newarr)
    tong = 0
    for x in newarr:
        tong += int(x)*(2**(sophantu-1))
        sophantu-=1
    return tong

print("Nhap mot chuoi cac so nhi phan ma ban muon kiem tra xem no co chia het cho 5 khong")
print("Nhap x de ket thuc viec nhap so: ")
dulieunhapvao = []
while True:
    data = input("Nhap so nhi phan: ")
    if data=='x':
        break
    dulieunhapvao.append(data)
ketqua = []
print(dulieunhapvao)
for i in range(0,len(dulieunhapvao)-1):
    if decimalconverter(dulieunhapvao[i])%5==0:
        ketqua.append(dulieunhapvao[i])
print("Cac so nhi phan chia het cho 5 la: ", ketqua)