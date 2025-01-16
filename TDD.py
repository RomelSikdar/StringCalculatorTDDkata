import re

def add(numbers: str) -> int:
    # Return 0 if string is empty
    if not numbers:
        return 0
        
    # Checking for split character ','
    delimiter = ","
    if numbers.startswith("//"): 
        delimiter_part, numbers = numbers.split("\n", 1)
        delimiter = re.escape(delimiter_part[2:])
        
    # Checking for newlines 
    numbers = numbers.replace("\n", delimiter) 
    
    # Splitting the numbers by the delimiter 
    number_list = re.split(delimiter, numbers) 
    
    # Convert to integers and check for negatives 
    negatives = [int(n) for n in number_list if n.startswith("-")] 

    # Check for any negative numbers
    if negatives: 
        raise ValueError(f"negative numbers not allowed {', '.join(map(str, negatives))}")
    
    # Calculate the sum and return it
    return sum(int(n) for n in number_list if n)
