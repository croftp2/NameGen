#!/usr/bin/python

#Paul Croft
#March 11, 2015

import cPickle
from pprint import pprint, pformat
import random


def main():
    cdata = None
    with open("data.cpk") as infile:
        cdata = cPickle.loads(infile.read())

#    pprint(cdata,depth=2)
#    pprint(cdata["Special Machine Names"]["Name"])
    for i in range(10):
        if not random.randint(0,3):
            print random.choice(cdata["Special Machine Names"]["Name"])
        else:
            Adj = random.choice(reduce(lambda x,y:x+y, cdata["Adjective List"].values()))
            Noun = random.choice(reduce(lambda x,y:x+y, cdata["Noun List"].values()))

            print Adj,Noun



if __name__ == '__main__':
    exit(main())
