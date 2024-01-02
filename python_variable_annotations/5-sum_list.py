#!/usr/bin/en python3
"""module that type-annotated function sum_list
which takes a list input_list of floats as argument
and returns their sum as a float."""


def sum_list(imput_list: List[float]) -> float:
    """takes a list input_list of floats as argument
    and returns their sum as a float.
    """
    return sum(imput_list)
