# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 19:35:09 2021

@author: maksimPC
"""

from numpy import exp

import time
import json
import random
import requests
import headers_test as ht
import variablesIP
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from requests.auth import HTTPBasicAuth
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
    
    










def test():
    ip=variablesIP.IP_variables
    aip='https://'+ip+'/index.php'
    

     
    
      
    
    
    
    client = requests.session()
    r = client.get( aip,  headers=ht.headers, verify=False )
    text=r.content.decode()
    #print(text)
    
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
         ip_+'/system_usermanager.php?act=new' ,    
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
         ]
    
    url_text=[
            "/system_usermanager.php?act=new",
            #---------------------------------
             "/firewall_nat_edit.php",     
             "/firewall_nat_1to1_edit.php",
             "/firewall_nat_out.php",
             "/firewall_nat_npt_edit.php?after=-1",
             "/firewall_rules_edit.php?if=FloatingRules",
             "/firewall_rules_edit.php?if=lan",
             "/firewall_rules_edit.php?if=lo0",
             "/firewall_rules_edit.php?if=wan",
             "/system_advanced_firewall.php",
             "/firewall_scrub.php",
             "/firewall_schedule_edit.php",
             #-------------------------
            '/interfaces.php',
            '/interfaces_assign.php',      
            '/interfaces_bridge_edit.php',       
            '/interfaces_gif_edit.php',
            '/interfaces_gre.php',
            '/interfaces_gre_edit.php',        
            '/interfaces_groups_edit.php',        
            '/interfaces_lagg_edit.php',        
            '/interfaces_ppps_edit.php',        
            '/interfaces_vlan_edit.php',        
            '/interfaces_wireless_edit.php'
             
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
            'usernamefld': 'tet9s',
            'oldusername': '',
            'passwordfld1': 'test',
            'passwordfld2': 'tstgh',
            'descr':'test' ,
            'email':'test@mail.ru' ,
            'comment': 'test',
            'landing_page': 'https://192.168.56.107/index.php',
            'language': 'По умолчанию.',
            'shell':'', 
            'expires':'09/30/2021' ,
            'groups[]': 'admins',
            'otp_seed':'' ,
            'authorizedkeys':'' ,
            'ipsecpsk':'' ,
            'save': 'save'
            
        },
     #https://192.168.56.110/firewall_nat_edit.php
          {  n:v,
            'disabled': 'yes',
            'nordr': 'on',
            'interface[]': 'wan',
            'ipprotocol': 'inet',
            'protocol': 'tcp',
            'src': 'any',
            'srcmask': '32',
            'srcbeginport': 'any',
            'srcendport': 'any',
            'dst': '12.8.8.1',
            'dstmask': '32',
            'dstbeginport': '80',
            'dstendport': '80',
            'local-port': '',
            'descr': '',
            'tag': '',
            'tagged': '',
            'nosync': 'yes',
            'natreflection': 'purenat',
            'Submit': 'Сохранить'
            },
         
           #https://192.168.56.110/firewall_nat_1to1_edit.php
        {
             n:v,
            'interface': 'wan',
            'type': 'binat',
            'external': '10.0.8.8',
            'src': '10.8.8.9',
            'srcmask': '32',
            'dst': '(self)',
            'dstmask': '32',
            'descr': '',
            'natreflection': 'default',
            'Submit': 'Сохранить'   
         
         },
         #https://192.168.56.110/firewall_nat_out.php
         {     n:v,
              'id':'', 
              'act':"", 
              'mode': 'automatic',
              'save': 'Save',
      
          },
           #https://192.168.56.110/firewall_nat_npt_edit.php?after=-1
          {     n:v,
               'interface': 'wan',
               'src': '',
               'srcmask': '128',
               'dst': '',
               'dstmask': '128',
               'descr': '',
               'Submit': 'Save',
               'after': '',
                           
                     },
           #https://192.168.56.110/firewall_rules_edit.php?if=FloatingRules
          {
            n:v, 
            'id': '0',
            'after': '',
            'floating': 'yes',
            'type': 'reject',
            'quick': 'yes',
            'direction': 'in',
            'ipprotocol': 'inet',
            'protocol': 'udp',
            'icmptype': '',
            'icmp6-type': '',
            'src': 'wan',
            'srcmask': '32',
            'srcbeginport': '5999',
            'srcendport': '123',
            'dst': '(self)',
            'dstmask': '32',
            'dstbeginport': 'any',
            'dstendport': 'any',
            'descr': '',
            'os': '',
            'sched': '',
            'gateway': '',
            'set-prio': '',
            'set-prio-low': '',
            'prio': '',
            'tag': '',
            'tagged': '',
            'max': '',
            'max-src-nodes': '',
            'max-src-conn': '',
            'max-src-states': '',
            'max-src-conn-rate': '',
            'max-src-conn-rates': '',
            'statetimeout': '',
            'statetype': 'keep state',
            'Submit': 'Сохранить'
           },
         
         #https://192.168.56.110/firewall_rules_edit.php?if=lan 
         
         {      
             n:v,
            'id':'' ,
            'after': '',
            'floating': '',
            'type': 'pass',
            'quick': 'yes',
            'interface': 'lan',
            'direction': 'in',
            'ipprotocol': 'inet',
            'protocol': 'any',
            'icmptype':'' ,
            'icmp6-type':'' ,
            'src': 'any',
            'srcmask': '32',
            'dst': '(self)',
            'dstmask': '32',
            'descr': '',
            'os': '',
            'sched': '',
            'gateway': '',
            'set-prio':'' ,
            'set-prio-low': '',
            'prio': '',
            'tag': '',
            'tagged':'' ,
            'max':'' ,
            'max-src-nodes': '',
            'max-src-conn': '',
            'max-src-states': '',
            'max-src-conn-rate': '',
            'max-src-conn-rates': '',
            'statetimeout': '',
            'statetype': 'keep state',
            'Submit': 'Сохранить'
            },
      
         #https://192.168.56.110/firewall_rules_edit.php?if=lo0 
         {
          
            n:v,
            'id': '',
           'after': '',
            'floating': '',
            'type': 'pass',
            'quick': 'yes',
            'interface': 'wan',
            'direction': 'in',
            'ipprotocol': 'inet',
            'protocol': 'tcp',
            'icmptype': '',
            'icmp6-type': '',
            'src': 'wan',
            'srcmask': '32',
            'srcbeginport': 'any',
            'srcendport': 'any',
            'dst': 'any',
            'dstmask': '32',
            'dstbeginport': '53',
            'dstendport': '53',
            'descr': '',
            'os': '',
            'sched': '',
            'gateway': 'Null4',
            'set-prio': '',
            'set-prio-low': '',
            'prio': '',
            'tag': '',
            'tagged': '',
            'max': '',
            'max-src-nodes': '',
            'max-src-conn': '',
            'max-src-states': '',
            'max-src-conn-rate': '',
            'max-src-conn-rates': '',
            'statetimeout': '',
            'statetype': 'keep state',
            'Submit': 'Сохранить'  
          
          },
            
         #https://192.168.56.110/firewall_rules_edit.php?if=wan  
         
       
              {
          
            n:v,
            'id': '',
            'after': '',
            'floating': '',
            'type': 'pass',
            'quick': 'yes',
            'interface': 'wan',
            'direction': 'in',
            'ipprotocol': 'inet',
            'protocol': 'any',
            'icmptype': '',
            'icmp6-type':'' ,
            'src': '(self)',
            'srcmask': '32',
            'dst': 'lan',
            'dstmask': '32',
            'descr': '',
            'os': '',
            'sched': '' ,
            'gateway': '',
            'set-prio': '',
            'set-prio-low': '' ,
            'prio': '',
            'tag': '',
            'tagged': '', 
            'max': '',
            'max-src-nodes': '',
            'max-src-conn': '',
            'max-src-states': '',
            'max-src-conn-rate': '',
            'max-src-conn-rates': '',
            'statetimeout': '',
            'statetype':'keep state',
            'Submit': 'Сохранить'
       
          
          },
    
         #"https://192.168.56.110/system_advanced_firewall.php" 
         {
             n:v,
            'ipv6allow': 'yes',
            'natreflection': 'yes',
            'enablebinatreflection': 'yes',
            'enablenatreflectionhelper': 'yes',
            'bogonsinterval': 'monthly',
            'kill_states': 'yes',
            'lb_use_sticky': 'yes',
            'srctrack': '',
            'pf_share_forward': 'yes',
            'optimization': 'normal',
            'rulesetoptimization': 'basic',
            'adaptivestart': '',
            'adaptiveend': '',
            'maximumstates': '12',
            'maximumfrags': '2',
            'maximumtableentries': '2',
            'disablereplyto': 'yes',
            'aliasesresolveinterval': '2',
            'checkaliasesurlcert': 'yes',
            'Submit': 'Сохранить'
          
          },
         # "https://192.168.56.110/firewall_scrub.php"    +
         {
            n:v,
            'id': '',
            'act': 'edit',
            'scrub_interface_disable': 'yes',
            'scrubnodf': 'yes',
            'scrubrnid': 'yes',
        
          },
         #"https://192.168.56.110/firewall_schedule_edit.php"  
         {   n:v,
            'name': 'test',
            'descr': 'test2',
            'monthsel': '10',
            'starttimehour': '0',
            'starttimemin': '00',
            'stoptimehour': '23',
            'stoptimemin': '59',
            'timerangedescr': '' ,
            'starttime0': '1:00',
            'stoptime0': '2:59',
            'timedescr0': '',
            'schedule0': 'w35p4-m9d2,w35p5-m9d3,w36p3-m9d8,w36p4-m9d9,w36p5-m9d10,w37p3-m9d15,w37p6-m9d18,w38p6-m9d25,w39p5-m10d1,w40p4-m10d7',
            'submit': 'Сохранить'
           
          },
            #'/interfaces.php',
            
                {
                   n:v, 
                    'action': '',
                    'id': '',
                    'lan':' em0',
                    'wan': 'em1',
                    'Submit': 'yes'
                    
                    },
            
            #'/interfaces_assign.php',
            
                {
                    n:v,                 
                    'action': '',
                    'id': '',
                    'lan': 'em0',
                    'wan': 'em1',
                    'Submit': 'yes'
                    
                    },
            #'/interfaces_bridge_edit.php',
                {
                   n:v, 
                    'members[]':'lan',
                    'descr': 'rrffff',
                    'proto': 'rstp',
                    'maxage': '',
                    'fwdelay': '',
                    'hellotime': '',
                    'priority': '',
                    'holdcnt': '',
                    'ifpriority_lan': '',
                    'ifpriority_wan': '',
                    'ifpathcost_lan': '',
                    'ifpathcost_wan': '',
                    'maxaddr': '',
                    'timeout': '',
                    'span': 'none',
                    'bridgeif': '',
                    'Submit': 'Сохранить'
                    
                    },
            
            #'/interfaces_gif_edit.php',
            
            
                {
                   n:v, 
                 'if': 'lan',
                'remote-addr': '10.8.8.1',
                'tunnel-local-addr': '10.8.8.0',
                'tunnel-remote-addr': '10.8.8.8',
                'tunnel-remote-net': '32',
                'link0': 'on',
                'link1': 'on',
                'descr': 'i]oo',
                'gifif': '',
                'Submit': 'Сохранить'
                    
                    },  
            #'/interfaces_gre_edit.php',
            
                {
                    n:v, 
                    'if': 'lan',
                    'remote-addr': '10.8.0.8',
                    'tunnel-local-addr': '10.8.0.8',
                    'tunnel-remote-addr': '10.8.0.8',
                    'tunnel-remote-net': '32',
                    'link0': 'on',
                    'link1': 'on',
                    'link2': 'on',
                    'descr': 'dddd',
                    'greif': '',
                    'Submit': 'Сохранить'
                    
                    },
            #'/interfaces_groups_edit.php',
                {
                    n:v,                 
                    'ifname': 'htthth',
                    'descr': 'rgrgrgrg',
                    'members[]': 'lan',
                    'submit': 'Сохранить'
                    },
            #'/interfaces_lagg_edit.php' &&&  Родительский интерфейс,
            
                {
                   n:v, 
                    'proto': 'lacp',
                    'descr': "tset",
                    'lacp_fast_timeout': 'yes',
                    'mtu': '1000',
                    'laggif': '',
                    'Submit': 'Сохранить'
                    },
            #'/interfaces_ppps_edit.php',
            
                {
                   n:v, 
                    'type': 'ppp',
                    'descr': 'test',
                    'country': 'AF',
                    'provider_list': 'AWCC',
                    'providerplan': 'internet',
                    'username': 'awcc',
                    'password': '1111',
                    'phone': '*99#',
                    'apn': 'internet',
                    'provider': '',
                    'null_service': 'on',
                    'hostuniq': '',
                    'apnum': '5445',
                    'simpin': '45455',
                    'pin-wait': '455545454',
                    'initstr': '54544554',
                    'connect-timeout': '455544545',
                    'uptime': 'on',
                    'ondemand': 'on',
                    'idletimeout': '',
                    'mschap': 'on',
                    'ccp': 'on',
                    'mppc': 'on',
                    'mppc-compression': 'on',
                    'mppc-e40': 'on',
                    'mppc-e56': 'on',
                    'mppc-e128': 'on',
                    'mppc-stateless': 'on',
                    'vjcomp': 'on',
                    'tcpmssfix': 'on',
                    'shortseq': 'on',
                    'acfcomp': 'on',
                    'protocomp': 'on',
                    'Submit': 'Сохранить',
                    'ptpid': '0'
                    
                    },
            #'/interfaces_vlan_edit.php',
                {
                   n:v, 
                    'if': 'em0',
                    'tag': '44',
                    'pcp': '0',
                    'descr': '444',
                    'vlanif': '',
                    'Submit': 'Сохранить'
                    
                    },
            
            
            
            
            #'/interfaces_wireless_edit.php'   
             {
                   n:v, 
                   'descr': 'test',
                   'mode': 'bss',
                   'cloneif': '',
                   'Submit': 'Сохранить'
                    },
         
              
    
        ]
        
        
    
    memory=''
    count= True 
    n=[]
    T=1

    while count:
        
        for i in range(len(data)): 
            
            
            
            for j in data[i]:
                n.append(j)
     
            memory=data
            print("------------------"+str(T)+"----------------------\n")        
            for key in range(1,len(n)):
    
                data[i][n[key]]=ht.get_mutation(data[i][n[key]])
                print("data:",data[i][n[key]],"key:",n[key])
                
                
                
                if random.random()< 0.05:               
                    data[0][str(ht._generator())]=str(ht._generator())
                    
                ht.write_data(data) 
                page =  client.post(url[i],data=data[i], headers=ht.Headers_(csrftoken['PHPSESSID'],csrftoken['cookie_test'],url_text[i], ips=ip),   verify=False )
                print(page.status_code, page.reason)
                if(page.status_code==500):
                   print(page.status_code, page.reason)
               
                   print("-------------------------")  
                   f = open( 'HTML_500'+n[key]+str(i)+'.txt', 'w' )
                   for item in page.text:
                       f.write("%s" % item)
            
            n.clear() 
                     
        data=memory
        T+=1
        
    print("Request end")










