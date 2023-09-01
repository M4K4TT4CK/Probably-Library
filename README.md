Welcome to the isItLikely Library!

Here you will find basic functions for probablity. I plan on packaging this and adding to PyPi. This will be updated as time goes on. 

This library is published on Pypi - pip install isItLikely==0.1.0


The functions provided are below:

A. probability:

    Calculates the probability of an event.

    Parameters:
    event_occurrences (int): The number of favorable outcomes.
    total_outcomes (int): The total number of possible outcomes.

    Returns:
    float: The probability of the event occurring.

B. complementary_probability:

    Calculates the complementary probability (probability of "not" an event).

    Parameters:
    event_occurrences (int): The number of unfavorable outcomes.
    total_outcomes (int): The total number of possible outcomes.

    Returns:
    float: The probability of the event not occurring.

C. joint_probability:
    Calculates the joint probability of two or more independent events occurring.

    Parameters:
    probability_event1, probability_event2, *args (float): Probabilities of individual events.

    Returns:
    float: The joint probability of all events occurring.


D. conditional_probability:

    Calculates the conditional probability of an event given a condition.

    Parameters:
    probability_event_given_condition (float): Probability of the event given the condition.
    probability_condition (float): Probability of the condition.

    Returns:
    float: The conditional probability of the event given the condition.


E. addition_rule_disjoint:

    Calculates the probability of the union of two or more disjoint events.

    Parameters:
    probability_event1, probability_event2, *args (float): Probabilities of individual events.

    Returns:
    float: The probability of the union of all disjoint events.


F. addition_rule_non_disjoint:

    Calculates the probability of the union of two or more non-disjoint events using the inclusion-exclusion principle.

    Parameters:
    probability_event1, probability_event2, *args (float): Probabilities of individual events.
    probability_intersection (float): Probability of the intersection of all events.

    Returns:
    float: The probability of the union of all non-disjoint events.

