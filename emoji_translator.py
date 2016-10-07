#!/usr/bin/python3
import argparse
import sys
from unicodedata import name
from string import punctuation
exclude = ({chr(x) for x in range(256)}|{x for x in '█\ufeff\'’'})-{x for x in
                                                             '(){}[#@$-~=^!?+'}
mapping = {"AUBERGINE": "EGGPLANT"}

delete = {"VARIATION", "SELECTOR"}

def parse2(s, exclude=exclude, mapping=mapping, delete=delete):
    """Blah"""
    return ' '.join(map(lambda x: mapping.get(x, x),
                        ''.join(map(lambda x: x if all(map(lambda w: w not in
                                                           x, delete)) else '',
                                    map(lambda x: x if x in exclude else
                                        " %s "%name(x, ' '), s))).split()))

def parse(s, exclude=exclude, mapping=mapping, delete=delete):
    """Blah"""
    return ' '.join([mapping.get(x, x) for x in
                     ''.join([x if all(word not in x for word in delete) else
                              '' for x in [' '+name(x, x)+' ' if x not in exclude else x for x in
                              s]]).split()])

if __name__ == '__main__':
    try:
        s = sys.stdin.read()
        sys.stdout.write(str(parse2(s)))
    except KeyboardInterrupt:
        pass
    sys.exit(0)
