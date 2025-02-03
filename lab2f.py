#!/usr/bin/env python3

#Author ID: cthomas49

#Date Created: 2025/02/02

import sys

if len(sys.argv) != 2:
   print('Script needs 1 argument that is a number.')
   sys.exit(1) 
else:
    timer = int(sys.argv[1])
    while timer != 0:
        print(timer)
        timer = timer - 1
    print('blast off!')
