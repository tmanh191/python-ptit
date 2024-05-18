from math import gcd
import sympy
import random
import math

# Hàm tính
def bipow(a, b, m):
    if b==0:
        return 1
    x= bipow(a,b//2,m)%m
    if b%2==0:
        return (x*x)%m
    else:
        return (x*x*a)%m

print("a^b mod m: " ,bipow(23322237329231,239847243,4))

def multiplicative_inverse(e,phi):
    d=0
    x1=0
    x2=1
    y1=1
    temp_phi=phi

    while e>0:
        temp1= temp_phi//e
        temp2= temp_phi - temp1*e
        temp_phi=e
        e=temp2

        x=x2 - temp1 * x1
        y= d -temp1 * y1

        x2=x1
        x1=x
        d=y1
        y1=y

    if temp_phi==1:
        return d+phi
    
print(f"số d: {multiplicative_inverse(3233,3120)}")
mod= 3233*multiplicative_inverse(3233,3120)%3120
print(f"số dư cho d.e mod phi: {mod}")


def generate_keypair(p,q):
    n=p*q

    phi=(p-1)*(q-1)

    # Chọn 1 số nguyên sao cho 1< e < phi
    e=65537

    #Sử dụng thuật toán Euclid mở rộng để tìm d
    d= multiplicative_inverse(e,phi)
    return ((e,n),(d,n))

def encrypt(public_key, plaintext):
    e,n= public_key
    #Hàm ord: nhận 1 kí tự làm đầu vào và trả về mã ASII của nó
    cipher= [bipow(ord(char),e,n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    d,n=private_key
    #hàm chr: Nhận 1 số nguyên làm đầu vào và trả về ký tự tương ứng với mã ASII
    plain= [chr(bipow(char,d,n)) for char in ciphertext]
    return ''.join(plain)

#Thử nghiệm mã hóa và giải mã
# p=101
# q=53
p=sympy.randprime(2**1023,2**1024)
q=sympy.randprime(2**1023,2**1024)

public_key,private_key =generate_keypair(p,q)
print("KHÓA CÔNG KHAI: ",public_key)
print("KHÓA BÍ MẬT: ",private_key)

message= "I am Tran Trong Manh"
print("plaintext: ",message)

encrypt_msg= encrypt(public_key,message)
out_encrypted= ''.join(str(x) for x in encrypt_msg)

print("Encrypted: ",out_encrypted)

decrypted_msg= decrypt(private_key, encrypt_msg)
print("Decrypted: ",decrypted_msg)




