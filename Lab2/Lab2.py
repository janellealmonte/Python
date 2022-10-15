#!/usr/bin/env python3

import sys

#This stores the first argument as a string object
name = sys.argv[1]
#This stores the second argument as a string object
age = sys.argv[2]

print('Hi ' + name + ', you are '+str(age)+' years old.')
print('The script and variables used are:')
print('variable1 = '+name)
print('variable2 = '+age)
