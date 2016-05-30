#/usr/bin/python

from operator import add


liste =[1,2,3,4,5,6,7,8,9]
res = reduce(add, liste[:6])
print(res)





