from socket import *
import threading
from datetime import datetime

host = '192.168.1.214'
port = 9091
address = (host,port)
conn =[]
adrr = []
threads =[]
logins = []

def whosonline(connTemp):
        connTemp.send(str.encode("Online:\n"))
        if logins.__len__() == 0: 
                connTemp.send(str.encode("None\n"))
        else:
                for temp in logins:
                        connTemp.send(str.encode(temp+'\n'))
def getConnects():
    i = 0
    while True:
        connTemp,adrrTemp = tcp_socket.accept()
        conn.append(connTemp)
        adrr.append(adrrTemp)
        whosonline(connTemp)
        connTemp.send(str.encode("enter login:"))
        while True:
                login = bytes.decode(connTemp.recv(1024))
                if checkLogin(login) == True:
                        break
                connTemp.send(str.encode('INVALID LOGIN'))
        logins.append(login)
        print(adrrTemp,login,datetime.now())
        hasConnected = 'User ' + login + ' has connected'
        hasConnected = str.encode(hasConnected)
        sendMessagesToAll(connTemp,hasConnected)
        threads.append(threading.Thread(target=getMessages,args=[connTemp,adrrTemp,login]))
        threads[i].start()
        i+=1
        
def sendMessagesToAll(cur,tempmes):
        for temp in conn:
                if temp != cur:
                        temp.send(tempmes)
            
def getMessages(cur,adr,login):
        while True:
                data = cur.recv(1024)
                if not data:
                        hasDisconected = 'User ' + login + ' has disconnected'
                        sendMessagesToAll(cur,str.encode(hasDisconected))
                        conn.pop(conn.index(cur))
                        adrr.pop(adrr.index(adr))
                        logins.pop(logins.index(login))
                        break
                else:
                        data = bytes.decode(data)
                        message_ = '\n' + login+' :' + data 
                        message_ = str.encode(message_)
                        sendMessagesToAll(cur,message_)


if __name__ == '__main__':
        print("start")
        tcp_socket = socket(AF_INET, SOCK_STREAM)
        tcp_socket.bind(address)
        tcp_socket.listen()

        t1 = threading.Thread(target=getConnects)
        t1.start()
        t1.join()



    