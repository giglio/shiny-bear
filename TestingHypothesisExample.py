#!/usr/bin/python


"""
TestingHypothesisExample.py
"""


from scipy import stats

from FlippingCoins import flip_a_coin


def example_test_coin_fairness(number_of_flips, fairness=0.5, significance_level=0.95):
    results = [flip_a_coin(fairness) for flip in range(number_of_flips)]

    t_statistic, prob = stats.ttest_1samp(results, 0.5)
    alpha = 1 - significance_level
    if prob > alpha:
        return 'The coin is fair'
    else:
        return 'The coin is unfair'

def example_compare_two_coins(number_of_flips, fairness_1=0.5, fairness_2=0.5, significance_level=0.95):
    results_1, results_2 = [], []
    for _ in range(number_of_flips):
        results_1.append(flip_a_coin(fairness_1))
        results_2.append(flip_a_coin(fairness_2))

    t_statistic, prob = stats.ttest_ind(results_1, results_2, equal_var=True)
    alpha = 1 - significance_level
    if prob > alpha:
        return 'Coins are equal'
    else:
        return 'Coins are not equal'

def main():
    """ TestingHypothesisExample.py """

    print 'Testing the fairness of a fair coin:', example_test_coin_fairness(
                                                    number_of_flips=1000,
                                                    fairness=0.5)
    print 'Testing the fairness of an unfair coin:', example_test_coin_fairness(
                                                    number_of_flips=1000,
                                                    fairness=0.3)
    print 'Comparing equal coins:', example_compare_two_coins(
                                                    number_of_flips=1000,
                                                    fairness_1=0.5,
                                                    fairness_2=0.5)
    print 'Comparing unequal coins:', example_compare_two_coins(
                                                    number_of_flips=1000,
                                                    fairness_1=0.5,
                                                    fairness_2=0.3)


if __name__ == '__main__':

    main()

