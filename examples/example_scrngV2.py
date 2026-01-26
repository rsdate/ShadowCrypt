"""
TODO: Make this work

import datetime
import sys
import time

import colorama

from src.scrngV2.scrngV2 import random_nums

colorama.init(autoreset=True)


def delay_print(s, delay: float = 0.1):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")


def example_scrngV2():
    delay_print(
        "Welcome to scrypt! This is the example associated with the core algorithm."
    )
    delay_print("There are 2 functions that you can use: ")


example_scrngV2()
"""
