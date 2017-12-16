#!/usr/bin/env python3
def f(c, gdict={}):
    b= n - n*0.165 - c
    i=l1[0]
    gdict[i] = b
    for key,value in gdict.items():
        print(key,":",end='')
        print(format(value,".2f"))
l1dict = {}
import sys
for a1 in sys.argv[1:]:
    l1 = a1.split(':')
#    print(l1[0])
    l1dict[l1[0]] = l1[1]
#    print(l1dict)
for key in l1dict.keys():
    n1 = key
#    print(key)
try:
    n = int(l1dict[n1])
except ValueError:
    print("Paramenter Error")
a = n - n*0.165 - 3500
#print(a)
if a <= 1500:
    c = a*3/100
#    print(format(c,".2f"))
if 1500 < a <= 4500:
    c = a*10/100 - 105
#    print(format(c,".2f"))
if 4500 < a <= 9000:
    c = a*20/100 - 555
#    print(format(c,".2f"))
if 9000 < a <= 35000:
    c = a*25/100 - 1005
#    print(format(c,".2f"))
if 35000 < a <= 55000:
    c = a*30/100 - 2755
#    print(format(c,".2f"))
if 55000 < a <= 80000:
    c = a*35/100 - 5505
#    print(format(c,".2f"))
if a > 80000:
    c = a*45/100 -13505
#    print(format(c,".2f"))
#f(c,gdict={})
b= n - n*0.165 - c
l1dict[key] = format(b,".2f")
#print(l1dict)
for key,value in l1dict.items():
#    print(key,value)
    print('%s%s%s' % (key,':',value))
#    print(key.join(format(value,".2f")))
