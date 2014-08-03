#!/usr/bin/python


"""
NonParametricMethods.py
"""


from random import random
from numpy import mean
from scipy import stats
from matplotlib.pyplot import hist, show

from FlippingCoins import flip_some_coins_lots_of_times, \
                          flip_some_coins_lots_of_times_and_plot
from ConfidenceIntervals import get_confidence_intervals_using_the_normal_distribution, \
                                get_confidence_intervals_using_the_quantiles
from TestingHypothesisWithMeans import example_compare_two_means


def create_random_non_normal_data(sample_size=1000, a=11.3, c=0.4, plot=False):
    data = stats.gengamma.rvs(a, c, size=sample_size)
    if plot: hist(data, 100); show()
    return data

def test_for_normality(a_list_of_values, significance_level=0.95):
    chi2_statistic, prob = stats.normaltest(a_list_of_values)
    alpha = 1 - significance_level
    if prob > alpha:
        return 'Data is normal'
    else:
        return 'Data is not normal'

def bootstrap_confidence_intervals(a_list_of_values):

    def sample_wr(population, k):
        "Chooses k random elements (with replacement) from a population"
        n = len(population)
        _random, _int = random, int
        result = [None] * k
        for i in xrange(k):
            j = _int(_random() * n)
            result[i] = population[j]
        return result

    n = len(a_list_of_values)
    data = sample_wr(a_list_of_values, n)
    lower_bound, upper_bound = get_confidence_intervals_using_the_quantiles(data)
    return lower_bound, upper_bound


def non_parametric_test_for_difference_of_means(list_of_values_1, list_of_values_2, significance_level=0.95):
    z_statistic, prob = stats.mannwhitneyu(list_of_values_1, list_of_values_2)
    alpha = 1 - significance_level
    if prob > alpha:
        return 'The means are equal'
    else:
        return 'The means are not equal'


if __name__ == '__main__':

    normal_data = flip_some_coins_lots_of_times_and_plot(10000, number_of_flips=1000, fairness=0.5)
    normal_mean = mean(normal_data)
    normal_lower_bound, normal_upper_bound = get_confidence_intervals_using_the_normal_distribution(normal_data)
    print 'normal: len', len(normal_data), 'mean', mean(normal_data)
    print 'Normality test for normal data:', test_for_normality(normal_data)
    print 'Confidence intervals for normal data:', normal_lower_bound, normal_upper_bound
    normal_lower_bound, normal_upper_bound = bootstrap_confidence_intervals(normal_data)
    print 'Bootstrapping confidence intervals for normal data:', normal_lower_bound, normal_upper_bound
    print

    powerlaw_data = create_random_non_normal_data(sample_size=10000, plot=True)
    print 'powerlaw: len', len(powerlaw_data), 'mean', mean(powerlaw_data)
    powerlaw_mean = mean(powerlaw_data)
    powerlaw_lower_bound, powerlaw_upper_bound = get_confidence_intervals_using_the_normal_distribution(powerlaw_data)
    print 'Normality test for powerlaw data:', test_for_normality(powerlaw_data)
    print 'Confidence intervals for powerlaw data:', powerlaw_lower_bound, powerlaw_upper_bound
    powerlaw_lower_bound, powerlaw_upper_bound = bootstrap_confidence_intervals(powerlaw_data)
    print 'Bootstrapping confidence intervals for powerlaw data:', powerlaw_lower_bound, powerlaw_upper_bound

    data_1 = flip_some_coins_lots_of_times(10000, number_of_flips=1000, fairness=0.5)
    data_2 = flip_some_coins_lots_of_times(10000, number_of_flips=1000, fairness=0.5)
    print 'Normality based test to compare two equal normal means:', example_compare_two_means(data_2, data_1)
    print 'Ranksum test to compare two equal normal means:', non_parametric_test_for_difference_of_means(data_2, data_1)
    print
    data_1 = flip_some_coins_lots_of_times(10000, number_of_flips=1000, fairness=0.5)
    data_2 = flip_some_coins_lots_of_times(10000, number_of_flips=1000, fairness=0.45)
    print 'Normality based test to compare two unequal normal means:', example_compare_two_means(data_2, data_1)
    print 'Ranksum test to compare two unequal normal means:', non_parametric_test_for_difference_of_means(data_2, data_1)
    print
    data_1 = create_random_non_normal_data(sample_size=10000)
    data_2 = create_random_non_normal_data(sample_size=10000)
    print 'Normality based test to compare two equal non-normal means:', example_compare_two_means(data_2, data_1)
    print 'Ranksum test to compare two equal non-normal means:', non_parametric_test_for_difference_of_means(data_2, data_1)

