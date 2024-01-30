#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Union[int, None] = None,
                        page_size: int = 10) -> Dict:
        """
        Return a dictionary with pagination information based on index
        and page_size.
        """
        dataset = self.indexed_dataset()

        # assert isinstance(index, int) and index >= 0
        # assert isinstance(page_size, int) and page_size > 0
        # assert index <= len(dataset)  # check if index is out of range
        assert index is not None and index >= 0 and index <= max(
            dataset.keys())

        start = index if index else 0
        indexed_data = []
        count = 0
        next_index = None

        for idx, item in dataset.items():
            if idx >= start and count < page_size:
                count += 1
                indexed_data.append(item)
                continue
            if count == page_size:
                next_index = idx
                break

        return {"index": index, "data": indexed_data,
                "page_size": len(indexed_data), "next_index": next_index}
