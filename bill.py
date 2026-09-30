def calculate_bill(order):
    subtotal = 0
    for item in order:
        subtotal = subtotal + item[3]

    discount = 0
    if subtotal >= 1000:
        discount = subtotal * 0.20
    elif subtotal >= 500:
        discount = subtotal * 0.10

    gst = (subtotal - discount) * 0.05
    grand_total = subtotal - discount + gst

    return subtotal, discount, gst, grand_total


def get_payment_mode():
    print("\n--- Payment Mode ---")
    print("1. Cash")
    print("2. Card")
    print("3. UPI")
    
    while True:
        choice = input("Select Payment Mode: ")
        if choice == "1":
            return "Cash"
        elif choice == "2":
            return "Card"
        elif choice == "3":
            return "UPI"
        else:
            print("Please enter a valid option (1, 2, or 3).")


def print_bill(order_id, customer_name, phone, order_type, my_order, subtotal, discount, gst, grand_total, payment, date_time):
    print("\n" + "=" * 45)
    print("               ADITYA CAFE")
    print("=" * 45)
    print(f"Order ID : {order_id}")
    print(f"Date/Time: {date_time}")
    print(f"Customer : {customer_name} ({phone})")
    print(f"Order    : {order_type}")
    print(f"Payment  : {payment}")
    print("-" * 45)
    print(f"{'Item':<15} {'Qty':<5} {'Price':<10} {'Total'}")
    print("-" * 45)
    
    for item in my_order:
        print(f"{item[0]:<15} {item[1]:<5} Rs.{item[2]:<7} Rs.{item[3]}")
        
    print("-" * 45)
    print(f"Subtotal:         Rs. {subtotal:.2f}")
    print(f"Discount:       - Rs. {discount:.2f}")
    print(f"GST (5%):       + Rs. {gst:.2f}")
    print("-" * 45)
    print(f"GRAND TOTAL:      Rs. {grand_total:.2f}")
    print("=" * 45)
    print("          Thank You! Visit Again!")
    print("=" * 45)