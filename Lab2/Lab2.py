#!/usr/bin/env python3

#A function that uses command line arguments. This function will print two variables used, the script and then the script AND variables.
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

def helloWorld():
	print(‘Hello World’)


helloWorld()
