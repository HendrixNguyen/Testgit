#tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, 
# nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200)
# .tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200).

a = []
for i in range(2000,3200):
    if(i % 7== 0) and (i % 5 != 0 ):
        a.append(str(i))
print(",".join(a))



'''Bài 2: tính giai thừa của một số cho trước. Kết quả được in thành chuỗi trên một dòng,
 phân tách bởi dấu phẩy.Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320..'''
 
b = int(input('Nhap so can tinh giai thua: '))
def Factorial(b):
    if(b == 0):
     return 1
    return b*Factorial(b-1)
print(Factorial(b))

'''Bài 3: Với số nguyên n nhất định, hãy viết chương trình để tạo ra một dictionary chứa (i, i*i)
như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này'''

c = int(input("Nhap N:"))
Dic = dict()
for i in range(1,c-1):
    Dic[i]= i*i
print(Dic)

''' Bài 4: Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển, 
tạo ra một danh sách và một tuple chứa mọi số..'''

d = input('Nhập chuỗi cần nhập: ')
sli= d.split(",")
T = tuple(sli)
print(T)

'''Bài 05: Định nghĩa một class có ít nhất 2 method: getString: 
để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.printString: 
in chuỗi vừa nhập sang chữ hoa.Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.'''

class Bai5(object):
    def __init__(self):
        self.s = ''
    def getString(self):
        self.s =input("Please input the name: ")
    def printString(self):
        print(self.s.upper())
        pass
strObj = Bai5()
strObj.getString()
strObj.printString()

'''Bài 06: Viết một method tính giá trị bình phương của một số.'''

x = int(input('Nhap so can binh phuong: '))
def Square(x):
    """Nhap so can binh phuong
"""
    return x**2 #**2 mean the square i  python = pow()
print("So da binh la: ",Square(x))

"""Bài 07: viết một chương trình để in tài liệu về một số hàm Python được tích hợp sẵn như abs(),int(),
input() và thêm tài liệu cho hàm bạn tự định nghĩa."""

print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)
print(Square.__doc__)

'''Bài 08: Định nghĩa một lớp gồm có tham số lớp và có cùng tham số instance'''

class Person:
    name = "Person"
    def __init__(self,name = None):
        self.name = name
jeffrey = Person("Jeffrey")
print ("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print ("%s name is %s" % (Person.name, nico.name))