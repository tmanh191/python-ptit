import socket
import hashlib
def Server_Program():
    host= socket.gethostname()
    port=191
    Server_Socket=socket.socket()
    Server_Socket.bind((host,port))
    Server_Socket.listen(1)
    conn,address=Server_Socket.accept()
    key='TranTrongManh-B21DCAT127'

    data=conn.recv(1024).decode()
    data_1=conn.recv(1024).decode()
    print("Nhận từ client: "+ str(data))
    print("Nhận mã hóa SHA-512 từ client: "+ str(data_1))
    hashed=hashlib.sha512(data.encode("utf-16") + key.encode("utf-16")).hexdigest()
    data= "Mã hóa thành công! \n Hello, I am B21DCAT127 server"
    print("Server gửi tới client: ", data)
    print("Server mã hóa SHA-512 thông điệp: ",hashed)
    if data_1!=hashed:
        data="The received message has lost its integrity"
        conn.send(data.encode())
    else:
        conn.send(data.encode())
    conn.close()

if __name__=='__main__':
    print("Server sẵn sàng!")
    Server_Program()


