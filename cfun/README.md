
To make a custom script into an executable command in the linux console, you must copy it to ``/usr/local/bin`` and ensure it has permissions to +rwx with ``chmod``. This can be doen with shell scripts (.sh) as well as ``python``, but you must first declare the env at top.
example python: ``#!/usr/bin/env python``
example bash: ``#!/bin/bash``


# fkill (arg)
this command searches for an active process named by the arg. fkill b/c i use it to find processes to kill.

# genpass.py
generates a 16 character alphanumeric password using special characters.
example: HR3hvOn&DY_@yF&=

# genserial.py
generates a random number that is 72 digits long. 10^72 (a trevingintillion) possibilities.
example: 093562007002907445922206027958409276969037095676272290691766921290494198

# now.py
just reformats the DATE function into a format I prefer.
i.e. "It is NOW: 14/10/24 and  10:50:52"

# pwcheck.py
checks the strength of a give password to ensure it has: at least 16 chars, mixed upper and lower case, numbers, special characters, and no spaces. if password fails, reasons why are returned and user is prompted to try again.
