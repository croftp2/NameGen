#!/usr/bin/python

#Paul Croft
#March 11, 2015

import cPickle
from pprint import pprint, pformat
import random
from sys import argv

def main():
    todo = 10
    if len(argv) - 1:
        try:
            todo = int(argv[1])
        except ValueError:
            pass

    cdata = None
    with open("data.cpk") as infile:
        cdata = cPickle.loads(infile.read())

#    pprint(cdata,depth=2)
#    pprint(cdata["Special Machine Names"]["Name"])
    for i in range(todo):
        if not random.randint(0, 3):
            print random.choice(cdata["Special Machine Names"]["Name"])
        else:
            Adj = random.choice(reduce(lambda x, y: x+y, cdata["Adjective List"].values()))
            Noun = random.choice(reduce(lambda x,y : x+y, cdata["Noun List"].values()))

            print Adj, Noun



if __name__ == '__main__':
    exit(main())
