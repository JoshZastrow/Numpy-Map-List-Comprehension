# Numpy-Map-List-Comprehension
basic use of Numpy, Map function and List Comprehension

import numpy

#map the row and column info to variables n and m
n,m = map(int, input().split())

#map the column values to a list, create list for n rows
arr = [list(map(int, input().split())) for x in range(n)]

#Use numpy to do basic calculations
result = numpy.prod(numpy.sum(arr, axis = 0))

print(result)
