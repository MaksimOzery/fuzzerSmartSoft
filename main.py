#import Interfaces
import simulated_annealing
#import mutatorIn
#import mutatorInGA
#import GA
from numpy import exp
import time
import json
import random
import requests
import headers_test as ht
import variablesIP
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from itertools import *
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from requests.auth import HTTPBasicAuth
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup




def main():
    
    
    simulated_annealing.test()
    #simulated_annealing.test()    
    #Interfaces.test()
    
   
main()