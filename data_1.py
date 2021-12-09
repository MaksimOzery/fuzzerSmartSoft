data=[  

          
    {
         
        'act':'new',
        'certmethod': 'internal',
        'descr': 'ffff',
        'cert': '',
        'key': '',
        'caref_sign_csr': '619b94248a9a2',
        'digest_alg_sign_csr': 'sha256',
        'lifetime_sign_csr': '397',
        'csr': '',
        'basic_constraints_path_len_sign_csr':'' ,
        'caref': '619b94248a9a2',
        'cert_type':'usr_cert',
        'keytype': 'RSA',
        'keylen': '2048',
        'curve': 'prime256v1',
        'digest_alg': 'sha256',
        'lifetime': '397',
        'private_key_location': 'firewall',
        'dn_country': 'AD',
        'dn_state': 'mo',
        'dn_city': 'Озеры',
        'dn_organization': 'ssm',
        'dn_email':'mail@mail.ru',
        'dn_commonname': '234',
        'altname_type[]': 'DNS',
        'altname_value[]':'' ,
        'csr_keytype': 'RSA',
        'csr_keylen': '2048',
        'csr_curve': 'prime256v1',
        'csr_digest_alg': 'sha256',
        'csr_dn_country': 'AD',
        'csr_dn_state': '',
        'csr_dn_city': '',
        'csr_dn_organization': '',
        'csr_dn_organizationalunit': '',
        'csr_dn_email':'' ,
        'csr_dn_commonname': '',
        'certref': '619b949b283ee',
        'save': 'Сохранить'
    
    
    },
          

            #id: 0
            #firewall_nat_edit.php?id=0",
            { 
            'interface[]': 'wan',
            'ipprotocol': 'inet',
            'protocol': 'tcp',
            'src': 'any',
            'srcmask': '128',
            'srcbeginport': 'any',
            'srcendport': 'any',
            'dst': 'any',
            'dstmask': '32',
           'dstbeginport': '80',
            'dstendport': '80',
            'target': 'bogons',
            'local-port': '80',
            'poolopts':'' ,
            'log': 'yes',
            'category[]': '99',
            'descr': '99',
            'tag': '99',
            'tagged': '99',
            'natreflection': 'purenat',
            'filter-rule-association': 'add-associated',
            'Submit': 'Сохранить'
            },
   
    {
              
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
       
     #https://192.168.56.110/firewall_nat_edit.php
          {  
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
         {     
              'id':'', 
              'act':"", 
              'mode': 'automatic',
              'save': 'Save',
      
          },
           #https://192.168.56.110/firewall_nat_npt_edit.php?after=-1
          {     
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
            
            'id': '',
            'act': 'edit',
            'scrub_interface_disable': 'yes',
            'scrubnodf': 'yes',
            'scrubrnid': 'yes',
        
          },
         #"https://192.168.56.110/firewall_schedule_edit.php"  
         {   
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
                    
                    'action': '',
                    'id': '',
                    'lan':' em0',
                    'wan': 'em1',
                    'Submit': 'yes'
                    
                    },
            
            #'/interfaces_assign.php',
            
                {
                                     
                    'action': '',
                    'id': '',
                    'lan': 'em0',
                    'wan': 'em1',
                    'Submit': 'yes'
                    
                    },
            #'/interfaces_bridge_edit.php',
                {
                    
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
                                     
                    'ifname': 'htthth',
                    'descr': 'rgrgrgrg',
                    'members[]': 'lan',
                    'submit': 'save'
                    },
            #'/interfaces_lagg_edit.php' &&&  Родительский интерфейс,
            
                {
                    
                    'proto': 'lacp',
                    'descr': "tset",
                    'lacp_fast_timeout': 'yes',
                    'mtu': '1000',
                    'laggif': '',
                    'Submit': 'save'
                    },
            #'/interfaces_ppps_edit.php',
            
                {
                    
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
                    
                    'if': 'em0',
                    'tag': '44',
                    'pcp': '0',
                    'descr': '444',
                    'vlanif': '',
                    'Submit': 'save'
                    
                    },
            #'/interfaces_wireless_edit.php'   
             {
                    
                   'descr': 'test',
                   'mode': 'bss',
                   'cloneif': '',
                   'Submit': 'save'
                    },
                    
                     
                   {
          
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
            
            'name': 'Local Database',
            'type': 'local',
            'enable_password_policy_constraints': 'on',
            'password_policy_duration': '0',
            'password_policy_length': '8',
            'save': 'Сохранить',
            'id': '0'
        },
                
                
                
        {
            
           'id': '0',
           'act': 'del'     
           }
        ,
        {
        
        'authmode': 'Local Database',
        'username': 'mak',
        'password': '123',
        'save': 'Save'  
                 
        }            
       
              
]
