#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'countAnalogousArrays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY consecutiveDifference
#  2. INTEGER lowerBound
#  3. INTEGER upperBound
#

def countAnalogousArrays(consecutiveDifference, lowerBound, upperBound):
    if len(consecutiveDifference) == 0:
        return 0
    if upperBound < lowerBound:
        return 0
    
    Max = float('-inf')
    Min = float('inf')
    runningSum = 0
    for diff in consecutiveDifference:
        runningSum +=diff
        if runningSum > Max:
            Max = runningSum
        if runningSum < Min:
            Min = runningSum
            
    if upperBound+Min < upperBound:
        validUpper = upperBound + Min
    else:
        validUpper = upperBound
        
    if lowerBound+Max > lowerBound:
        validLower = lowerBound + Max
    else:
        validLower = lowerBound
        
    if validUpper >= validLower:
        return validUpper - validLower + 1
    else:
        return 0

if __name__ == '__main__':
