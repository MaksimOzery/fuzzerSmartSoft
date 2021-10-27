from numpy import exp
import time
import json
import random
import requests
import json
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from requests.auth import HTTPBasicAuth
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9', "%","$","@"]    


def write_data(x):
    n=[]
    f = open('data_variables', 'w', encoding='utf-8' )
    for i in range(len(x)):
        for j in x[i]:
            n.append(j)
    
    
        f.write("%s" % "\n_________________________\n")
        for key in range(1,len(n)):
            f.write("%s" % str(n[key])+":"+str(x[i][n[key]])+"\n")
        n.clear() 
    f.close()
    
    
    



    
def _generator(n=4,k=8):    
    chrs = ''
    for i in range(n):
        for j in range(k):
            chrs+=chars[random.randint(0,len(chars)-1)] 
    return chrs   
   
def get_mutation(txt):
    items = []
    for c in txt:
        # Шанс 10% 
        if random.randint(0, 9) == 0:
            c = chr((ord(c) + random.randint(0, 255)) % 255)
        items.append(c)
    return ''.join(items)
 
def Convert(string, symbol=":"):
    li = list(string.split(symbol))
    return li
 

def input_(html):
    parsed_html = BeautifulSoup(html)
    print("=>pasing html\n")
    print("get=>inputl")
    print("\n")
    name=[]
    _id=[]
    for link in parsed_html.find_all('input'):        
        name.append(link.get('name'))
    for link in parsed_html.find_all('input'):        
        _id.append(link.get('id'))    
    print("----------------------")
    
    return name ,_id

def namevalue(html):
    parsed_html = BeautifulSoup(html)
    print("=>pasing html\n")
    print("get=>name and value")
    print("\n")
    name=''
    value=''
    for link in parsed_html.find_all('input' , type="hidden"):
        name=link.get('name')        
    for link in parsed_html.find_all('input', type="hidden"):
        value=link.get('value')    
    print("----------------------")
    return name ,value



def Headers_(PHPSESSID='',cookie_test='', slash="/", ips=''):
    header_info = {      
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8,en-US;q=0.7",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Content-Length": "111",
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": "PHPSESSID="+str(PHPSESSID)+"; cookie_test="+str(cookie_test),
                "Host": ips,
                "Origin": "https://"+ips,
                "Referer": "https://"+ips+slash,
                "sec-ch-ua-mobile": "?0",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
                }    
    return header_info


#идентификация агента
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}