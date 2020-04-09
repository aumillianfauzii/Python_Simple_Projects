###2 Digits Calc###

num1= float(input('Input value : '))
num2=float(input('Input value : '))

def tambah(x,y):
    return x+y

def kali(x,y):
    return x*y

def bagi (x,y):
    return x/y

def kurang (x,y):
    return x-y

print("Pilih Operasi")
print('1.Tambah')
print('2.Kali')
print('3.Bagi')
print('4.Kurang')

choice = input('Masukkan pilihan: ')

if choice == '1':
   print('Hasil dari', num1,"+",num2,"=", tambah(num1,num2))
elif choice == '2':
   print('Hasil dari', num1,"*",num2,"=",  kali(num1,num2))
elif choice == '3':
    print('Hasil dari', num1, "/",num2, "=", bagi(num1,num2))
elif choice == "4":
    print('Hasi; dari', num1, "-", num2, "=", Kurang(num1,num2))
