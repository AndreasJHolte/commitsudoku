import math
import copy
import random
from create2 import *
from solvers import *
from interface import *


[absi,bas]=findunique()

babsi=backtrack(absi)

displaycompact(babsi)

print(checksolve(babsi))


