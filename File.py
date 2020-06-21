with open(file= "new.txt", mode= "r+") as file_Obj:

 #brand_new = file_Obj.write(str(58))

 file_Obj.write(input(print("Nhao 1 chuoi vao file: ")))
 file_Obj.seek(0)
 brand_new1 = file_Obj.read()

#file_Obj.close()
print(brand_new1)

