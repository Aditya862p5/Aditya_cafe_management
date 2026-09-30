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