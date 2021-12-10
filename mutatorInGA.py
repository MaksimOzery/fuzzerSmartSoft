# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 19:35:09 2021

@author: maksimPC
"""

from numpy import exp
import time
import data_1
import json
import random
import requests
import headers_test as ht

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from requests.auth import HTTPBasicAuth
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
    
    
def data_write(n,v,data_1):
 
    data={n:v}
    data.update(data_1)
    return data

     
def request_server_algRead(ip):
    _ip="http://"+ip+":8081/algEnd.php"
    client = requests.session()
    return client.get(_ip, verify=False ).text 


def test(x):
    ip=x
    print(ip)
    aip='https://'+ip+'/index.php'
    
 
    
    
    
    client = requests.session()
    r = client.get( aip,  headers=ht.headers, verify=False, timeout=5 )
    text=r.content.decode()
   
    
    csrftoken =  client.cookies.get_dict()
    print(client.cookies.get_dict())
    
    
    print("------------autorization-------------") 
    
    n, v=ht.namevalue(text)
    print( n, v)
    
    payload = {'usernamefld': "root",
               'passwordfld':"ting",
               'login':'1', 
                n:v 
               } 
    
    #автозицаия post  КУКИ НЕ РАБОТАЮТ
    
    
    r = client.post( aip,  data=payload,  headers=ht.Headers_(csrftoken['PHPSESSID'],csrftoken['cookie_test'],ips=ip),  verify=False )
    #print(r.status_code, r.reason)
    print("------------autorization-------------")  
    
    ip_='https://'+ip
    url=[
         ip_+'/system_usermanager.php?act=new',     
         '''
         ip_+"/firewall_nat_edit.php",     
         ip_+"/firewall_nat_1to1_edit.php",
         ip_+"/firewall_nat_out.php",
         ip_+"/firewall_nat_npt_edit.php?after=-1",
         ip_+"/firewall_rules_edit.php?if=FloatingRules",
         ip_+"/firewall_rules_edit.php?if=lan",
         ip_+"/firewall_rules_edit.php?if=lo0",
         ip_+"/firewall_rules_edit.php?if=wan", 
         ip_+"/system_advanced_firewall.php",
         ip_+"/firewall_scrub.php",
         ip_+"/firewall_schedule_edit.php",   
         #---------------------------------------
         ip_+'/interfaces.php',
         ip_+'/interfaces_assign.php',     
         ip_+'/interfaces_bridge_edit.php',    
         ip_+'/interfaces_gif_edit.php',   
         ip_+'/interfaces_gre_edit.php',     
         ip_+'/interfaces_groups_edit.php',     
         ip_+'/interfaces_lagg_edit.php',
         ip_+'/interfaces_ppps_edit.php', 
         ip_+'/interfaces_vlan_edit.php',   
         ip_+'/interfaces_wireless_edit.php'  
         '''         
         ]
   
    
    page =  client.get(url[0], verify=False )
    
    csrftoken =  client.cookies.get_dict()
    
    memory=''
    count= True 
    n2=n
    n=[]
    T=1
    
    iterations = 0
    inetaration_status_break=0
    while count:
        if(inetaration_status_break==2):
            break
               
        for i in range(0,1): 
            number_request=0
            data= data_write(n2,v,data_1.data[0])
            for j in data:
                n.append(j)
            old_memory=""
            memory=data
            print("------------------"+str(T)+"----------------------\n")   
            inetaration_status=0            
            starttimes = time.time()
            for key in range(1,len(n)):
                iterations+=1
                data[n[key]]=ht._generator()
                
                if(inetaration_status==0):
                    try:
                        memoris=request_server_algRead(ip)
                        if(memory==old_memory):
                            if((time.time()-starttimes)/60>=2):
                                inetaration_status=1
                                print(url[0] ," ", iterations, " end time and data not changed ",(time.time()-starttimes)/60)  
                        else:
                            old_memory=memoris
                            memory=data  
                    except:
                           print("----------no connection---------")                           
                           f = open( 'HTML_500.txt', 'a' )                           
                           f.write("staus code %s " % 'no connection')                          
                           f.write("data: %s " % data[n[key]])
                           f.write("key: %s  " % n[key])
                           f.write("%s" % "\n")
                           f.close()
                           return 
                           
                   
                    try:
                        page =  client.post(url[0],data=data,  timeout=25 ,headers=ht.Headers_(csrftoken['PHPSESSID'],csrftoken['cookie_test'], ips=ip),   verify=False )                
                        number_request+=1
                        if(page.status_code==500):
                           print(page.status_code, page.reason)               
                           print("-----------post--------------")  
                           f = open( 'HTML_500.txt', 'a' )                           
                           f.write("staus code %s " % 'no connection')                          
                           f.write("data: %s " % data[n[key]])
                           f.write("key: %s  " % n[key])
                           f.write("%s" % "\n")
                           f.close()
                    except:
                           inetaration_status=1
                           print("-----------except post--------------")  
                           f = open( 'HTML_500.txt', 'a' )                           
                           f.write("staus code %s " % 'no connection')                          
                           f.write("data: %s " % data[n[key]])
                           f.write("key: %s  " % n[key])
                           f.write("%s" % "\n")
                           f.close()
                           

            
            n.clear() 
        print("Request",number_request )
        iterations = 0
        data=memory
        T+=1
        
    print("Request end")










