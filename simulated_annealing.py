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
from itertools import *
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from requests.auth import HTTPBasicAuth
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
    
    
ip="192.168.56.107"
aip='https://'+ip+'/'+'index.php'
password=''
login=''

client = requests.session()
r = client.get( aip,  headers=ht.headers, verify=False )
text=r.content.decode()
#print(text)

csrftoken =  client.cookies.get_dict()
print(client.cookies.get_dict())


print("------------autorization-------------") 

n, v=ht.namevalue(text)
print( n, v)

payload = {'usernamefld':"root",
           'passwordfld':"ting",
           'login':'1', 
            n:v 
          } 

#автозицаия post  КУКИ НЕ РАБОТАЮТ


r = client.post( aip,  data=payload,  headers=ht.Headers_(csrftoken['PHPSESSID'],csrftoken['cookie_test'], ips=ip),  verify=False )
#print(r.status_code, r.reason)
print("------------autorization-------------")  

url=[
     'https://'+ip+'/system_usermanager.php?act=new',  
     ]

url_text=[        
         "/system_usermanager.php?act=new",     
         ]


page =  client.get(url[0], verify=False )

csrftoken =  client.cookies.get_dict()

data=[{ 
         n:v ,     
        'act': 'new',
        'userid': '',
        'priv_delete': '',
        'api_delete': '',
        'certid': '',
        'scope': 'user',
        'usernamefld': 'te',
        'oldusername': '',
        'passwordfld1': 'tet9',
        'passwordfld2': 'tt9',
        'descr':'' ,
        'email':'' ,
        'comment': '',
        'landing_page': '',
        'language': 'По умолчанию.',
        'shell':'', 
        'expires':'' ,
        'otp_seed':'' ,
        'authorizedkeys':'' ,
        'ipsecpsk':'' ,
        'save': 'save'
        
    }]


chars = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9', "%","$","@","{","}","[","]",":"]



def _generator(s,key,memory):
    rand_chain=random.random()
    if rand_chain<0.25:
        for i in range(20):
            s[0][key]+=str(chars[random.randint(0,len(chars)-1)])
    elif rand_chain >0.25 and rand_chain<0.75:
        memory2= s[0][key]
        s[0][key]=""
        variant=""
        for cur in chars[random.randint(0,len(chars)):random.randint(0,len(chars)-1)]:                     
            variant += str(''.join(cur))   
        for i in range(random.randint(0,len(memory2)),len(memory2)):           
            s[0][key]=str(variant)+str(memory2[i])
            
    else:
        s[0][key]=memory
    return s


def active(client,s, url,csrftoken_PHPSESSID,csrftoken_cookie_test, key):  
    try:
      
        page =  client.post(url,data=s[0], headers=ht.Headers_(csrftoken_PHPSESSID, csrftoken_cookie_test,ips=ip),   verify=False , timeout=1.5)
       
    except:
        print("----------no connection---------")                           
        f = open( 'HTML_500.txt', 'a' )                           
        f.write("staus code %s " % 'no connection')                          
        f.write("data: %s " % s[0])
        f.write("key: %s  " % key)
        f.write("%s" % "\n")
        f.close()
       
    return page   

def ocenka(data,x,s, keys):   
    if(data.status_code==500):
        print("-------------------------")  
        f = open( 'HTML_500.txt', 'a' )                           
        f.write("staus code %s " % 'no connection')                          
        f.write("data: %s " % s[0])
        f.write("key: %s  " % key)
        f.write("%s" % "\n")
        f.close()
        return (100*x)/len(s[0]),  data.status_code,1

    elif(data.status_code==200 and data.text.rfind('успешно')!=-1 ):
        return (100*x)/len(s[0]),  data.status_code,1
 
    return 1 ,  data.status_code ,0

def simulated_annealing(active,  n_iterations, step_size, temp,data,
                        client, url,csrftoken_PHPSESSID,
                        csrftoken_cookie_test,url_text):
    n=[] 
    for i in data[0]:
        n.append(i)
    memory=data
    status=""
    value_n=1
    Value_n2=0
    S=""
    best=''
    Request=0
    
    for j in range(random.randint(1,len(n)),len(n)):
        
        s=_generator(data,n[j],memory) 
        
        info=active(client,s,url,csrftoken_PHPSESSID,
                    csrftoken_cookie_test,n[j])      
        best, status,Value_n2=ocenka(info,value_n,s,n[j])
        curr_eval = best
        print("-------------------"+str(j)+"---------------------\n")
        value_n+=Value_n2
        for i in range(n_iterations):
             s=_generator(data,n[j],memory)             
             dataN=active(client,s,url,csrftoken_PHPSESSID,
                          csrftoken_cookie_test,n[j])
             bestN,status,Value_n2=ocenka(dataN,value_n,s,n[j])
             Request+=1 
             value_n+=Value_n2
             if bestN < best:
                 data=s
                 best=bestN
             diff = bestN - curr_eval
             t = temp / float(i + 1)
             print(Request)
             metropolis = exp(-diff / t)
             if diff < 0 or  random.random() < metropolis:  
                 data, best = s, bestN
        print("Request ",Request)    
        S=data
    return S, best,status

n_iterations = 2000
step_size = 0.1
temp = 10



def test():

    simulated_annealing(active, n_iterations, step_size, temp,data, client,url[0],csrftoken['PHPSESSID'],csrftoken['cookie_test'],url_text[0])
