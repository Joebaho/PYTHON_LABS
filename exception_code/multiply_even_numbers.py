'''
PYTHON LAB: receipt_sales.py

Write a code using function that will accepts a list of numbers and returns the product of all even numbers 
in the list. Numbers =[8, 9, 11,  20, 32, 101, 100]

Please have exceptions handled and Docstring for this code to make code look great! 
'''
def multiply_even_numbers(numbers):
    """
    This function takes a list of numbers as input and returns the product of all even numbers in the list.
    If there are no even numbers in the list, it returns 1.

    Args:
        numbers (list): A list of numbers.

    Returns:
        multiply_even_numbers (float): The product of all even numbers in the list.
    """
    even_product = 1
    even_numbers=[]
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
            even_product *= num
    print(f"The new even numbers list is {even_numbers}")         
    return even_product
       
# Example usage
numbers = [8, 9, 11, 20, 32, 101, 100]
result = multiply_even_numbers(numbers)
print(f"The product of even numbers in the list {numbers} is: {result}")

#################################################################################################
def product_of_even_numbers(numbers):
    """
    Calculates the product of all even numbers in a given list of numbers.
    
    Parameters:
    numbers (list): A list of numbers.
    
    Returns:
    int: The product of all even numbers in the list. If the list contains no even numbers, the function returns 0.
    
    Raises:
    TypeError: If the input is not a list or the list contains non-numeric elements.
    """
    try:
        even_numbers = [num for num in numbers if num % 2 == 0]
        if not even_numbers:
            return 0
        product = 1
        for num in even_numbers:
            product *= num
        return product
    except TypeError:
        print("Error: The input must be a list of numbers.")
        return None
    
numbers = [8, 9, 11, 20, 32, 101, 100]
result = product_of_even_numbers(numbers)
if result is not None:
    print(f"The product of even numbers in the list is: {result}")
