# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 20:35:13 2021

@author: maksimPC
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 20:57:39 2021

@author: maksimPC
"""

from numpy import exp
import headers_test as ht
import time
import json
import random
import requests
import variablesIP
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from requests.auth import HTTPBasicAuth

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

ip = variablesIP.IP()
aip = 'https://' + ip + '/index.php'
print(ip)

client = requests.session()
r = client.get(aip, headers=ht.headers, verify=False)
text = r.content.decode()
# print(text)

csrftoken = client.cookies.get_dict()
print(client.cookies.get_dict())

print("------------autorization-------------")

n, v = ht.namevalue(text)
print(n, v)
password=''
login=''

payload = {'usernamefld': "root",
           'passwordfld': "ting",
           'login': '1',
           n: v
           }

# автозицаия post  КУКИ НЕ РАБОТАЮТ


r = client.post(aip, data=payload, headers=ht.Headers_(csrftoken['PHPSESSID'], csrftoken['cookie_test'] ,ips=ip), verify=False)
# print(r.status_code, r.reason)
print("------------autorization-------------")

url = [
    'https://' + ip + '/system_usermanager.php?act=',
    'https://' + ip + '/system_certmanager.php?act='
    ]

url_text = [
    "/system_usermanager.php?act=",
    '/system_certmanager.php?act='
    ]

page = client.get(url[0], verify=False)

csrftoken = client.cookies.get_dict()

data = [
    {
        n: v,
        'act': 'new',
        'userid': '3',
        'priv_delete': '',
        'api_delete': '',
        'certid': '',
        'scope': 'user',
        'usernamefld': 'test18',
        'oldusername': '',
        'passwordfld1': 'test18',
        'passwordfld2': 'test18',
        'descr': '',
        'email': '',
        'comment': '',
        'landing_page': '',
        'language': 'По умолчанию.',
        'shell': '',
        'expires': '',
        'otp_seed': '',
        'authorizedkeys': '',
        'ipsecpsk': '',
        'save': 'save'

    },

    {n: v,
     'act': 'edit',
     'userid': '1'
     },

    {n: v,
     'act': 'newApiKey',
     'userid': '1',
     'username': ''
     },

    {n: v,
     'act': 'delApiKey',
     'userid': '1',
     'priv_delete': '',
     'api_delete': '---------',
     'certid': '',
     'scope': 'user',
     'usernamefld': 'test18',
     'oldusername': 'test18',
     'passwordfld1': '',
     'passwordfld2': '',
     'descr': '',
     'email': '',
     'comment': '',
     'landing_page': '',
     'language': 'По умолчанию.',
     'shell': '',
     'expires': '',
     'otp_seed': '',
     'authorizedkeys': '',
     'ipsecpsk': '',
     'id': '1'
     },

    {n: v,
     'act': 'new',
     'userid': '1',
     'certmethod': 'internal',
     'descr': 'test_serificate',
     'cert': '',
     'key': '',
     'caref_sign_csr': '6122bbf4200a1',
     'digest_alg_sign_csr': 'sha256',
     'lifetime_sign_csr': '397',
     'csr': '',
     'basic_constraints_path_len_sign_csr': '',
     'caref': '6122bbf4200a1',
     'cert_type': 'usr_cert',
     'keytype': 'RSA',
     'keylen': '2048',
     'curve': 'prime256v1',
     'digest_alg': 'sha256',
     'lifetime': '397',
     'private_key_location': 'firewall',
     'dn_country': 'RU',
     'dn_state': '-',
     'dn_city': '-',
     'dn_organization': '-',
     'dn_email': '230700-z@mail.ru',
     'dn_commonname': 'test9',
     'altname_type[]': 'DNS',
     'altname_value[]': '',
     'csr_keytype': 'RSA',
     'csr_keylen': '2048',
     'csr_curve': 'prime256v1',
     'csr_digest_alg': 'sha256',
     'csr_dn_country': 'AD',
     'csr_dn_state': '',
     'csr_dn_city': '',
     'csr_dn_organization': '',
     'csr_dn_organizationalunit': '',
     'csr_dn_email': '',
     'csr_dn_commonname': '',
     'certref': '6122bc10d8514',
     'save': 'Сохранить'
     },

    {
        n: v,
        'act': 'delcert',
        'userid': '1',
        'priv_delete': '',
        'api_delete': '',
        'certid': '0',
        'scope': 'user',
        'usernamefld': 'test_serificate',
        'oldusername': 'test_serificate',
        'passwordfld1': '',
        'passwordfld2': '',
        'descr': '',
        'email': '',
        'comment': '',
        'landing_page': '',
        'language': 'По умолчанию.',
        'shell': '',
        'expires': '',
        'otp_seed': '',
        'authorizedkeys': '',
        'ipsecpsk': '',
        'id': '1'
    }

]

act_get = ["new&userid=",
           'expcert&userid=',
           'expckey&userid=',
           "edit&userid=",
           ]

act_post = [
    "newApiKey&userid=",
    "delApiKey&userid=",
    "deluser&userid=",
    "delcert&userid="
]




def  mutatot(x):
    n=[]
    for i in x:
        n.append(i)        
    for i in range(1,len(n)):
        if(n[i] not in ['act', "api_delete", 'certmethod', 'userid']):        
            x[n[i]]=ht._generator(2,2)
    
    return x  
    
def test():
 
    count = True
    iteration_n=0
    
    
    
    while count:
        for i in range(len(act_get)):
            r = client.get(url[0] + act_get[i] + str(ht._generator()), headers=ht.headers, verify=False)
            print(r.status_code, ht._generator(), count)
    
        test = 0
        page = client.post(url[0] + act_get[0], data=data[0],
                           headers=ht.Headers_(csrftoken['PHPSESSID'], csrftoken['cookie_test'],ips=ip), verify=False)
        print(ip)    
        if(page.status_code=='500'):            
            f = open( 'HTML_error_500_'+str(iteration_n)+str(0)+'.txt', 'w' )
            for item in data[0]:
                f.write("%s: " % item)
            f.close()
        
        for i in range(0, 10):
            page = client.get(url[0] + act_get[3] + str(i), headers=ht.headers, verify=False)
            if (page.text.rfind('test18') != -1):
                test = i
                print(page.status_code, "successful write User") 
        s_key = ""
    
        data[2]['userid'] = test
        data[2] = mutatot(data[2])
        
        page = client.post(url[0] + act_post[0], data=data[2],
                           headers=ht.Headers_(csrftoken['PHPSESSID'], csrftoken['cookie_test'],ips=ip), verify=False)
        
        if(page.status_code=='500'):            
            f = open( 'HTML_error_500_'+str(iteration_n)+str(2)+'.txt', 'w' )
            for item in data[2]:
                f.write("%s: " % item)
            f.close()
        
        if (page.text.rfind('key') != -1):
            try:
                s_key = ht.Convert(page.text)
                s_key = s_key[1][1:len(s_key[1]) - 10].replace("\/", "/")
                print(page.status_code, "successful  write key API")
                data[3]['api_delete'] = s_key
            except:
                print("Error API")
        else:
            print("Error  write key API")
    
        data[3] = mutatot(data[3])    
        page = client.post(url[0] + act_post[1], data=data[3],
                           headers=ht.Headers_(csrftoken['PHPSESSID'], csrftoken['cookie_test'],ips=ip), verify=False)
        
        if(page.status_code=='500'):            
            f = open( 'HTML_error_500_'+str(iteration_n)+str(3)+'.txt', 'w' )
            for item in data[3]:
                f.write("%s: " % item)
            f.close()
        
        if (page.text.rfind('удален') != -1):
            print(page.status_code, "APi ключ удален")
        else:
            print(page.status_code, "Ошибка APi ключ  не удален")
    
        data[4] = mutatot(data[4])
        page = client.post(url[1] + act_post[2], data=data[4],
                           headers=ht.Headers_(csrftoken['PHPSESSID'], csrftoken['cookie_test'],ips=ip), verify=False)
            
        if(page.status_code=='500'):            
            f = open( 'HTML_error_500_'+str(iteration_n)+str(4)+'.txt', 'w' )
            for item in data[4]:
                f.write("%s: " % item)
            f.close()
        
        if (page.text.rfind('TING CA') != -1):
            print(page.status_code, "Sertificat is dowload")
        else:
            print(page.status_code, "Sertificat error")
    
        data[5] = mutatot(data[5])
        page = client.post(url[0] + act_post[3], data=data[5],
                           headers=ht.Headers_(csrftoken['PHPSESSID'], csrftoken['cookie_test'],ips=ip), verify=False)
            
        if(page.status_code=='500'):            
            f = open( 'HTML_error_500_'+str(iteration_n)+str(5)+'.txt', 'w' )
            for item in data[5]:
                f.write("%s: " % item)
            f.close()
        if (page.text.rfind('Ассоциация сертификата') != -1):        
            print(page.status_code, "Sertificat is delete")
        else:
            print(page.status_code, "Sertificat delete error")
            
        iteration_n+=1

