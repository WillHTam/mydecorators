from mydecorators import *

@trace
@pvm
def cat(m):
    return len(m)

print(cat('hellou'))
