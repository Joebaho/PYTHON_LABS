'''
PYTHON LAB: receipt_sales.py

Write a code usung function that will add item in your grocery cart and return total in a file name reciept.txt 

order = {'tomato':30, 'thyme':4.50, 'garlic':7.5, 'rice':10, 'onions':4, 'fish':9.99}

Make sure to use exceptions handled and Docstring for this code to make code look great! 
'''

import datetime

def add_item_to_cart(item, price, cart, receipt_file):
    """
    Adds an item and its price to the cart and writes the receipt to a file.

    Args:
        item (str): The name of the item.
        price (float): The price of the item.
        cart (dict): The cart dictionary containing items and their prices.
        receipt_file (str): The file path to write the receipt.

    Returns:
        total (float): The total price of all items in the cart.
    """
    cart[item] = price
    total = sum(cart.values())
    
    with open(receipt_file, 'w') as f:
        f.write("\t\tYour Shopping Receipt:\n\n")
        f.write(f"Name:\t{client_name.upper()} \t\t Date/time: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("\nDesignation of items:\n\n")
        f.write("-------------------------------\n")
        for idx, (item, price) in enumerate(cart.items(), start=1):
            f.write(f"\t{idx}.{item}: \t${price:.2f}\n")
            f.write("-------------------------------\n")
        f.write(f"\nTotal: \t${total:.2f}\n")

# Example usage
client_name = input("Enter the client name:\t ")
cart = {}
receipt_file = "receipt.txt"
now = datetime.datetime.now()

# Add items to the cart
add_item_to_cart("Tomato", 30, cart, receipt_file)
add_item_to_cart("Thyme", 4.50, cart, receipt_file)
add_item_to_cart("Garlic", 7.50, cart, receipt_file)
add_item_to_cart("Rice", 10, cart, receipt_file)
add_item_to_cart("Onions", 4, cart, receipt_file)
add_item_to_cart("Fish", 9.99, cart, receipt_file)

# Print receipt details to console
print("\t\tYour Shopping Receipt:\n\n")
print(f"Name:\t{client_name.upper()} \t\t Date/time: ", now.strftime('%Y-%m-%d %H:%M:%S'))
print("\nDesignation of items:\n")

# Loop through cart items and print them with numbers
for idx, (item, price) in enumerate(cart.items(), start=1):
    print(f"\t{idx}.{item}: \t${price:.2f}")
print(f"\n\tTotal: \t${sum(cart.values()):.2f}")

###############################################################################################
def create_grocery_receipt(order, filename="receipt.txt"):
    """
    Creates a receipt for grocery items and saves it to a text file.
    
    Parameters:
    order (dict): A dictionary containing items as keys and prices as values
    filename (str): Name of the file to save the receipt (default: 'receipt.txt')
    
    Returns:
    float: Total amount of the order
    
    Raises:
    TypeError: If the input is not a dictionary
    ValueError: If prices are negative or non-numeric
    IOError: If there's an error writing to the file
    """
    try:
        # Verify that order is a dictionary
        if not isinstance(order, dict):
            raise TypeError("Order must be a dictionary")
        
        # Calculate total and validate prices
        total = 0
        for item, price in order.items():
            if not isinstance(price, (int, float)):
                raise ValueError(f"Price for {item} must be a number")
            if price < 0:
                raise ValueError(f"Price for {item} cannot be negative")
            total += price
        
        # Create receipt content
        receipt_content = """
=================================
          GROCERY RECEIPT        
=================================
"""
        # Add items and prices
        for item, price in order.items():
            receipt_content += f"{item.capitalize():15} ${price:>8.2f}\n"
        
        receipt_content += """
=================================
"""
        receipt_content += f"Total Amount:      ${total:>8.2f}\n"
        receipt_content += "=================================\n"
        receipt_content += "Thank you for shopping with us!\n"
        
        # Write to file
        with open(filename, 'w') as file:
            file.write(receipt_content)
            
        return total
    
    except IOError as e:
        print(f"Error writing to file: {e}")
        return None
    except (TypeError, ValueError) as e:
        print(f"Error with input data: {e}")
        return None

# Test the function
def main():
    order = {
        'tomato': 30,
        'thyme': 4.50,
        'garlic': 7.5,
        'rice': 10,
        'onions': 4,
        'fish': 9.99
    }
    
    try:
        total = create_grocery_receipt(order)
        if total is not None:
            print(f"Receipt has been created successfully!")
            print(f"Total amount: ${total:.2f}")
            
            # Read and display the receipt
            print("\nHere's your receipt:")
            with open('receipt.txt', 'r') as file:
                print(file.read())
                
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()