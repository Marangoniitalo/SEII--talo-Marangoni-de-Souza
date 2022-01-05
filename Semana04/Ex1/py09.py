print('Imported my_module...')

test = 'Test String'

def find_index(to_search, terget):

    for i, value in enumerate(to_search):
        if value == target:
            return i
    
    return -1


import my_module

courses = ['History', 'Math', 'Physics', 'CompSci']

index = my_module.find_index(courses, 'Math')
print(index)

import my_module as mm

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')
print(index)

from my_module import find_index

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)

from my_module import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test)

from my_module import find_index as fi, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = fi(courses, 'Math')
print(index)
print(test)

from my_module import find_index, test
import sys

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
#print(index)
#print(test)

print(sys.path)

import sys
sys.path.append('/Users/coreyschafer/Desktop/My-Modules')
from my_module import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
#print(index)
#print(test)

print(sys.path)

import random
courses = ['History', 'Math', 'Physics', 'CompSci']
random_course = random.choice(courses)
print(random_course)

import math
courses = ['History', 'Math', 'Physics', 'CompSci']
rads = math.radians(90)
print(rads)
print(math.sin(rads))

import datetime
import calendar
courses = ['History', 'Math', 'Physics', 'CompSci']
today =  datetime.date.today()
print(today)
print(calendar.isleap(2020))

import os
courses = ['History', 'Math', 'Physics', 'CompSci']
print(os.getcwd())
print(os.__file__)

import webbrowser
import hashlib
webbrowser.open("https://xkcd.com/353/")
def geohash(latitude, longitude, datedow):
    h=hashlib.md5(datedow).hexdigest()
    p, q =[('%f' % float.fromhex('0.' + x)) for x in (h[:16], h[16:32])]
    print('%d%s %d%s' % (latitude, p[1:], longitude, q[1:]))

import antigravity