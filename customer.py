def get_name():

    while True:

        name = input("Enter customer name: ").strip()

        if name != "":
            return name

        print("Name cannot be empty!")


def get_phone():

    while True:

        phone = input("Enter phone number: ").strip()

        if phone.isdigit() and len(phone) == 10:
            return phone

        print("Please enter a valid 10-digit number.")


def get_customer_details():

    print("\n--- Customer Details ---")

    name = get_name()
    phone = get_phone()

    return name, phone


def get_order_type():

    print("\n1. Dine-In")
    print("2. Takeaway")

    while True:

        choice = input("Choose Order Preference: ")

        if choice == "1":
            return "Dine-In"

        elif choice == "2":
            return "Takeaway"

        else:
            print("Please enter 1 or 2.")