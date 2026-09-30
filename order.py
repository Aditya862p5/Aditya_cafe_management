from menu import menu
from menu import show_menu


def add_item(order):

    show_menu()

    choice = input("\nEnter item number: ")

    if not choice.isdigit():

        print("Please enter a valid number.")
        return

    choice = int(choice)

    if choice not in menu:

        print("Please enter the correct item number.")
        return

    quantity = input("Enter quantity: ")

    if not quantity.isdigit():

        print("Please enter a number.")
        return

    quantity = int(quantity)

    if quantity <= 0:

        print("Quantity must be greater than 0.")
        return

    item_name = menu[choice][0]
    price = menu[choice][1]

    total = price * quantity

    order.append([item_name, quantity, price, total])

    print(quantity, item_name, "added to your order!")


def show_order(order):

    if len(order) == 0:

        print("\nYour order is empty.")
        return

    print("\n========== YOUR ORDER ==========")

    count = 1

    for item in order:

        print(
            count,
            item[0],
            "x",
            item[1],
            "=",
            "Rs.",
            item[3]
        )

        count = count + 1

    print("================================")


def remove_item(order):

    show_order(order)

    if len(order) == 0:
        return

    number = input("\nEnter item number to remove: ")

    if not number.isdigit():

        print("Please enter a number.")
        return

    number = int(number)

    if number >= 1 and number <= len(order):

        removed = order.pop(number - 1)

        print(removed[0], "has been removed!")

    else:

        print("Invalid item number.")