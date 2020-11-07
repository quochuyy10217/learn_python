import random
import os
os.system("clear")
print("Day la tro choi doan so ma chuong trinh dua ra, so nam trong khoang tu 0 den 20!")
print("Ban se co nhieu nhat la 5 lan thu doan, chuc ban may man!")
print("Nhan phim ENTER de bat dau: ")
a = input()
print('----------------------------------------------------------------------')
while True:
    os.system("clear")
    secretNumber = random.randint(0,20)
    for i in range(1,6):
        luaChon = int(input("Nhap mot so ma ban nghi la trung voi ket qua: "))
        if luaChon==secretNumber:
            print("Ban da nghi dung roi!")
            break
        else:
            print("Tiec qua, ban da nghi sai roi!")
            if (i<3):
                print("Ban con " + str(5-i) + " lan thu!")
    print("So bi mat: " + str(secretNumber))
    print("Ban co muon thu lai khong?")
    print("1.Co     2.Khong")
    again = int(input("Lua chon cua ban: "))
    if again==2:
        break
    if again!=1 & again!=2:
        print("Lua chon khong hop le, tu dong thoat chuong trinh")
        break
print("Ket thuc chuong trinh!")

