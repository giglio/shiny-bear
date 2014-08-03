#!/usr/bin/python


"""
TestingHypothesisWithProportions.py
"""


from scipy import stats


def example_test_a_proportion(p=0.1, n=100, target=0.1, significance_level=0.95):
    sigma = (p*(1-p)/n)**0.5
    z_score = (p-target)/sigma
    prob = stats.zprob(z_score)

    alpha = 1 - significance_level
    if prob > alpha:
        return 'Proportion is equal to target'
    else:
        return 'Proportion is not equal to target'

def example_compare_two_proportions(p1=0.1, n1=100, p2=0.1, n2=100, significance_level=0.95):
    p = ((p1*n1)+(p2*n2))/(n1+n2)
    standard_error = (p*(1.-p)*((1./n1)+(1./n2))**0.5)
    z_score = (p1-p2)/standard_error
    prob = stats.zprob(z_score)

    alpha = 1 - significance_level
    if prob > alpha:
        return 'Proportions are equal'
    else:
        return 'Proportions are not equal'


if __name__ == '__main__':

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

