import socket

HOST = '192.168.100.9'  # The server's hostname or IP address
PORT = 5050        # The port used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    sendData=input('Enter the terminal command: ')
    s.sendall(sendData.encode())#sending the entered command to server
    if(sendData=="screenshot"):
        with open('received_file1.png','wb') as f:
            print('file opened')
            while(1):
                data=s.recv(1024)
                print("data",data)
                if not data:
                    print('finished receving')
                    break
                else:
                    f.write(data)
    else:
        data = s.recv(1024)
        if not data:
            s.close()
        if(data.decode()=="stop"):
            s.close()
        print('Received', repr(data))
        

    
