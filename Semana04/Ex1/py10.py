import os

print(dir(os))
print(os.getcwd())


os.chdir('/Users/coreyschafer/Desktop/')
os.mkdir('OS-Demo-2')
os.makedirs('OS-Demo-2')

print(os.listdir())


os.chdir('/Users/coreyschafer/Desktop/')
os.mkdir('OS-Demo-2/Sub-Dir-1')
os.makedirs('OS-Demo-2/Sub-Dir-1')

print(os.listdir())

os.chdir('/Users/coreyschafer/Desktop/')
os.rmdir('OS-Demo-2/Sub-Dir-1')
os.removedirs('OS-Demo-2/Sub-Dir-1')

print(os.listdir())

os.chdir('/Users/coreyschafer/Desktop/')
os.rename('test.txt, demo.txt')
print(os.listdir())

os.chdir('/Users/coreyschafer/Desktop/')
print(os.stat('demo.txt'))

os.chdir('/Users/coreyschafer/Desktop/')
print(os.stat('demo.txt').st_size)

os.chdir('/Users/coreyschafer/Desktop/')
print(os.stat('demo.txt').st_mtime)

import os
from datetime import datetime
os.chdir('/Users/coreyschafer/Desktop/')
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

import os
from datetime import datetime
os.chdir('/Users/coreyschafer/Desktop/')
for dirpath, dirnames, filenames in os.walk('/Users/coreyschafer/Desktop/'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

import os
from datetime import datetime
os.chdir('/Users/coreyschafer/Desktop/')
print(os.environ.get('HOME'))


file_path = os.environ.get('HOME') + 'test.txt'
print(file_path)

file_path = os.path.join(os.environ.get('HOME') + 'test.txt')
print(file_path)

with open(file_path, 'w') as f:
    f.wte

import os
from datetime import datetime
os.chdir('/Users/coreyschafer/Desktop/')
print(os.path.basename('/tmp/test.txt'))

print(os.path.dirname('/tmp/test.txt'))

print(os.path.split('/tmp/test.txt'))

print(os.path.exists('/tmp/test.txt'))

print(os.path.isdir('/tmp/fgdfgdf'))

print(os.path.isfile('/tmp/fgdfgdf'))

print(os.path.splitext('/tmp/test.txt'))

print(dir(os.path))
