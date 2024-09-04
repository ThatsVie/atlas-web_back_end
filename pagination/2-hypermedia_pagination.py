#!/usr/bin/env python3
'''
This module contains a Server class to paginate a database of popular
baby names with hypermedia pagination.
'''

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Calculate the start and end index for pagination.
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    '''
    Server class to paginate the database.
    '''
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        '''
        Cached data set
        '''
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        Returns a page of data from the data set.
        '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        
        dataset = self.dataset()

        return dataset[start_index:end_index] if start_index < len(dataset) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''
        Returns a dictionary containing hypermedia pagination data.
        '''
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
