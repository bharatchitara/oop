# from __main__ import sys
import sys
lst=[]
print(sys.getsizeof(lst))
print(len(lst))
lst.append(202.67)
lst.append(15)
print(len(lst))
print(sys.getsizeof(lst))