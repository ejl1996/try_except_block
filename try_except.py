"""
Emma Lee
A01246983
"""
import sys
from itertools import combinations
import doctest


def create_unordered_tuples(lines: list) -> tuple:
    """
    Create unordered tuples of length 2 comprised of letters from a file.

    A function that creates unordered tuples of length 2 comprised of letters from a file.

    :param lines: output of reading file
    :precondition: first line of the plain text file must contain an integer N denoting the list of letters' length
    :precondition: second line of the plain text file must consist of N space-separated, alphabetically sorted, lowercase Latin letters
    :precondition: third line of the file must contain the size of subset to be selected, an integer K
    :precondition: 1<=N<=10 and 1<=K<=N
    :postcondition: return unordered tuples of length 2 comprised of letters from a file
    :return: unordered tuples of length 2 comprised of letters from a file
    :raises FileNotFoundError: if file does not exist
    :raises ValueError: if list of letter's length is less than 1
    :raises ValueError: if list of letter's length is greater than 10
    :raises ValueError: if number of indices to be selected is less than 1
    :raises ValueError: if number of indices to be selected is greater than the length of list of letters
    >>> test_input_some_a = ['4\\n', 'a a c d\\n', '2\\n']
    >>> create_unordered_tuples(test_input_some_a)
    (('a', 'a'), ('a', 'c'), ('a', 'd'), ('a', 'c'), ('a', 'd'), ('c', 'd'))
    >>> test_input_all_a = ['4\\n', 'a a a a\\n', '2\\n']
    >>> create_unordered_tuples(test_input_all_a)
    (('a', 'a'), ('a', 'a'), ('a', 'a'), ('a', 'a'), ('a', 'a'), ('a', 'a'))
    >>> test_input_no_a = ['4\\n', 'b c d e\\n', '2\\n']
    >>> create_unordered_tuples(test_input_no_a)
    (('b', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'd'), ('c', 'e'), ('d', 'e'))
    """
    number_of_elements = int(lines[0].replace('\n', ''))
    number_of_indices = int(lines[2].replace('\n', ''))

    if number_of_elements < 1 or number_of_elements > 10:
        raise ValueError("List of letters' length should be between 1 to 10")
    if number_of_indices < 1 or number_of_indices > number_of_elements:
        raise ValueError("Number of indices to be selected should be between 1 and N")

    latin_letters_list = lines[1].replace('\n', '').split()
    tuple_result = tuple(combinations(latin_letters_list, number_of_indices))
    return tuple_result


def probability_of_letter_in_file(tuple_result: tuple) -> None:
    """
    Determine the probability of a group of letters containing a specific letter.

    :param tuple_result: a string of filename
    :precondition: first line of the plain text file must contain an integer N denoting the list of letters' length
    :precondition: second line of the plain text file must consist of N space-separated, alphabetically sorted, lowercase Latin letters
    :precondition: third line of the file must contain the size of subset to be selected, an integer K
    :precondition: 1<=N<=10 and 1<=K<=N
    :postcondition: probability of the subset containing a specific letter is printed
    :postcondition: probability is rounded to 4 decimal places
    >>> test_input_some_a = ['4\\n', 'a a c d\\n', '2\\n']
    >>> tuple_result_some_a = create_unordered_tuples(test_input_some_a)
    >>> probability_of_letter_in_file(tuple_result_some_a)
    0.8333 probability that a group of 2 items selected from 4 will contain one or more 'a'
    >>> test_input_all_a = ['4\\n', 'a a a a\\n', '2\\n']
    >>> tuple_result_all_a = create_unordered_tuples(test_input_all_a)
    >>> probability_of_letter_in_file(tuple_result_all_a)
    1.0 probability that a group of 2 items selected from 4 will contain one or more 'a'
    >>> test_input_no_a = ['4\\n', 'b c d e\\n', '2\\n']
    >>> tuple_result_no_a = create_unordered_tuples(test_input_no_a)
    >>> probability_of_letter_in_file(tuple_result_no_a)
    0.0 probability that a group of 2 items selected from 4 will contain one or more 'a'
    """
    occurrence = 0
    for sub_tuple in tuple_result:
        if 'a' in sub_tuple:
            occurrence += 1
    probability = occurrence / len(tuple_result)
    print(round(probability, 4), "probability that a group of 2 items selected from 4 will contain one or more 'a'")


def main():
    """
    Drive the program
    """
    doctest.testmod(verbose=True)
    try:
        with open(sys.argv[1]) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError as e:
        print(e)
    else:
        print("Thank you for entering a valid file")

    tuple_result = create_unordered_tuples(lines)
    probability_of_letter_in_file(tuple_result)

if __name__ == "__main__":
    main()
