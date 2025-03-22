import store
import products

# Setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = store.Store(product_list)


# Funktionen für das Menü
def list_products(store):
    print("------")
    products = store.get_all_products()
    if products:
        for idx, product in enumerate(products, 1):
            print(
                f"{idx}. {product.name}, Price: ${product.price}, Quantity: {product.get_quantity()}")
    else:
        print("No active products in the store.")
    print("------")
    return True


def show_total_number(store):
    total = store.get_total_quantity()
    print(f"Total of {total} items in store.")
    return True


def make_order(store):
    print("------")
    list_products(store)  # Zeigt die Produkte erneut an
    print("When you want to finish order, enter empty text.")

    order_list = []

    while True:
        product_choice = input("Which product # do you want? ")
        if product_choice == "":
            break  # Beendet die Bestellaufnahme

        try:
            product_index = int(
                product_choice) - 1  # 1-basiertes Menü auf 0-basierte Liste anpassen
            product = store.get_all_products()[product_index]
        except (ValueError, IndexError):
            print("Invalid choice. Please select a valid product number.")
            continue

        amount = input("What amount do you want? ")
        if not amount.isdigit():
            print("Please enter a valid number.")
            continue

        amount = int(amount)
        if amount > product.get_quantity():
            print(f"Sorry, only {product.get_quantity()} available.")
        else:
            order_list.append((product, amount))
            print("Product added to list!")

    if order_list:
        print("Order placed successfully!")
    else:
        print("No items were ordered.")


def quit_best_buy(store):
    print("Exiting store. Goodbye!")
    return False  # Signalisiert `start()`, dass die Schleife aufhören soll


# Function Dispatcher
func_dict = {
    1: list_products,
    2: show_total_number,
    3: make_order,
    4: quit_best_buy,
}


def start(store):
    """This function prints and controls the CLI menu."""
    while True:
        print("\n   Store Menu ")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        user_choice = input("Please choose a number: ")

        if not user_choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        user_choice = int(user_choice)
        if user_choice in func_dict:
            if not func_dict[user_choice](store):  # Falls Funktion False zurückgibt, Schleife beenden
                break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")


# Hauptprogramm starten
if __name__ == "__main__":
    start(best_buy)
