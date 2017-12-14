#!/usr/bin/env python3
import sys
for a in sys.argv:
    break
try:
    n = int(sys.argv[1])
except ValueError:
    print("Value") 
a = (n - 3500)
if a <= 1500:
    c = a*3/100
    print(format(c,".2f"))
if 1500 < a <= 4500:
    c = a*10/100 - 105
    print(format(c,".2f"))
if 4500 < a <= 9000:
    c = a*20/100 - 555
    print(format(c,".2f"))
if 9000 < a <= 35000:
    c = a*25/100 - 1005
    print(format(c,".2f"))
if 35000 < a <= 55000:
    c = a*30/100 - 2755
    print(format(c,".2f"))
if 55000 < a <= 80000:
    c = a*35/100 - 5505
    print(format(c,".2f"))
if a > 80000:
    c = a*45/100 -13505
    print(format(c,".2f"))
#n = int(sys.argv[2])
#if a-3500 < 1500:
#    c = (a - 3500)*0.03
#    print(format(c,".2f"))
#else:
#    print(a)

