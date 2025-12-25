import pytest

from task.queries import *
from .conftest import data


def test_query_one_to_many(data):
    browsers, computers, _ = data
    result = query_one_to_many(browsers, computers)

    assert result == [
        ("Chrome", 120, "PC1"),
        ("Firefox", 118, "PC1"),
        ("Браузеров", 5, "PC2"),
    ]


def test_query_computers_with_browser_count(data):
    browsers, computers, _ = data
    one_to_many = query_one_to_many(browsers, computers)

    result = query_computers_with_browser_count(one_to_many)

    assert result == [
        ("PC2", 1),
        ("PC1", 2),
    ]


def test_query_many_to_many(data):
    browsers, computers, relations = data

    result = query_many_to_many(browsers, computers, relations)

    assert result == [
        ("Браузеров", "PC2"),
    ]
