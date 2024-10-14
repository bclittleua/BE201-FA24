#! /usr/bin/env python
import random as r
p = '0123456789'
print(''.join([p[r.randint(0,len(p)-1)] for i in range(72)]))
