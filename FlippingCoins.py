#!/usr/bin/python


"""
FlippingCoins.py
"""


# Preferred way of working with the binomial distribution
from numpy.random import binomial
## Plotting stuff
from matplotlib.pyplot import hist, show


def flip_a_coin(fairness=0.5):
    """ Flips a coin and returns 1 for heads and 0 for tails"""
    return binomial(1, fairness)

def flip_some_coins(number_of_flips, fairness=0.5):
    """ Flips some coins and prints the numbers of heads and tails"""
    number_of_heads = sum([flip_a_coin(fairness) for _ in range(number_of_flips)])
    number_of_tails = number_of_flips - number_of_heads
    return 'number of heads:', number_of_heads, 'number of tails:', number_of_tails

def flip_some_coins_lots_of_times(number_of_times, number_of_flips=1000, fairness=0.5):
    """ Flips some coins lots of times"""
    return binomial(number_of_flips, fairness, number_of_times)

def flip_some_coins_lots_of_times_and_plot(number_of_times, number_of_flips=1000, fairness=0.5):
    """ Flips some coins lots of times and plot the histogram of the results"""
    results = flip_some_coins_lots_of_times(number_of_times, number_of_flips, fairness)
    hist(results, 1000); show()
    return results


if __name__ == '__main__':

    print 'Binary flip of a coin:', flip_a_coin()
    print 'Flipping a thousand coins'
    print flip_some_coins(1000)
    print 'Flipping a hundred thousand coins'
    print flip_some_coins(100000)
    print 'Plotting a thousand coins flipped a thousand times'
    flip_some_coins_lots_of_times_and_plot(1000)
    print 'Plotting a thousand coins flipped a hunddred thousand times'
    flip_some_coins_lots_of_times_and_plot(100000)

