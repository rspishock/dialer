#!/usr/local/bin/python3

from random import randint
from tqdm import tqdm
from sys import exit
import argparse
import pyttsx3
import time


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


message = 'Hello Senator.  For too long, you\'ve held a position of great importance in this country, living off of ' \
          'the tax payers dollar but failed to perform your duties.  It\'s time for you to do the job that you were ' \
          'elected for.'
total_calls = 1

while True:
    try:
        # generate 'from' number
        test = create_number()
        call_from = f'({test[0:3]}) {test[3:6]}-{test[6:]}'
        print(f'Call from: {call_from}')
        time.sleep(5)

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
