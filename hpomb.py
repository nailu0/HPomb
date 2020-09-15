#!/usr/bin/env python
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
import requests
from os import path

Red = '\033[1;31m'
Blue= '\033[1;36m'
Endc = '\033[0m'


  

verl = open("core/.version", 'r').read()


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

\tCreated by Honey Pots...

-------------------------------------------- 
"""
    print(Red+logo[0]+Blue+logo[1]+logo[2]+logo[3])


def banner1():
    clr()
    new_path = 'core/.da'
    new_days = open(new_path,'a')

    days_file = open(new_path,'r')

    da = days_file.read()

    if  da != '':
            headers={'User-Agent': 'Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)'}
            data={
            'id':da
            }
            url = "https://honeypots.tech/p/HPomb/user/user.php"
            r = requests.get(url,params = data, headers=headers)
            txt = r.text
            txt = txt.strip()
            use = txt
            userid = da
            while txt == '':
                print("\tSomething Wrong Please Contact To Developer")
                input("\tPlease Press Enter To Restart HPomb Tool :")
                subprocess.call([sys.executable, 'hpomb.py'])
    else :

            headers={'User-Agent': 'Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)'}
            url = "https://honeypots.tech/p/HPomb/user/id.php"
            r = requests.get(url,headers=headers)
            txt1 = r.text
            txt1 = txt1.strip()
            userid = str(txt1)
            use = str(1)
            print(userid)
            while txt1 == '':
                print("\tSomething Wrong Please Contact To Developer\n")
                input("\tPlease Press Enter To Restart HPomb Tool :")
                subprocess.call([sys.executable, 'hpomb.py'])
            new_days.write(txt1)
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

\tCreated by Honey Pots...

-------------------------------------------- 
    ID : """,userid,"""               USE : """,use,"""        
-------------------------------------------- 
\n"""
    print(Red+logo[0]+Blue+logo[1]+logo[2]+logo[3]+logo[4]+logo[5]+logo[6]+logo[7])

def home():
    print(Red +"""            [ Main Menu ] \n"""+ Blue + """
        
[01] Mail Bombing
[02] SMS Bombing 
[03] Call Bombing 
[04] Telegram Bombing [Inactive]
[05] vBeta Feature
[06] Donate For This Project
[07] Help [ Tutorials ]
[08] Exit 
""")

def checkinternet():
    res = False
    try:
        requests.get('https://www.google.com', verify=True)
        res = False
    except Exception:
        res = True
    if res:
        print("\n\n\tYour Internet Speed is Slow ...")
        print('\t\tHPomb Will Stop Now...\n\n')
        banner()
        exit()


def update():
    stuff_to_update = ['hpomb.py','core/ml.py','core/smcl.py','core/cl.py', 'core/tg.py','core/.version','requirements.txt']
    for fl in stuff_to_update:
        dat = urllib.request.urlopen(
            "https://raw.githubusercontent.com/HoneyPots0/HPomb/master/" + fl).read()
        file = open(fl, 'wb')
        file.write(dat)
        file.close()
    print('\n\t    Updated Successfull !!!')
    input('\n\tPress Enter To Run Again HBomb Tool: ')
    subprocess.call([sys.executable, 'hbomb.py'])




clr()
banner()
try:
    urllib.request.urlopen('https://www.google.com')
except Exception:
    print("   You are not connected To Internet!!!")
    print("\n  Please Connect To Internet To Continue...\n")
    input('   Press Enter To Run Again HPomb Tool ...')
    subprocess.call([sys.executable, 'hpomb.py'])

print('\t    Checking For Updates...')
ver = urllib.request.urlopen(
    "https://raw.githubusercontent.com/HoneyPots0/HPomb/master/core/.version").read().decode('utf-8')
verl = ''
try:
    verl = open("core/.version", 'r').read()
except Exception:
    pass
if ver != verl:
    print('\n\tNew Version Available : ', ver)
    print('\n\t  HBomb Tool Start Updating...')
    update()
print("\n\tYour Version is Up-To-Date")
print('\n\t     Starting HPomb...\n')





