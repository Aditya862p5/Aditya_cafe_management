import datetime

from customer import get_customer_details
from customer import get_order_type

from menu import show_menu

from order import add_item
from order import show_order
from order import remove_item

from billing import calculate_bill

from bill import get_payment_mode
from bill import print_bill


order_id = 1

my_order = []


print("======================================")
print("       WELCOME TO ADITYA CAFE")
print("======================================")


# Customer Details

customer_name, phone = get_customer_details()


# Order Type

order_type = get_order_type()


# Main System

while True:

    print("\n========== CAFE SYSTEM ==========")

    print("1. Display Menu")
    print("2. Add Item")
    print("3. View Order")
    print("4. Remove Item")
    print("5. Generate Bill")
    print("6. Exit")

    print("=================================")


    choice = input("Enter your choice: ")


    # Display Menu

    if choice == "1":

        show_menu()


    # Add Item

    elif choice == "2":

        add_item(my_order)


    # View Order

    elif choice == "3":

        show_order(my_order)


    # Remove Item

    elif choice == "4":

        remove_item(my_order)


    # Generate Bill

    elif choice == "5":

        if len(my_order) == 0:

            print("Cannot generate bill.")
            print("Your order is empty.")

            continue


        # Calculate Bill

        subtotal, discount, gst, grand_total = calculate_bill(my_order)


        # Payment

        payment = get_payment_mode()


        # Date and Time

        now = datetime.datetime.now()

        date_time = now.strftime("%Y-%m-%d %H:%M")


        # Print Bill

        print_bill(
            order_id,
            customer_name,
            phone,
            order_type,
            my_order,
            subtotal,
            discount,
            gst,
            grand_total,
            payment,
            date_time
        )


        # Prepare for next order

        order_id = order_id + 1

        my_order.clear()

        break


    # Exit

    elif choice == "6":

        print("\nClosing system.")
        print("Have a great day!")

        break


    # Wrong Choice

    else:

        print("Wrong choice.")
        print("Please select from 1 to 6.")