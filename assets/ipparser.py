#!/usr/bin/env python3

import sys

file = open('/usr/local/share/Eternal_Scanner/vuln.txt','r')
files = open('assets/ip.txt', 'w')

# starts from 2nd line
file.readline()
file.readline()

lines = file.readlines()
ips = []
for i in lines:
    a = i.strip('\n').split(':')[0]
    ips.append(a)
    files.write(a+"\n")

files.close()
file.close()