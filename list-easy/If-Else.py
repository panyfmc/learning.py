# Dado m valor n, execute as condições dos ifs

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 != 0:                  # Se n for impar
        print("Weird")
    elif n % 2 == 0 and n >= 2 and n<= 5:        # Se n for par e está na range de 2 até 5
        print("Not Weird")
    elif n % 2 == 0 and n >= 6 and n <= 20:       # range de 6 até 20
        print("Weird")
    else:
        print("Not Weird")
