#!/usr/bin/env python3
"""Paganing Database"""
import csv
import math
from typing import List

index_range = __import__("0-simple_pagination.py").index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """that takes two integer arguments page with default value 1
        and page_size with default value 10.
        - assert to verify that both arguments are integers great than 0
        - index_range to find the correct indexes to paginate
        the dataset correctly and return the appropriate page
        of the dataset (i.e. the correct list of rows)."""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        index_page: tuple = index_range(page, page_size)
        dataset: List = self.dataset()

        current_page = dataset[index_page[0]: index_page[1]]
        return current_page
