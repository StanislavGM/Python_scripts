# Script to use the sumof function.
import logging
from Python.script10 import sumof
logging.basicConfig(level=logging.INFO)
a = [5, 6, 8]
sumofa = sumof(a)
logging.info(sumofa)