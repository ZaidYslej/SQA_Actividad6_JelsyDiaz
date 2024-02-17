# tests/test_search.py
import pytest
from src.search import search

def test_search_success():
    query = "zapatillas deportivas"
    results = search(query)
    assert len(results) > 0  
    for product in results:
        assert query.lower() in product["category"].lower()

def test_search_no_results():
    query = "producto no existente"
    results = search(query)
    assert len(results) == 0  
