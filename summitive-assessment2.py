# Vending Machine Program
# Author: Muhammad Ammar Ammar
# Date: January 13, 2026

# Inventory dictionary: code -> details
inventory = {
    'A1': {'name': 'Coke', 'price': 3.57, 'category': 'Drinks', 'stock': 68},
    'A2': {'name': 'Pepsi', 'price': 2.12, 'category': 'Drinks', 'stock': 50},
    'A3': {'name': 'Coffee', 'price': 1.26, 'category': 'Drinks', 'stock': 89},
    'B1': {'name': 'Chips', 'price': 3.98, 'category': 'Snacks', 'stock': 83},
    'B2': {'name': 'Biscuits', 'price': 1.28, 'category': 'Snacks', 'stock': 56},
    'B3': {'name': 'Chocolate', 'price': 3.83, 'category': 'Snacks', 'stock': 87}
}

# Suggestions based on item name
suggestions = {
    'Coffee': 'Biscuits',
    'Coke': 'Chips',
    'Pepsi': 'Chips'
}

def display_menu(inventory):
    # Group items by category for better UX
    categories = {}
    for code, item in inventory.items():
        cat = item['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(f"{code}: {item['name']} - {item['price']:.2f} AED (Stock: {item['stock']})")
    
    print("Vending Machine Menu:")
    for cat, items in categories.items():
        print(f"\n{cat}:")
        for item in items:
            print(item)
    print("\nEnter code to select, or 'quit' to exit.")

def handle_purchase(code, inventory):
    # Check if code exists
    if code not in inventory:
        print("Invalid code. Try again.")
        return False
    
    item = inventory[code]
    if item['stock'] <= 0:
        print(f"Sorry, {item['name']} is out of stock.")
        return False
    
    print(f"Selected: {item['name']} - {item['price']:.2f} AED")
    try:
        tendered = float(input("Insert money (AED): "))
    except ValueError:
        print("Invalid amount. Transaction cancelled.")
        return False
    
    if tendered < item['price']:
        print("Insufficient funds. Transaction cancelled.")
        return False
    
    change = tendered - item['price']
    print(f"Dispensing {item['name']}. Enjoy!")
    inventory[code]['stock'] -= 1  # Update stock
    
    # Suggest related item using change as credit
    suggested = False
    if item['name'] in suggestions:
        suggest_name = suggestions[item['name']]
        for c, it in inventory.items():
            if it['name'] == suggest_name and it['stock'] > 0:
                yn = input(f"Would you like to add {suggest_name} for {it['price']:.2f} AED? (y/n): ").lower()
                if yn == 'y':
                    if change >= it['price']:
                        change -= it['price']
                        print(f"Dispensing {suggest_name}. Enjoy!")
                        inventory[c]['stock'] -= 1  # Update stock for add-on
                        suggested = True
                    else:
                        print(f"Not enough credit for {suggest_name}. Dispensing your change now.")
                break
    
    # Now give the final change
    print(f"Your change: {change:.2f} AED")
    
    return True

# Main loop
while True:
    display_menu(inventory)
    code = input("Enter code: ").upper()
    if code == 'QUIT':
        break
    if handle_purchase(code, inventory):
        # Only ask if purchase was successful
        while True:
            more = input("Buy another? (y/n): ").lower()
            if more == 'y':
                break  # Continue to next purchase
            elif more == 'n':
                print("Thank you for using the vending machine!")
                exit()  # Or break out of outer loop, but using exit for simplicity
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
    # If purchase failed, loop back to menu automatically

print("Thank you for using the vending machine!")