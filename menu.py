menu = {
    1: ["Coffee", 50],
    2: ["Tea", 30],
    3: ["Cold Coffee", 80],
    4: ["Burger", 120],
    5: ["Pizza", 180],
    6: ["Sandwich", 90],
    7: ["French Fries", 70],
    8: ["Momos", 120],
    9: ["Ice Cream", 60],
    10: ["Cake", 250],
    11: ["Cheese Cake", 300],
    12: ["Garlic Bread", 230],
    13: ["MilkShake", 120]
}


def show_menu():

    print("\n" + "=" * 40)
    print("              CAFE MENU")
    print("=" * 40)

    print("No.  Item                 Price")
    print("-" * 40)

    for number in menu:

        name = menu[number][0]
        price = menu[number][1]

        print(f"{number:<4}{name:<20}Rs.{price}")

    print("=" * 40)