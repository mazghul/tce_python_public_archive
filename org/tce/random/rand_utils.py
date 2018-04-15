#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
author:
    raja

source: (if any)

    https://pythonspot.com/python-set/
    
'''

from random import randint

def rand_int(max):
    return randint(0, max)

def get_programming():
    
    languages = set([
        "java", "c++", 'python', 'c#', 'angularjs'
        ])    
    languages.add('swift')    
    
    return list(languages)[randint(0, len(languages)-1)]




def main():
    print('Main')
    print(get_programming())

if __name__ == '__main__':
    main()