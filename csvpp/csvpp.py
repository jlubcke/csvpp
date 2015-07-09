#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import csv
from io import StringIO
from itertools import izip_longest
import sys


def csvpp(csv_input):

    max_widths = []
    indent = 0
    for line in csv.reader(StringIO(csv_input)):
        widths = [len(s.strip()) for s in line]
        max_widths = map(max, izip_longest(max_widths, widths, fillvalue=0))
        indent = max(indent, len(line[0]) - len(line[0].lstrip()))

    result = StringIO()
    for line in csv.reader(StringIO(csv_input)):
        result.write(u' ' * indent)
        result.write(u''.join(value + u", " + u" " * (width - len(value)) for value, width in zip([s.strip() for s in line], max_widths)).rstrip()[:-1])
        result.write(u'\n')

    return result.getvalue()


def main():
    csv_input = sys.stdin.read().decode('utf-8')
    sys.stdout.write(csvpp(csv_input).encode('utf-8'))

