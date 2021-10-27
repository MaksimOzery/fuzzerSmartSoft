# -*- coding: utf-8 -*-
"""
genetic algoritm
"""
import sys
import time
import string
import random
import logging
import variablesIP
import headers_test as ht
from optparse import OptionParser
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from itertools import *
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from requests.auth import HTTPBasicAuth
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
    
    

__version__ = "1.0"


logger = logging.getLogger('')

# form genetic codes
GENES = "".join(map(lambda x, y: x+y, string.ascii_uppercase, string.ascii_lowercase)) + \
        string.punctuation + " "
GOAL = ""   

#--------------------------------------------------------------------------
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
         ip_+'/interfaces_wireless_edit.php',  
         ip_ + '/system_groupmanager.php?act=',
         ip_ + '/system_groupmanager.php',
         ip_ + '/system_usermanager_addprivs.php?groupid=',
         ip_ + '/system_authservers.php?act=',        
         ip_ + '/system_authservers.php',
         ip_ + '/diag_authentication.php'
         ]
    

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
            'Submit': 'save'
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
            'Submit': 'save'   
         
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
            'Submit': 'save'
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
            'Submit': 'save'
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
            'Submit': 'save'  
          
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
            'Submit': 'save'
       
          
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
            'Submit': 'save'
          
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
            'submit': 'save'
           
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
                    'Submit': 'save'
                    
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
                'Submit': 'save'
                    
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
                    'Submit': 'save'
                    
                    },
            #'/interfaces_groups_edit.php',
                {
                    n:v,                 
                    'ifname': 'htthth',
                    'descr': 'rgrgrgrg',
                    'members[]': 'lan',
                    'submit': 'save'
                    },
            #'/interfaces_lagg_edit.php' &&&  Родительский интерфейс,
            
                {
                   n:v, 
                    'proto': 'lacp',
                    'descr': "tset",
                    'lacp_fast_timeout': 'yes',
                    'mtu': '1000',
                    'laggif': '',
                    'Submit': 'save'
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
                    'Submit': 'save',
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
                    'Submit': 'save'
                    
                    },
            #'/interfaces_wireless_edit.php'   
             {
                   n:v, 
                   'descr': 'test',
                   'mode': 'bss',
                   'cloneif': '',
                   'Submit': 'save'
                    },
                     
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
         'save': 'Save'

       },
           {
            n:v,
            'name': 'Local Database',
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
        'save': 'Save'  
                 
        }            
         
              
]


page =  client.get(url[0], verify=False )

csrftoken =  client.cookies.get_dict()
print(page.status_code)
#-------------------------------------------------------------------
        
def active(client,s, url,csrftoken_PHPSESSID,csrftoken_cookie_test):       
    page =  client.post(url,data=s, headers=ht.Headers_(csrftoken_PHPSESSID, csrftoken_cookie_test,ips=ip),   verify=False )
    return page        
        
def fitness(dnk, goal):
    f = 0
    for index, gene in enumerate(dnk):
        if gene != goal[index]:
            f -= 1
    return f

def sample_wr(population, k):
    n = len(population)
    _random, _int = random.random, int  # speed hack 
    result = [None] * k
    for i in range(k):
        j = _int(_random() * n)
        result[i] = population[j]
  
    return result


class GeneticCode:
    def __init__(self, dnk="", goal=GOAL):
        if dnk == "":
            self.dnk = "".join(sample_wr(GENES, len(goal)))
        else:
            self.dnk = dnk
        self.goal = goal

    def get(self):
        return self.dnk

    def fitness(self):
        return fitness(self.dnk, self.goal)
    
    def mutate(self, turns=5):
        _dnk = list(self.dnk)
        for item in range(turns):
            rnd_elem_index = random.randint(0, len(_dnk)-1)
            if _dnk[rnd_elem_index] == self.goal[rnd_elem_index]:
                pass
            else:
                _dnk[rnd_elem_index] = random.choice(GENES)
        self.dnk = "".join(_dnk)

    def replicate(self, another_dnk):  
        part = random.randint(0, len(self.dnk)-1)
        return "".join(self.dnk[0:part] + another_dnk.get()[part:])


class GenePool():
    pool_size = 100
    
    def __init__(self, goal, init, json,url):
        self.pool = [GeneticCode(goal=goal) for item in range(self.pool_size)]
        self.goal = goal
        self.init=init
        self.json=json
        self.url=url
    def _print(self):
        for item in self.pool:
            print( item.get() + " - " + str(item.fitness()))

    def get_random(self):
        
        return self.pool[random.randint(0, len(self.pool)-1)]

    def darvin(self, winners=0.1):

        all_fitness = [(item.fitness(), item) for item in self.pool]
        
        new_pool = [item[1] for item in
                    sorted(all_fitness, key=lambda x: x[0], reverse=True)]       
        
        self.pool = new_pool[:int(round(self.pool_size * winners))]

        while len(self.pool) < self.pool_size:
            new_life = self.get_random().replicate(self.get_random())
            new_gc = GeneticCode(dnk=new_life, goal=self.goal)
            self.pool.append(new_gc)

    def evolution(self, turns=1000):
        
        iterations = 0
        while (iterations < turns) and (self.pool[0].get() != self.goal):
            for index, item in enumerate(self.pool):
                self.pool[index].mutate()
            self.darvin()
            self.requset_evolution(self.json, self.pool)
            
            logger.info(self.pool[0].get())
            time.sleep(0.1)
            iterations += 1
            
        return iterations

    def requset_evolution(self, j, k):
        massiv=[]
        for item in k:
            massiv.append(item.get())            
        for i in range(len(massiv)):        
            j[self.init]=massiv[i]
            
            info=active(client,j,self.url,csrftoken['PHPSESSID'],csrftoken['cookie_test'])
            if(info.status_code==500):
                print("-------------------------")  
                f = open( 'HTML_500.txt', 'w' )
                f.write("%s" % str(j[self.init])+"key"+str(self.init))
            elif(info.status_code==200):
                print(self.url, "code 200" )
            
    
def copy_data(data):     
    for k in range(len(data)):
        n=[]
        for i in data[k]:
            n.append(i)
        for key in range(1,len(n)):
            data[k][n[key]]=ht.get_mutation(data[k][n[key]])            
    return data



def test():
    for s in range(len(data)):
        n=[]
        
        for i in data[s]:
            n.append(i)
        for K in range(1,len(n)): 
            gp = GenePool(data[s][n[K]],n[K],data[s], url[s])   
            
            steps = gp.evolution()  
            logger.info("Steps: %d" % steps)
        
       

start_time = time.time()
test()
print()
print( "Estimatied time:\t%s" % (time.time() - start_time))
