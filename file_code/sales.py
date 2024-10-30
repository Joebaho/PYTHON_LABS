'''
PYTHON LAB: sales.py

Write a code usung function that will add item in your grocery cart and return total in a file name reciept.txt 

order = {'tomato':30, 'thyme':4.50, 'garlic':7.5, 'rice':10, 'onions':4, 'fish':9.99}
'''
import datetime

def add_item_to_cart(item, price, cart, receipt_file):
    cart[item] = price
    total = sum(cart.values())
    
    with open(receipt_file, 'w') as f:
        f.write("\t\tYour Shopping Receipt:\n\n")
        f.write(f"Name:\t{client_name.upper()} \t\t Date/time: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("\nDesignation of items:\n\n")
        for idx, (item, price) in enumerate(cart.items(), start=1):
            f.write(f"\t{idx}.{item}: \t${price:.2f}\n")
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



