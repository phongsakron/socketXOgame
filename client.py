import socket
import threading
import pickle

HOST = 'localhost'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = ''

def pr_msg():
    while 1:
        data = s.recv(1024)
        mydata = pickle.loads(data)
        if mydata:
            if type(mydata) == str:
                print("\n"+ mydata)
            else:
                for myda in mydata:
                    print(myda)
        
        

x = threading.Thread(target=pr_msg)
x.start()

while 1:
    send_data = input("Client : ")
    if send_data in ['quit', 'Quit', 'QUIT']:
        x.exit()
        s.close()
        print
    # print(send_data)
    s_data = pickle.dumps(send_data)
    s.send(s_data)
