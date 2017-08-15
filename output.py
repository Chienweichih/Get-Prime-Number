import os
import sys
import binascii

min = 0
max = 0

if len(sys.argv) == 2:
    max = int(sys.argv[1])
elif len(sys.argv) > 2:
    min = int(sys.argv[1])
    max = int(sys.argv[2])

prime = 2
dir   = os.path.dirname(os.path.abspath(__file__))
with open(dir + '/primes.32b', 'rb') as f:
    while prime < max:
        if prime > min:
            print(prime, end="|")
        prime = int(binascii.hexlify(f.read(4)[::-1]), 16)