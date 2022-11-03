#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from scipy import stats
def compare_stats( rn1, rn2 ):
    stats1 = stats.describe( rn1 )
    stats2 = stats.describe( rn2 )
    print( "{:14s} {:14s} {:14s}".format( 'statistic', 'data set 1', 'data set 2' )  )
    print( 45 * "-" )
    print( "{:14s} {:14.3f} {:14.3f}".format( 'size', stats1[0], stats2[0] ) )
    print( "{:14s} {:14.3f} {:14.3f}".format( 'min', stats1[1][0], stats2[1][0] ) )
    print( "{:14s} {:14.3f} {:14.3f}".format( 'max', stats1[1][1], stats2[1][1] ) )
    print( "{:14s} {:14.3f} {:14.3f}".format( 'mean', stats1[2], stats2[2] ) )
    print( "{:14s} {:14.3f} {:14.3f}".format( 'std', stats1[3], stats2[3] ) )
    print( "{:14s} {:14.3f} {:14.3f}".format( 'skew', stats1[4], stats2[4] ) )
    print( "{:14s} {:14.3f} {:14.3f}".format( 'kurtosis', stats1[5], stats2[5] ) )

