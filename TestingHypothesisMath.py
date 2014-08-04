#!/usr/bin/python


"""
TestingHypothesisMath.py
"""


from numpy import mean, std, sqrt
from scipy import stats

from FlippingCoins import flip_some_coins_lots_of_times


def example_test_a_mean(a_list_of_values, target=0.5, significance_level=0.95):
    """ The math behind 'example_test_coin_fairness' """
    sample_size = len(a_list_of_values)
    sample_standard_deviation = std(a_list_of_values)
    sample_mean = mean(a_list_of_values)

    standard_error = sample_standard_deviation/sqrt(sample_size)
    t_statistic = (sample_mean-target)/standard_error
    degrees_of_freedom = sample_size-1
    prob = stats.t.sf(t_statistic, degrees_of_freedom)

    # If we observe a large p-value, for example larger than 0.05 or 0.1,
    # then we cannot reject the null hypothesis of identical averages
    alpha = 1 - significance_level
    if prob > alpha:
        return 'Mean is equal to target'
    else:
        return 'Mean is not equal to target'

def example_compare_two_means(list_of_values_1, list_of_values_2, significance_level=0.95):
    """ The math behind 'example_compare_two_coins' """
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

    # If we observe a large p-value, for example larger than 0.05 or 0.1,
    # then we cannot reject the null hypothesis of identical averages
    alpha = 1 - significance_level
    if prob > alpha:
        return 'Means are equal'
    else:
        return 'Means are not equal'

def example_test_a_proportion(p=0.1, n=100, target=0.1, significance_level=0.95):
    """ The math """
    sigma = sqrt(p*(1-p)/n)

    z_score = (p-target)/sigma
    prob = stats.zprob(z_score)

    # If we observe a large p-value, for example larger than 0.05 or 0.1,
    # then we cannot reject the null hypothesis of identical averages
    alpha = 1 - significance_level
    if prob > alpha:
        return 'Proportion is equal to target'
    else:
        return 'Proportion is not equal to target'

def example_compare_two_proportions(p1=0.1, n1=100, p2=0.1, n2=100, significance_level=0.95):
    """  """
    p = ((p1*n1)+(p2*n2))/(n1+n2)
    standard_error = sqrt(p*(1.-p)*((1./n1)+(1./n2)))

    z_score = (p1-p2)/standard_error
    prob = stats.zprob(z_score)

    # If we observe a large p-value, for example larger than 0.05 or 0.1,
    # then we cannot reject the null hypothesis of identical averages
    alpha = 1 - significance_level
    if prob > alpha:
        return 'Proportions are equal'
    else:
        return 'Proportions are not equal'

def main():
    """ TestingHypothesisMath.py """
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

    print 'Testing a single proportion:', example_test_a_proportion(p=0.1,
                                                                    n=100,
                                                                    target=0.1)

    print 'Comparing two equal proportions:', example_compare_two_proportions(p1=0.1,
                                                                              n1=1000,
                                                                              p2=0.1,
                                                                              n2=1000)

    print 'Comparing two unequal proportions:', example_compare_two_proportions(p1=0.1,
                                                                                n1=1000,
                                                                                p2=0.15,
                                                                                n2=1000)


if __name__ == '__main__':

    main()

