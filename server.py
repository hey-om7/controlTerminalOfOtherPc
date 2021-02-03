import socket
import os
import subprocess as sp
import pyautogui

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5012        # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while(1):
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            
            data = conn.recv(1024)
            # print(data.decode())
            if not data:
                break
            
            elif(data.decode()=="byee"):
                conn.sendall("closing the server".encode())
                s.close()
                break
            elif(data.decode()=="screenshot"):
                print('getting screenshot')
                screenShot=pyautogui.screenshot()
                screenShot.save("screenshot.png")
                filename='screenshot.png'
                f=open(filename,'rb')
                n=f.read(1024)
                while(n):
                    conn.sendall(n)
                    print('Sent',repr(n))
                    n= f.read(1024)
                f.close()
                print('Sent full image data')
            else:
                try:
                    pipe = sp.Popen( data.decode(), shell=True, stdout=sp.PIPE, stderr=sp.PIPE )
                    res = pipe.communicate()
                    res="Response from server: "+str(res)
                    conn.sendall(res.encode())
                except:
                    conn.sendall("some random error")

                