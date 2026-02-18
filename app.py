#!/usr/bin/env python3
'''
Reserves N memory chunks of 10MB each. Waiting 2 seconds in between each reserve.
'''

import time
import sys

def main(number_chunks, chunk_size, sleep_time):
    '''
    Main function, number_chunks is the number 10MB chunks to reserve
    '''
    array = []
    for i in range(0,number_chunks):
        array.append(bytearray(chunk_size*1000000)) # add 10MB to array
        print(f"{(i+1)*chunk_size}MB", flush=True)
        time.sleep(sleep_time)

    print("Sleeping...")
    # Infinite loop, to keep it alive
    while True:
        time.sleep(5)

if __name__ == "__main__":
    try:
        NUMBER=int(sys.argv[1])
    except IndexError as ierr:
        NUMBER=210

    try:
        CHUNK_SIZE=int(sys.argv[2])
    except IndexError as ierr:
        CHUNK_SIZE=10

    try:
        SLEEP_TIME=int(sys.argv[3])
    except IndexError as ierr:
        SLEEP_TIME=2

    main(number_chunks=NUMBER,chunk_size=CHUNK_SIZE,sleep_time=SLEEP_TIME)
