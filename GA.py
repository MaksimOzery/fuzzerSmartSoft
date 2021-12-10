# -*- coding: utf-8 -*-
"""
genetic algoritm
"""
import sys
import time
import string
import random
import logging
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
import data_1


def data_write(n,v,data_1):
    data={n:v}
    data.update(data_1)
    return data

logger = logging.getLogger('')

# form genetic codes
GENES = "".join(map(lambda x, y: x+y, string.ascii_uppercase, string.ascii_lowercase)) + \
        string.punctuation + " "
GOAL = ""   

#--------------------------------------------------------------------------
ip="192.168.56.107"
#ip="192.168.50.2"
#ip="192.168.50.3"
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



r = client.post( aip,  data=payload,    headers=ht.Headers_(csrftoken['PHPSESSID'],csrftoken['cookie_test'],ips=ip),  verify=False )
#print(r.status_code, r.reason)
print("------------autorization-------------")  

ip_='https://'+ip    
url=[
         ip_+'/system_usermanager.php?act=new',            
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
         ip_ + '/system_groupmanager.php?act=',
         ip_ + '/system_groupmanager.php',
         ip_ + '/system_usermanager_addprivs.php?groupid=',
         ip_ + '/system_authservers.php?act=',        
         ip_ + '/system_authservers.php',
         ip_ + '/diag_authentication.php'
        
         ]
    



def request_server_algRead(ip):
    _ip="http://"+ip+":8081/algEnd.php"

    client = requests.session()

    return client.get(_ip, verify=False ).text


page =  client.get(url[0], verify=False )

csrftoken =  client.cookies.get_dict()

#-------------------------------------------------------------------
        
def active(client,s, url,csrftoken_PHPSESSID,csrftoken_cookie_test, key):  
    try:
        page =  client.post(url,data=s, headers=ht.Headers_(csrftoken_PHPSESSID, csrftoken_cookie_test,ips=ip),   verify=False , timeout=1.5)
    except:
        print("----------no connection---------")                           
        f = open( 'HTML_500.txt', 'a' )                           
        f.write("staus code %s " % 'no connection')                          
        f.write("data: %s " % s)
        f.write("key: %s  " % key)
        f.write("%s" % "\n")
        f.close()
        return  
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
        self.memory=""
        self.old_memory=""
        self.starttimes=0
        self.inetaration_status=1
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
        self.inetaration_status=0
        iterations = 0
        self.starttimes = time.time()  
        R=0
        while (iterations < turns) and (self.pool[0].get() != self.goal):
            if(self.inetaration_status==0):
                for index, item in enumerate(self.pool):
                    self.pool[index].mutate()
                self.darvin()
                R =self.requset_evolution(self.json, self.pool) 
                time.sleep(0.1)
                iterations += 1
                self.memory=request_server_algRead(ip)
                if(self.memory==self.old_memory):
                    if((time.time()-self.starttimes)>=2):
                        self.inetaration_status=1
                else:
                    self.old_memory=self.memory
            else:
                break
        
        return R
    def requset_evolution(self, j, k):
        massiv=[]
        text_m=0
        R=0
        for item in k:
            massiv.append(item.get())            
        for i in range(len(massiv)):        
            j[self.init]=massiv[i]            
            info=active(client,j,self.url,csrftoken['PHPSESSID'],csrftoken['cookie_test'], massiv[i])  
                        
            if(info.status_code==500):
                print("-------------------------")  
                f = open( 'HTML_500.txt', 'a' )                           
                f.write("staus code %s " % 'no connection')                          
                f.write("data: %s " % data[n[key]])
                f.write("key: %s  " % n[key])
                f.write("%s" % "\n")
                f.close()
            elif(info.status_code==200):
                R+=1
                
        return   R
    
def copy_data(data):     
    for k in range(len(data)):
        n=[]
        for i in data[k]:
            n.append(i)
        for key in range(1,len(n)):
            data[k][n[key]]=ht.get_mutation(data[k][n[key]])            
    return data



def test():
    steps_new=""
     
    for s in range(len(data_1.data)):
        
        data= data_write(n,v,data_1.data[0])
        name=[]
        
        for i in data:            
            name.append(i)
        for K in range(1,len(name)): 
            print("-----------------------"+str(K)+"--------------------------------")
            data= data_write(n,v,data_1.data[0])            
            gp = GenePool(data[name[K]],name[K],data, url[0])             
            steps  = str(gp.evolution()  )            
            print("Request ",steps)
            #print(chr(27) + "[2J")
        
       

start_time_ = time.time()


test()
print()
print( "Estimatied time:\t%s" % (time.time() - start_time_ ))
