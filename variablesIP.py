

IP_variables="192.168.56.111"

def writes(y):
    f = open('IP_variables', 'w' )
    f.write("%s" % y)
    f.close()

def IP():  
    f = open('IP_variables', 'r')
    x=f.read()
    return x


