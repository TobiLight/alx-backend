#!/usr/bin/env python3
"""Helper function module"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two containing a start index
    and an end index
    """
    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)
