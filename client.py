from socket import *
import sys
import threading

host = '78.140.8.143'
port = 9091
addr = (host,port)
end = False
login = ''
def getMessages():
    while True:
        recv_data = tcp_socket.recv(1024)
        if recv_data:
            print(bytes.decode(recv_data))
        else:
            print("CLOSE CONNECTION")
            end = True
            tcp_socket.close()
            break
def sendMessages():
    login = input()
    tcp_socket.send(str.encode(login))
    login+=' :'
    while True:
        getdata = input()
        if getdata == 'exit':
            tcp_socket.close()
            end = True
            sys.exit()
        else:
            tcp_socket.send(getdata.encode("UTF-8"))

if __name__ == "__main__":
    
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.connect(addr)

    t1 = threading.Thread(target=getMessages,daemon=False)
    t2 = threading.Thread(target=sendMessages,daemon=False)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('all?')
