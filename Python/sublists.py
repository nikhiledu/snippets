#!/usr/bin/python
from types import *;
from itertools import chain;

l=[1,2,3]+[4,5,6]+[7]+[8,9]

for i in l:
  if type(i) is list:
    print("Found array: {}".format(i))

#f=list(chain.from_iterable(l))

#for i in f:
#  if type(i) is list:
#    print("Found array: {}".format(i))

print("l: {}".format(l))
#print("f: {}".format(f))
