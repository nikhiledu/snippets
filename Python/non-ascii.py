#!/usr/bin/python
import sys

def whatisthis(s):
    if isinstance(s, str):
        print("ordinary string")
    elif isinstance(s, unicode):
        print("unicode string")
    else:
        print("not a string")

def is_ascii(s):
  s.decode('ascii')

whatisthis("""components:

tools-fff
tools-ggg
tools-jjj-vpn
email: john.1@gov.uk
firstname: 'John '
lastname: 1
role: xxx
team: 'Data '""")

