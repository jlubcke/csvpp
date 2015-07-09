#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import csv
from io import StringIO
from itertools import count
import sys
try:
    # Python 2
    from itertools import izip_longest
except ImportError:
    # Python 3
    from itertools import zip_longest as izip_longest

def csvpp(csv_input):

    max_widths = []
    max_indent = 0
    for line in csv.reader(StringIO(csv_input)):
        widths = [len(s.strip()) for s in line]
        max_widths = list(map(max, izip_longest(max_widths, widths, fillvalue=0)))
        indent = len(line[0]) - len(line[0].lstrip())
        max_indent = max(max_indent, indent)

    result = StringIO()
    for line in csv.reader(StringIO(csv_input)):
        result.write(u' ' * max_indent)

        last_column = len(line) - 1
        for value, max_width, column in zip(line, max_widths, count()):
            value = value.strip()
            result.write(u"" + value)
            if column != last_column:
                result.write(u", ")
                result.write(u" " * (max_width - len(value)))

        result.write(u'\n')

    return result.getvalue()


def main():
    csv_input = sys.stdin.read().decode('utf-8')
    sys.stdout.write(csvpp(csv_input).encode('utf-8'))

