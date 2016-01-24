#!/usr/bin/env python

import json

for a in xrange(32,256):
  b = json.dumps(unichr(a))
  if b.startswith("\"\\"):
    print a,b

