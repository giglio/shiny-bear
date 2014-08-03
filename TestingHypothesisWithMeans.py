#!/usr/bin/python


"""
TestingHypothesisWithMeans.py
"""


from numpy import mean, std, sqrt
from scipy import stats

from FlippingCoins import flip_some_coins_lots_of_times


def example_test_a_mean(a_list_of_values, target=0.5, significance_level=0.95):
    sample_size = len(a_list_of_values)
    sample_standard_deviation = std(a_list_of_values)
    sample_mean = mean(a_list_of_values)

    standard_error = sample_standard_deviation/sqrt(sample_size)
    t_statistic = (sample_mean-target)/standard_error
    degrees_of_freedom = sample_size-1

    prob = stats.t.sf(t_statistic, degrees_of_freedom)
    alpha = 1 - significance_level
    if prob > alpha:
        return 'Mean is equal to target'
    else:
        return 'Mean is not equal to target'

def example_compare_two_means(list_of_values_1, list_of_values_2, significance_level=0.95):
    sample_size_1 = len(list_of_values_1)
    sample_standard_deviation_1 = std(list_of_values_1)
    sample_mean_1 = mean(list_of_values_1)
    s12 = sample_standard_deviation_1**2

    sample_size_2 = len(list_of_values_2)
    sample_standard_deviation_2 = std(list_of_values_2)
    sample_mean_2 = mean(list_of_values_2)
    s22 = sample_standard_deviation_2**2

    standard_error = sqrt((s12/sample_size_1)+(s22/sample_size_2))
    t_statistic = (sample_mean_1-sample_mean_2)/standard_error
    degrees_of_freedom = round(min(sample_size_1, sample_size_2)-1)
    prob = stats.t.sf(abs(t_statistic), degrees_of_freedom)*2

    alpha = 1 - significance_level
    if prob > alpha:
        return 'Means are equal'
    else:
        return 'Means are not equal'


if __name__ == '__main__':

    results = flip_some_coins_lots_of_times(number_of_times=100000,
                                        number_of_flips=1000,
                                        fairness=0.5)
    print 'Testing a single mean:', example_test_a_mean(
                                        results,
                                        target=500,
                                        significance_level=0.95)

    results_1 = flip_some_coins_lots_of_times(number_of_times=100000,
                                        number_of_flips=1000,
                                        fairness=0.5)
    results_2 = flip_some_coins_lots_of_times(number_of_times=100000,
                                        number_of_flips=1000,
                                        fairness=0.5)
    print 'Comparing two equal means:', example_compare_two_means(
                                        results_1,
                                        results_2)

    results_2 = flip_some_coins_lots_of_times(number_of_times=100000,
                                        number_of_flips=1000,
                                        fairness=0.3)
    print 'Comparing two unequal means:', example_compare_two_means(
                                        results_1,
                                        results_2)
