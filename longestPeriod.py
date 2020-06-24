from itertools import groupby
import Cov

def longestPeriod(coverages):
    # Creat list representing a year set all dates to None
    # 366 days because Jan/1 would not be entered as Jan/0
    year =  [None] * 366

    for term in coverages:
        start = term.eff
        end = term.term    
        #Set all dates for when there was coverage to 1
        year[start:end] = [1] *(end - start)

    #Find the longest streak in coverages.
    return max(sum(1 for x in v if x == 1) for k,v in groupby(year))