def at34():
    new_path = 'core/.da'
    days_file = open(new_path,'r')

    da = days_file.read()
    headers={'User-Agent': 'Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)'}
    data={
    'id':da
    }
    url = "https://honeypots.tech/p/HPomb/user/at.php"
    r = requests.get(url,params = data, headers=headers)
    


time.sleep(1)
clr()
banner1()
home()
at34()



bomb = input("Choose one options : ")
while bomb.isdigit() != True:
    bomb = input("\aInvalid ! Choose one options  [ 1 to 8]: ")

while int(bomb) > 8 :
    bomb = input("\aInvalid ! Choose one options  [ 1 to 8]: ")
clr()
banner()
if int(bomb) == 1 : 
    subprocess.call([sys.executable, 'core/ml.py'])
elif int(bomb) == 2 :
    subprocess.call([sys.executable, 'core/smcl.py'])
elif int(bomb) == 3 :
    subprocess.call([sys.executable, 'core/smcl.py', 'call'])
elif int(bomb) == 4 :
    subprocess.call([sys.executable, 'core/tg.py', 'call'])
    
    
elif int(bomb) == 5 :
            webbrowser.open('https://honeypots.tech/p/HPomb/', new=2)
            print("If You Use Mobile . May be Website not open automatically \n Visit : https://honeypots.tech/p/HBomb/")
            input("\nPress Enter To Run HBomb Tool Again : ")
            subprocess.call([sys.executable, 'hpomb.py'])
elif int(bomb) == 6 :
            webbrowser.open('https://honeypots.tech/p/HPomb/d/', new=2)
            print("If You Use Mobile . May be Website not open automatically \n Visit : https://honeypots.tech/p/HBomb/d/")
            input("\nPress Enter To Run HBomb Tool Again : ")
            subprocess.call([sys.executable, 'hpomb.py'])   
elif int(bomb) == 7:
        webbrowser.open('https://honeypots.tech/p/HPomb/help', new=2)
        print("If You Use Mobile . May be Website not open automatically \n Visit : https://honeypots.tech/p/HBomb/help")
        input("\nPress Enter To Run HBomb Tool Again : ")
        subprocess.call([sys.executable, 'hpomb.py'])

elif int(bomb) == 8:
    print("\tThank you for using ... Byee \n\n")
    exit()
else :
    home()
    bomb = input("\aInvalid ! Choose one options  [ 1 to 6]: ")
    clr()
    banner()
    if int(bomb) == 1 : 
        subprocess.call([sys.executable, 'core/ml.py'])
    elif int(bomb) == 2 :
        subprocess.call([sys.executable, 'core/smcl.py'])
    elif int(bomb) == 3 :
        subprocess.call([sys.executable, 'core/smcl.py', 'call'])
    elif int(bomb) == 4 :
        subprocess.call([sys.executable, 'core/tg.py'])
    elif int(bomb) == 5 :
            webbrowser.open('https://honeypots.tech/p/HPomb/', new=2)
            print("If You Use Mobile . May be Website not open automatically \n Visit : https://honeypots.tech/p/HPomb/")
            input("\nPress Enter To Run HBomb Tool Again : ")
            subprocess.call([sys.executable, 'hpomb.py'])
    elif int(bomb) == 6 :
            webbrowser.open('https://honeypots.tech/p/HPomb/d/', new=2)
            print("If You Use Mobile . May be Website not open automatically \n Visit : https://honeypots.tech/p/HBomb/d/")
            input("\nPress Enter To Run HBomb Tool Again : ")
            subprocess.call([sys.executable, 'hpomb.py'])
    elif int(bomb) == 7 :
            webbrowser.open('https://honeypots.tech/p/HPomb/help', new=2)
            print("If You Use Mobile . May be Website not open automatically \n Visit : https://honeypots.tech/p/HBomb/help")
            input("\nPress Enter To Run HBomb Tool Again : ")
            subprocess.call([sys.executable, 'hpomb.py'])

    elif int(bomb) == 8:
        print("\tThank you for using ... Byee \n\n")
        exit()
    else :
        home()
        bomb = input("\aInvalid ! Choose one options  [ 1 to 8]: ")

