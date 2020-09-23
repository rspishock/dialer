from random import randint
from time import sleep
from sys import exit
import argparse
import pyttsx3


def create_number():
    temp = ''
    number = []
    count = 1
    print('Generating number')
    while count <= 10:
        number.append(str(randint(0,9)))
        count+=1

    final = temp.join(number)

    return str(final)


message = 'Hello Senator, it\'s time for you to do the job that you were elected for.'

while True:
    try:
        # generate 'from' number
        test = create_number()
        final_number = (f'({test[0:3]}) {test[3:6]}-{test[6:]}')
        print(f'Number: {final_number}')
        sleep(5)

        # play message
        engine = pyttsx3.init()
        engine.say(message)
        engine.runAndWait()

        # wait 5 minutes for next call
        print('Sleep')
        sleep(5)  # change to 300 for 5 minutes
        print()
    except KeyboardInterrupt:
        print('Quitting script.')
        exit()


