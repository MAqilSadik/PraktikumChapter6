def jumlah (a,b):
    hasil = a + b
    return hasil

def kali (a,b):
    hasil = a * b
    return hasil

def kurang (a,b):
    hasil = a - b
    return hasil

def bagi (a,b):
    hasil = a / b
    return hasil


from operation import *

a = 10
b = 7
print(a,'+',b,'=', jumlah(a,b))
print(a,'-',b,'=', kurang(a,b))
print(a,'*',b,'=', kali(a,b))
print(a,'/',b,'=', bagi(a,b))

