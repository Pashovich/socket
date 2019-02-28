from socket import *
import rsa
import threading
#данные сервера
host = 'localhost'
port = 9090
address = (host,port)
conn =[]
adrr = []
pubkey, privkey = rsa.newkeys(512)

def getMessages():
        tempdata = tcp_socket.recv(1024)

def getConnects():
    i = 0
    while True:
        connTemp,adrrTemp = tcp_socket.accept()
        conn.append(connTemp)
        adrr.append(adrrTemp)
        print(adrr[i])
        i+=1
        
def sendMessagesToAll():
    while True:
        data = input("waht to send")
        data = str.encode(data)
        for temp in conn:
            temp.send(data)

tcp_socket = socket(AF_INET, SOCK_STREAM)
#bind - связывает адрес и порт с сокетом
#tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_socket.bind(address)
#listen - запускает прием TCP
tcp_socket.listen()

t1 = threading.Thread(target=getConnects)
t2 = threading.Thread(target=sendMessagesToAll)
t1.start()
t2.start()


    