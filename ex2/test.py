from adaptable_heap_priority_queue import *
import time
import re
from job import *
import sys


q = AdaptableHeapPriorityQueue()

q.add(1,'ciao')

print(q.Locator(1,'ciao',0))
