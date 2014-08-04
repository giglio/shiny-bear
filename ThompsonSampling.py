#!/usr/bin/python


"""
ThompsonSampling.py
"""


from random import random
from scipy import stats
from matplotlib.pyplot import plot, legend, show


def simulate_bandit(number_of_requests=1000):
    """ """
    alternatives = {
        'A': {
            'success': 1,
            'failure': 2,
            'simulated_conversion': 0.05,
            'requests_so_far': 0.
        },
        'B': {
            'success': 1,
            'failure': 2,
            'simulated_conversion': 0.10,
            'requests_so_far': 0.
        },
        'C': {
            'success': 1,
            'failure': 2,
            'simulated_conversion': 0.15,
            'requests_so_far': 0.
        }
    }

    proportions_in_time = []
    for request_number in range(1, number_of_requests):

        chosen_alternative, chosen_alternative_temporary_value = 'A', 0
        for alternative in alternatives:
            success = alternatives[alternative]['success']
            failure = alternatives[alternative]['failure']
            temporary_values_from_beta = stats.beta.rvs(success, failure)
            if temporary_values_from_beta > chosen_alternative_temporary_value:
                chosen_alternative = alternative
                chosen_alternative_temporary_value = temporary_values_from_beta

        alternatives[chosen_alternative]['requests_so_far'] += 1
        if random() < alternatives[chosen_alternative]['simulated_conversion']:
            alternatives[chosen_alternative]['success'] += 1
        else:
            alternatives[chosen_alternative]['failure'] += 1

        proportions_in_time.append([alternatives[alternative]['requests_so_far']/request_number
                                    for alternative in alternatives])

    plot(proportions_in_time); legend(alternatives.keys()); show()

def main():
    """ ThompsonSampling.py """
    simulate_bandit(number_of_requests=10000)


if __name__ == '__main__':

    main()    

