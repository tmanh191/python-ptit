import socket
import hashlib


def Client_Program():
    host=socket.gethostname()
    port=191
    Client_Socket=socket.socket()
    Client_Socket.connect((host,port))
    key='TranTrongManh-B21DCAT127-error'
    message="Hello, I am B21DCAT127 client"
    hashed=hashlib.sha512(message.encode("utf-16")+key.encode("utf-16")).hexdigest()
    print("Client gửi đến server: ",message)
    Client_Socket.send(message.encode())
    print("Client gửi SHA-152 thông điệp tới server: ",hashed)
    Client_Socket.send(hashed.encode())
    data=Client_Socket.recv(1024).decode()
    print("Nhận từ server: ",data)
    Client_Socket.close()

if __name__=='__main__':
    Client_Program()


