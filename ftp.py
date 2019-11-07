#! /usr/bin/env python 
# -*- coding: UTF-8 -*-
#(c) Xavier 2019

# pour débugger… en ligne de commande !-) 
#import pdb; pdb.set_trace()  

from ftplib import FTP
ftp = FTP('ftp.monsite.com', 'user', 'password')  


f_name = "mon_fichier.txt"
f = open(f_name, 'rb')
ftp.storbinary('STOR ' + f_name, f)
f.close()

#ftp.delete(f_name)

#connect.sendcmd('CWD test')
