import re

def myInput(prompt, regex):
    data = raw_input (prompt)
    if re.match(regex, str(data)):
        return data
    return False

vart = myInput("test de rpompt", '[a-z]+')

print (vart)

#a = input('Entrez une valeur quelconque')
#if a:
#    print "vrai"
#else:
#    print "faux"
