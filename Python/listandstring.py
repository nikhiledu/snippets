#!/usr/bin/python
from types import *;
from itertools import chain;

list1=["one","two","three"]
str1="four"
str2="five"
str3=None

#print("list1+str1: {}".format(list1+str1))
if str3:
  print("list1+str1: {}".format(list1+str3))
print("[str1]+list1: {}".format([str1]+list1))
#print("[str1]+str2: {}".format([str1]+str2))
if str3:
  print("[str1]+str2: {}".format([str1]+str3))
