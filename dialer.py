#!/usr/local/bin/python3

from random import randint
from tqdm import tqdm
from sys import exit
import argparse
import pyttsx3
import time


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = argparse.ArgumentParser()
    # arguments
    parser.add_argument('-c', '--count', dest='count', help='Specify the number of times you want the dialer to call.')
    parser.add_argument('-t', '--target', dest='target', help='Specify the target number for the script to call.')

    (options) = parser.parse_args()

    return options


def create_number():
    temp = ''
    number = []
    count = 1
    # print('Generating number')
    while count <= 10:
        number.append(str(randint(0, 9)))
        count += 1

    final = temp.join(number)

    return str(final)


def progress_bar():
    # defaults to 30 seconds, change 3 to 10 for 5 minute wait
    for i in tqdm(range(10)):
        time.sleep(3)


message = 'Hello, you are being called by a Python script.'
total_calls = 1

options = get_arguments()
count = options.count     # number of times dialer will call
target = options.target   # the target number for the dialer to call

while True:
    if total_calls < int(count):
        try:
            # generate 'from' number
            test = create_number()
            call_from = f'({test[0:3]}) {test[3:6]}-{test[6:]}'
            print(f'Call from: {call_from}')
            time.sleep(5)

            print(f'Dialing: {target}')

            # play message
            engine = pyttsx3.init()
            engine.say(message)
            engine.runAndWait()

            # wait 5 minutes for next call
            print('Sleep')
            progress_bar()
            # sleep(5)  # change to 300 for 5 minutes
            print()
            total_calls += 1

        except KeyboardInterrupt:
            print('Quitting script.')
            print(f'Total calls made: {str(total_calls)}')
            exit()
    else:
        print(f'You have dialed {target} a total of {count} times.')
        exit()
