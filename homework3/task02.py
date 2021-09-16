"""
Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
Calculation time should not take more than a minute. Use functional
capabilities of multiprocessing module. You are not allowed to modify
slow_calculate function.
"""
import hashlib
import random
import struct
import os
import time
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def runner():
    with Pool(100) as p:
        print(sum(p.map(slow_calculate, [i for i in range(501)])))


if __name__ == '__main__':
    start_time = time.time()
    runner()
    proc_time = time.time() - start_time
    print(proc_time)


#  'Amount of processes is 10, get 106.01 seconds to done',
#  'Amount of processes is 40, get 34.60 seconds to done',
#  'Amount of processes is 80, get 20.35 seconds to done',
#  'Amount of processes is 100, get 19.36 seconds to done',
#  'Amount of processes is 125, get 20.01 seconds to done'
#  'Amount of processes is 150, get 20.79 seconds to done',
#  'Amount of processes is 250, get 24.62 seconds to done'
