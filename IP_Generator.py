#!/usr/bin/env python
import subprocess
import random
import time

first = [1, 2]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Time = 0
flag = 0
number = ""
ip = ""


def Generate(first, number, numbers, flag, ip):
    while True:
        number = ""
        number1 = random.choice(first)
        number2 = random.choice(numbers)
        number3 = random.choice(numbers)
        number += f'{number1}{number2}{number3}'

        if int(number) < 255:
            if flag <= 2:
                ip += str(f'{number1}{number2}{number3}') + "."
                flag += 1
            else:
                ip += str(f'{number1}{number2}{number3}')
                return ip


while True:
    ip = Generate(first, number, numbers, flag, ip)
    print(ip)
    subprocess.call("ifconfig eth0 " + ip, shell=True)
    ip = ""
    time.sleep(4)