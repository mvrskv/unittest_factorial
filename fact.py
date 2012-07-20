'''
Created on 05.07.2012

@author: mrasskazov
'''

def fact(n):
    f = n
    while n >= 3:
        n -= 1
        f *= n
    return f 


if __name__ == '__main__':
    for n in xrange(0, 10):
        print n, fact(n)
