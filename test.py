from TDD import add
import pytest

# This is test for empty string
def test_add_empty_string(): 
    assert add("") == 0

# This is test string "1"
def test_add_single_number(): 
    assert add("1") == 1 

# This is test string "1,2" 1 + 2 = 3
def test_add_two_numbers(): 
    assert add("1,2") == 3 

# This is test string "1,2,3,4" 1 + 2 + 3 + 4 = 10
def test_add_multiple_numbers(): 
    assert add("1,2,3,4") == 10 

# This is test string "1\n2,3" 1 + 2 + 3 = 6
def test_add_with_newlines(): 
    assert add("1\n2,3") == 6 

# This is test string "//;\n1;2" 1 + 2 = 3
def test_add_with_custom_delimiter(): 
    assert add("//;\n1;2") == 3 
    assert add("//|\n1|2|3") == 6 

# This is test string if is negative number and throws error if negative is present.
def test_add_negative_numbers(): 
    with pytest.raises(ValueError, match="negative numbers not allowed -1"): 
        add("-1,2,3") 
    with pytest.raises(ValueError, match="negative numbers not allowed -1, -2"): 
        add("-1,-2,3") 

# This is test string if is number is empty and ignores it.     
def test_add_ignore_empty_numbers(): 
    assert add("1,,2") == 3

test_add_empty_string()
test_add_single_number()
test_add_two_numbers()
test_add_multiple_numbers()
test_add_with_newlines()
test_add_with_custom_delimiter()
test_add_negative_numbers()
test_add_ignore_empty_numbers()
