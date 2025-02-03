#!/usr/bin/env python3

#Author ID: cthomas49

#Date Created: 2025/02/02

import sys

if len(sys.argv) == 2:
    timer = int(sys.argv[1])
    while timer != 0:
            print(timer)
            timer = timer - 1
    print('blast off!')

else:
    timer = int(3)
    while timer != 0:
        print(timer)
        timer = timer - 1
    print('blast off!')
