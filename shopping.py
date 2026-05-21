# Flipkart-style Shopping App (Console-Based)

# Sample product database
products = {
    "Mobiles": {
        "Samsung Galaxy S23": 69999,
        "Redmi Note 12": 18999
    },
    "Laptops": {
        "MacBook Air": 99999,
        "HP Pavilion": 59999,
        "Lenovo IdeaPad": 42999
    },
    "Watches": {
        "Apple Watch": 34999,
        "Fossil Gen 6": 14999,
        "Noise ColorFit": 2999
    }
}

cart = {}

def show_menu():
    print("\n🛒 Welcome to Flipkart Console App 🛍️")
    print("1. View Categories")
    print("2. View Cart")
    print("3. Checkout")
    print("4. Exit")

def show_categories():
    print("\nAvailable Categories:")
    for i, category in enumerate(products.keys(), 1):
        print(f"{i}. {category}")
    choice = int(input("Select a category number: "))
    category = list(products.keys())[choice - 1]
    show_products(category)

def show_products(category):
    print(f"\n--- {category} ---")
    category_products = products[category]
    for i, (item, price) in enumerate(category_products.items(), 1):
        print(f"{i}. {item} - ₹{price}")
    choice = int(input("Enter the number of product to add to cart (0 to cancel): "))
    if choice == 0:
        return
    selected_item = list(category_products.items())[choice - 1]
    add_to_cart(selected_item)

def add_to_cart(item):
    name, price = item
    if name in cart:
        cart[name]['quantity'] += 1
    else:
        cart[name] = {"price": price, "quantity": 1}
    print(f"✅ Added {name} to cart.")

def view_cart():
    if not cart:
        print("\n🛒 Your cart is empty.")
        return
    print("\n🛒 Items in Cart:")
    total = 0
    for i, (item, details) in enumerate(cart.items(), 1):
        print(f"{i}. {item} - ₹{details['price']} x {details['quantity']}")
        total += details['price'] * details['quantity']
    print(f"Total: ₹{total}")
    choice = input("Do you want to remove any item? (yes/no): ").strip().lower()
    if choice == 'yes':
        remove_item()

def remove_item():
    item_names = list(cart.keys())
    for i, item in enumerate(item_names, 1):
        print(f"{i}. {item}")
    choice = int(input("Enter number of item to remove: "))
    item_to_remove = item_names[choice - 1]
    del cart[item_to_remove]
    print(f"❌ Removed {item_to_remove} from cart.")

def checkout():
    if not cart:
        print("\n🛍️ Your cart is empty. Nothing to checkout.")
        return
    total = sum(details['price'] * details['quantity'] for details in cart.values())
    print("\n🧾 Final Bill:")
    for item, details in cart.items():
        print(f"{item} - ₹{details['price']} x {details['quantity']}")
    print(f"\nTotal Amount Payable: ₹{total}")
    print("✅ Checkout complete! Thank you for shopping with us.")
    cart.clear()

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        show_categories()
    elif choice == '2':
        view_cart()
    elif choice == '3':
        checkout()
    elif choice == '4':
        print("👋 Exiting... Have a great day!")
        break
    else:
        print("❌ Invalid choice. Try again.")
