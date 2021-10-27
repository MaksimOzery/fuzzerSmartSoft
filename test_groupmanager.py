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
        'https://' + ip + '/system_groupmanager.php?act=',
        'https://' + ip + '/system_groupmanager.php',
        'https://' + ip + '/system_usermanager_addprivs.php?groupid='
        ]
    
     
    page = client.get(url[0], verify=False)
    
    csrftoken = client.cookies.get_dict()
    
    data = [
        {
            n: v,
            'act': '',
            'groupid': '',
            'privid': '',
            'scope':'' ,
            'name': 'test_ss',
            'description': '11111',
            'members[]': '0',
            'save': 'Сохранить'
        },
         {
          n:v,
          'act': 'delgroup',
          'groupid': '2',
          'groupname': 'test_ss'
          
          },
               
                
    
       
    ]
    
    
    act_post = [
        "new",
        "",
        'edit&groupid='
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
            print(data[i])
            for key in range(1,len(n)):
                if(n[key] not in ['act', "id","groupid"]):
                    data[i][n[key]]=ht.get_mutation(data[i][n[key]])
                    
            if random.random()< 0.05:               
                    data[0][str(ht._generator())]=str(ht._generator())
            
            page = client.post(url[0] + act_post[0], data=data[0],
                           headers=ht.Headers_(csrftoken['PHPSESSID'], csrftoken['cookie_test'],ips=ip), verify=False)
            #print(data[0])
            #print(data[1])
            if(page.status_code=='500'):         
                f = open( 'HTML_error_500_'+str(iteration_n)+str(1), 'w' )
                for item in data[0]:
                    f.write("%s: " % item)
                f.close()   
                
            test=''        
            for k in range(1, 20):
                page = client.get(url[0] + act_post[2]+str(i), headers=ht.headers, verify=False)                
                if (page.text.rfind( data[0]['name']) != -1):
                    test = k
                    break
                    print(page.status_code,k, "successful write User") 
                    if(page.status_code=='500'):  
                        print(page.status_code, "Error get") 
              
            data[1]['groupid']=test   
            data[1]['groupname']= data[0]['name']
            print("H:",data[0]['name'])
            ht.write_data(data)
            page = client.post(url[1] + act_post[1], data=data[1],
                               headers=ht.Headers_(csrftoken['PHPSESSID'], csrftoken['cookie_test'],ips=ip), verify=False)       
            print(page.status_code, " delete User") 
            data=memory   
            n.clear()
            
            
        iteration_n+=1

test()
