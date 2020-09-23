from random import randint
from time import sleep
from sys import exit


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


while True:
    try:
        test = create_number()
        # print(test)
        final_number = (f'({test[0:3]}) {test[3:6]}-{test[6:]}')
        print(f'Number: {final_number}')

        print('Sleep')
        sleep(5)
        print()
    except KeyboardInterrupt:
        print('Quitting script.')
        exit()
