import socket
import threading
import xo
import pickle

HOST = 'localhost'
PORT = 50000
# 0 = server 1 = client
turn = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print('Connected by', addr)
data = ''


def switchTurn():
    global turn
    if turn == 1:
        turn = 0
    else:
        turn = 1


def getTurn():
    global turn
    return turn


def fetchValue(sInput):
    myList = []
    word = ""
    sInput = sInput.strip()
    lastIndex = 0
    for index in sInput:
        if(lastIndex == len(sInput)-1):
            word += index
            myList.append(word)
            word = ""
        elif(index == " "):
            myList.append(word)
            word = ""
        elif(index != " "):
            word = word + index
        lastIndex += 1

    return myList


def pr_msg():
    while 1:
        data = conn.recv(1024)
        p_data = pickle.loads(data)
        mydata_re = fetchValue(p_data)
        
            
        try:
            if mydata_re[0] == "set" and (int(mydata_re[1]) <= 2 or int(mydata_re[2]) <= 2) and getTurn() == 1:
                xo.editTable(int(mydata_re[1]), int(mydata_re[2]), "O")
                newTable = pickle.dumps(xo.sampletable)
                conn.send(newTable)
                xo.showTable()
                print("Winner is :", xo.chackWin(xo.sampletable))
                switchTurn()
            if(xo.chackWin(xo.sampletable) in "XO"):
                end = pickle.dumps("ENDGAME")
                conn.send(end)
                print("ENDGAME")

            if mydata_re[0] == "turn":
                    if turn == 0:
                        sender = pickle.dumps("Not your turn")
                        conn.send(sender)
                    else:
                        sender = pickle.dumps("You turn")
                        conn.send(sender)
            elif mydata_re[0] == "chat":
                fullmsg = 'Client : '
                for msg in mydata_re:
                    if msg != "chat":
                        fullmsg += msg
                        fullmsg += " "
                print("\n"+fullmsg)
        except Exception as err:
            print("Someting worng")

        


x = threading.Thread(target=pr_msg)
x.start()
starter_msg = 0
while 1:
    if(starter_msg == 0):
        print("Start game SERVER turn first")
        sender = pickle.dumps("Start game SERVER turn first")
        conn.send(sender)
        starter_msg = 1
    send_data = input("Server : ")
    if send_data[:4] in ['quit', 'Quit', 'QUIT']:
        x.exit()
        conn.close()
    myData = fetchValue(send_data)
    # ----------------------------------------
    
    
    try:
       
        if myData[0] == "set" and (int(myData[1]) <= 2 or int(myData[2]) <= 2 and getTurn() == 0):
            switchTurn()
            xo.editTable(int(myData[1]), int(myData[2]), "X")
            newTable = pickle.dumps(xo.sampletable)
            conn.send(newTable)
            xo.showTable()
            print("Winner is :", xo.chackWin(xo.sampletable))
            if(xo.chackWin(xo.sampletable) in "XO"):
                end = pickle.dumps("ENDGAME")
                conn.send(end)
                print("ENDGAME")
        if myData[0] == "turn":
                if turn == 0:
                    print("You turn")
                else:
                    print("Not You turn")
        elif myData[0] == "chat":
            fullmsg = 'SERVER : '
            for msg in myData:
                if msg != "chat":
                    fullmsg += msg
                    fullmsg += " "
            sender = pickle.dumps(fullmsg)
            conn.send(sender)
        elif myData[0] == "reset":
            xo.reset()
            print("table reset")
            xo.showTable()
            sender = pickle.dumps("table reset")
            conn.send(sender)
    except Exception as err:
        print("Someting worng")
