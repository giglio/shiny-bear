#!/usr/bin/python


"""
BayesianStatistics.py
"""


from scipy import stats
from matplotlib.pyplot import hist,  show

from ConfidenceIntervals import get_confidence_intervals_using_the_quantiles


def create_random_sample_from_beta(success, total, sample_size=1000, plot=False):
    failures = total - success
    data = stats.beta.rvs(success, failures, size=10000)
    if plot: hist(data, 100), show()
    return data

def compare_two_samples_from_beta(sample_1, sample_2, significance_level=0.95, plot=True):
    if plot: hist(sample_1, 100, alpha=0.5); hist(sample_2, 100, alpha=0.5); show()
    sample_1_lower_bound, sample_1_upper_bound = get_confidence_intervals_using_the_quantiles(sample_1, significance_level)
    sample_2_lower_bound, sample_2_upper_bound = get_confidence_intervals_using_the_quantiles(sample_2, significance_level)
    if sample_1_lower_bound > sample_2_upper_bound or sample_2_lower_bound > sample_1_upper_bound:
        return 'Samples are not equal'
    else:
        return 'Samples are equal'


if __name__ == '__main__':

    data = create_random_sample_from_beta(10, 100, plot=True)
    print 'CI:', get_confidence_intervals_using_the_quantiles(data)

    sample_1 = create_random_sample_from_beta(100, 10000)
    sample_2 = create_random_sample_from_beta(100, 10000)
    print 'Comparing equal samples:', compare_two_samples_from_beta(sample_1, sample_2)
    sample_1 = create_random_sample_from_beta(150, 10000)
    sample_2 = create_random_sample_from_beta(100, 10000)
    print 'Comparing unequal samples:', compare_two_samples_from_beta(sample_1, sample_2)

