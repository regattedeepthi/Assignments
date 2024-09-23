# math built in module
import math
print(dir(math))
print(math.pow(3,4)) #power of 3 to 4

print(math.sqrt(9))

#statistics built in module
import statistics
#mean module 
print(statistics.mean([1,2,3,4]))
#median modul---- return middle numeruc value of given list
print(statistics.median([1,2,3,4,4]))
#mode ---- gives most common repeated
print(statistics.mode([1,7,9,3,3,6,2,3]))

#sys built in module
import sys
print(sys.version)
print(sys.path)
print(sys.maxsize)

#os built in module
import os
print(os.getcwd) # gives name of current working dirsectory