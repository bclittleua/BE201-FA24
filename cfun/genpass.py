#! /usr/bin/env python
import random as r
p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-='
print(''.join([p[r.randint(0,len(p)-1)] for i in range(16)]))
