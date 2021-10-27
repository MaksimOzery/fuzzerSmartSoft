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




'''
def  mutatot(x):
    n=[]
    for i in x:
        n.append(i)        
    for i in range(1,len(n)):
        if(n[i] not in ['act', "id"]):        
            x[n[i]]=ht._generator(2,2)
    
    return x  
'''
    
def test():
    #ip = variablesIP.IP()
    ip="192.168.56.107"
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
        'https://' + ip + '/system_authservers.php?act=',        
        'https://' + ip + '/system_authservers.php',
        'https://' + ip + '/diag_authentication.php'
        ]
    
     
    page = client.get(url[0], verify=False)
    
    csrftoken = client.cookies.get_dict()
    
    data = [
     
         
        {
          n:v,
        'name': 'test1',
        'type': 'ldap',
        'ldap_host': '10.08.01.0',
        'ldap_port': '389',
        'ldap_urltype': 'TCP - Standard',
        'ldap_protver': '3',
        'ldap_binddn': 'mak',
        'ldap_bindpw': '123',
        'ldap_scope': 'one',
        'ldap_basedn': '',
        'ldapauthcontainers': '9o',
        'ldap_extended_query': '',       
         'ldap_tmpltype': 'open',
         'ldap_attr_user': 'cn',
         'save': 'Сохранить'
        

        
        
        
        
       },
           {
            n:v,
            'name': 'Локальная база данных',
            'type': 'local',
            'enable_password_policy_constraints': 'on',
            'password_policy_duration': '0',
            'password_policy_length': '8',
            'save': 'Сохранить',
            'id': '0'
        },
                
                
                
        {
            n:v,
           'id': '0',
           'act': 'del'     
           }
        ,
        {
        n:v,
        'authmode': 'Local Database',
        'username': 'mak',
        'password': '123',
        'save': 'Проверка'  
                 
        }  
                
    
       
    ]
    
    
    act_post = [
        "new",        
        'edit&id=',
        ''
    ]

 
    count = True
    iteration_n=0
    
    
    
    while count:
        #new
        n=[]
        for i in range(len(data)):            
            
            
            for j in data[i]:                 
                n.append(j)
     
            memory=data
            
            for key in range(1,len(n)):
                if(n[key] not in ['act', "id"]):
                    data[i][n[key]]=ht.get_mutation(data[i][n[key]])
                    
            if random.random()< 0.05:               
                    data[i][str(ht._generator())]=str(ht._generator())
                    
            ht.write_data(data,"write")  
            page = client.post(url[0] + act_post[0], data=data[0],
                           headers=ht.Headers_(csrftoken['PHPSESSID'], csrftoken['cookie_test'],ips=ip), verify=False)
            print(page.text.rfind( 'Обнаружены следующие ошибки ввода'))
            print(data[0])
            if(page.status_code=='500'):         
                f = open( 'HTML_error_500_'+str(iteration_n)+str(1), 'w' )
                for item in data[0]:
                    f.write("%s: " % item)
                f.close()   
                
            test=''        
            for k in range(0, 20):
                page = client.get(url[0] + act_post[1]+str(k), headers=ht.headers, verify=False)                
                if (page.text.rfind( data[0]['name']) != -1):
                    test = k                    
                    print(page.status_code,k, "successful write ")
                    break
                    if(page.status_code=='500'):  
                        print(page.status_code, "Error get") 
                
              
            ht.write_data(data,"edit")    
            page = client.post(url[0] + act_post[1], data=data[1],
                           headers=ht.Headers_(csrftoken['PHPSESSID'], csrftoken['cookie_test'],ips=ip), verify=False)
            
            if(page.status_code=='500'): 
                print(data[1])
                print(page.status_code, "Error get") 
            elif(page.status_code=='200'):
                print(page.status_code, "edit write ")
            
            
            try:
                data[2]['id']= test
                print("H:",data[2]['id'])
                ht.write_data(data, "delete")
                page = client.post(url[1] + act_post[3], data=data[2],
                                   headers=ht.Headers_(csrftoken['PHPSESSID'], csrftoken['cookie_test'],ips=ip), verify=False)       
                print(page.status_code, " delete User")
            except:
                print(" Error delete User, not found")
            
            data=memory   
            n.clear()
            iteration_n+=1
    
        print("ssssssssssssssssssssssss")
        s_n=[]
        for j in data[i]:                 
            s_n.append(j)
     
    
        memory=data
        for key in range(1,len(s_n)):
            if(s_n[key] not in ['act', "id"]):
                data[i][s_n[key]]=ht.get_mutation(data[i][s_n[key]]) 
                
        if random.random()< 0.05:               
            data[i][str(ht._generator())]=str(ht._generator())        
        ht.write_data(data,"test user") 
        
        page = client.post(url[2] + act_post[2], data=data[3],
                               headers=ht.Headers_(csrftoken['PHPSESSID'], csrftoken['cookie_test'],ips=ip), verify=False)            
                
        if(page.status_code=='500'): 
            print(data[1])
            print(page.status_code, "Error user") 
        elif(page.status_code=='200'):
            print(page.status_code, " user test 200 ") 
        else:
            print(page.status_code, " error not found ")
        data=memory   
        s_n.clear()

test()
