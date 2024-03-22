"""
Two ways to check for normality:
1. Visually checking with a histogram
2. Statistical Test of normality
"""

##### Histogram to Check for Normality
data['col'].hist()

##### Statistical Test for Normality (D'Agnostino K^2 Test)
"""This is a statistical test that tests whether a distribution is normally distributed or not. It isn't perfect, but suffice it to say: 
    * This test outputs a **p-value**. The _higher_ this p-value is the _closer_ the distribution is to normal."""

from scipy.stats.mstats import normaltest         # D'Agostino K^2 Test
normaltest(data['col'].values)
