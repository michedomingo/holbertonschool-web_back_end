#!/usr/bin/env python3
"""
Defines index_range function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns tuple with start and end indexes
    """
    return (page * page_size - page_size, page * page_size)
