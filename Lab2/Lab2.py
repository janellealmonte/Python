#!/usr/bin/env python3

import sys

def f1(country, year):
    print('You arrived in ' + country + ' in '+str(year)+'')
    print('The script and variables used are:')
    print('var1 = '+country)
    print('var2 = '+year)

if __name__ == '__main__':
    #This stores the first argument as a string object
    country = sys.argv[1]
    #This stores the second argument as a string object
    year = sys.argv[2]
    f1(country, year)

