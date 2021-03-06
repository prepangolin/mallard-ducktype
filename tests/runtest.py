#!/usr/bin/env python3

import os
import sys

sys.path.insert(0, (os.path.dirname(os.path.abspath(os.path.dirname(sys.argv[0])))))

import ducktype

try:
    parser = ducktype.DuckParser()
    parser.parse_file(sys.argv[1])
    parser.finish()
except ducktype.SyntaxError as e:
    print(os.path.basename(e.filename) + ':' +
          str(e.linenum) + ': ' + e.message)
    sys.exit(1)
parser.document.write_xml(sys.stdout)
