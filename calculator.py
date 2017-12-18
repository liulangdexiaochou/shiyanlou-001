#!/usr/bin/env python3
#jiangshurugongzibianchengzidian
def nashuie(b, dict1=None):
    if dict1 is None:
        dict1 = {}
    for b1 in b:
        dict1[b1.split(':')[0]] = b1.split(':')[1]
#    print(dict1)
#tiqugongzi,bingjisuan nashuie
    for key1,value1 in dict1.items():
        try:
            b2 = int(value1)
        except:
            print('Parameter Error')
        dict1[key1] = b2 - b2*0.165 -3500
#    print(dict1)
    return dict1

#jisuannashuie
def nashui(c):
    if c <= 0:
        c1 = 0
    if 0< c <= 1500:
        c1 = c*0.03
    if 1500 < c <= 4500:
        c1 = c*0.1 - 105
    if 4500 < c <= 9000:
        c1 = c*0.2 - 555
    if 9000 < c <= 35000:
        c1 = c*0.25 - 1005
    if 35000 < c <= 55000:
        c1 = c*0.30 - 2755
    if 55000 < c <= 80000:
        c1 = c*0.35 - 5505
    if c > 80000:
        c1 = c*0.45 - 13505
    c2 = c - c1 + 3500
    return c2
#    print(c1)

import sys
a = sys.argv[1:]
a1 = nashuie(a)
#a3 = nashui(13200.0)
#print(a1)
for key,value in a1.items():
    a1[key] = nashui(value)
#    print(a1)
#print(a1)
for key2,value2 in a1.items():
    print('%s%s%s' % (key2,':',"%.2f"%value2))
