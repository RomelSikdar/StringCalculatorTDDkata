from TDD import add
import pytest

# This is test for empty string
def test_add_empty_string(): 
    assert add("") == 0

test_add_empty_string()
