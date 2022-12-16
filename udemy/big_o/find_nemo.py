import time

a = ['nemo'] * 10000


def find_nemo(array):
    time1 = time.time()
    for i in array:
        if i == 'nemo':
            print('we found nemo')
    time2 = time.time()
    return time2 - time1


print(find_nemo(a))
