import os
from os import listdir
import os.path # Paquetes
from os.path import getsize as my_getsize


files = os.listdir()
print(files)

size = os.path.getsize('scope.py')
print(size)

size = my_getsize("scope.py")

help(os)

