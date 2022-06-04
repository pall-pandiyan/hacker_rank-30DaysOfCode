#!/bin/python3

import math
import os
import random
import re
import sys

def main():
    N = int(input().strip())
    if(N%2 == 1):
        print("Weird")
    else:
        if( N>=6 and N<=20):
            print("Weird")
        else:
            print("Not Weird")

if __name__ == '__main__':
    main()