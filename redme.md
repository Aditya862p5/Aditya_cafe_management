# Aditya Cafe Management System

## 1. Project Overview

Aditya Cafe Management System is a Python console application designed to manage basic café ordering and billing operations. The system helps users handle tasks in a café setting through a clean and straightforward interface.

The system allows the user to:

- Enter customer details

- Choose between Dine-In or Takeaway

- View the café menu

- Add, view and remove food items

- Calculate subtotal, discount and GST

- Select a payment method

- Generate the bill

The project is divided into different Python modules. This keeps the code simple organized and easy to follow.

## 2. Features

### Customer Management

- Collect customer name and phone number

- Validate the input to ensure correctness

- selection between Dine-In and Takeaway

### Menu & Order Management

- Display the menu with item names and prices

- Add items with the desired quantity

- View the current order list

- Remove items from the order

### Billing

- Calculate the subtotal of selected items

- Apply discount based on the subtotal amount

- Calculate 5% GST on the discounted amount

- Compute the total

### Payment

- Accept payment via Cash

- Accept payment via UPI

- Accept payment via Card

### Bill

The final bill includes the following details:

- Order number

- Customer name and phone number

- Date and time of order

- Order type (Dine-In or Takeaway)

- List of items with quantities and prices

- Subtotal

- Discount applied

- GST amount

- Grand total

- Payment mode used

## 3. Technologies Used

- **Language:** Python

- **Version:** Python 3.x

- **IDE:** VS Code / IDLE / PyCharm

- **Version Control:** Git and GitHub

- **Libraries:** Python built-in modules

No external packages are needed. The system uses standard Python features.

## 4. Project Structure

AdityaCafe/

│

├── main.py

├── menu.py

├── customer.py

├── order.py

├── billing.py

├── bill.py

└── README.md

File          |                       Purpose                        |

|-------------|------------------------------------------------------|

|  `main.py`  | Controls the flow of the café system                 |
.
| `menu.py` | Stores and displays the menu items                     |

| `customer.py` | Handles customer information and order type        |

| `order.py` | Manages adding, viewing and removing items            |

| `billing.py` | Calculates subtotal, discount, GST and final amount |

| `bill.py` | Processes payment and prints the final bill            |

| `README.md` | Contains project documentation                       |

## 5. System Workflow

Start-->Enter Customer Details-->Select Dine-In / Takeaway-->Display Café Menu-->Add / View / Remove Items-->Generate Bill-->Calculate Subtotal-->Apply Discount-->Calculate GST-->Select Payment Method-->Print Final Bill-->End

## 6. Discount Rules

|       Subtotal       | Discount 
|----------------------|----------|
|Below Rs. 500                  0% |
| Rs. 500. Rs. 999            10% |
| Rs. 1000 Or more |          20% |

GST is calculated at 5% after applying the discount.

### Example

For a subtotal of Rs. 600:

Subtotal       = Rs. 600

Discount (10%) = Rs. 60

Amount         = Rs. 540

GST (5%)       = Rs. 27

Grand Total    = Rs. 567

---

## 7. Installation and Running

### Requirements

- Python 3.x

- Any Python IDE

### Run the Project

Open the project folder. Run the following command:


python main.py

## 8. How to Use

1. Enter the customers name and a 10-digit phone number.

2. Choose either Dine-In or Takeaway.

3. View the café menu.

4. Select food items and enter the quantity.

5.. Remove items if needed.

6. Generate the bill.

7. Choose a payment method: Cash, UPI or Card.

8. The final bill is. Displayed.

## 9. Input Validation

The program ensures input at every step. It checks:

- Customer name is not empty

- Phone number is 10 digits

- Menu item number is valid

- Quantity is greater than zero

- Order is not empty before generating the bill

- Payment mode is valid

If invalid input is entered the user is prompted to correct it.

## 10. Testing

The main test cases include:

- Entering a customer name

- Providing an invalid phone number

- Choosing an invalid menu item

- Entering an invalid quantity

- Trying to generate a bill with no items

- Attempting to remove an item not in the order

- Selecting an invalid payment option

- Testing all discount ranges


## 11. Limitations

- The application runs in the console only.

- Bills are not saved to a database or file.

- Menu items are hardcoded in the code.

## 12. Future Enhancements

Possible improvements for the future:

- Save and search past bills

- Change the quantity of items in the order

- Add or remove menu items

- Use a database to store data

- Add admin login for security

- Create a graphical user interface

- Generate sales reports and analytics

## 13. Learning Outcomes

This project helps practice:

- Python functions

- Lists and dictionaries

- Loops and conditional statements

- Input validation

- Modular programming

- Function arguments. Return values

- Basic arithmetic calculations

- Date and time handling

- Error handling

## 14.

The Aditya Cafe Management System is a yet effective project that shows how Python can be used for real-world tasks like managing café orders, billing and payments.

The modular design makes the project easy to understand maintain and extend. It is a starting point, for learning practical Python development.