# Aditya Cafe Management System

# 1. Problem Statement

Managing customer orders and preparing the bill manually in a café may cost time and have errors in calculation of price, discount, GST and total amount.

Aditya Cafe Management System is designed to provide a simple python based solution for managing cafe orders and prepare bill.

The system provides,

User can enter customer details, select order type, view menu, add items, remove items, calculate bill, select payment method and prepare the bill.
The project uses separate python modules to organize the program.

# 2. Scope of the Project
The scope of the project comprises the following features required for a cafe ordering and billing system.

The system provides,

Customer detail management
Dine-In and Takeaway selection
Cafe menu display
Food item selection

Quantity input
Order management
Item removal
Subtotal calculation
Discount calculation
GST calculation
Grand total calculation
Payment method selection
Final bill generation

Basic input validation and error handling

The Current project is designed as a console based python application.
The current version has no database or permanent storage of bill.

# 3. Target Users
The target users of the system are
## Cafe Staff
Cafe staff can use the system to
Enter customer details
Take customer orders
View orders
Remove wrong items
Generate bills
Select payment methods
## Cafe Owner
The cafe owner can use the project as a basic computerized system to understand and manage the cafe ordering and billing process.
## Students
This project is also designed as an academic project to demonstrate the python programming concepts like,
Functions
Lists
Dictionaries
Loops
Conditional statements
Input validation
Modular programming
Basic calculations

# 4. High-Level Features
## 4.1 Customer Management
The system collects,
Customer name
Phone number
Order type
The user can select,
Dine-In
Takeaway
## 4.2 Menu Management
The system display a cafe menu consisting of different food and beverage items with their prices
Example items are,
Coffee
Tea
Cold Coffee
Burger
Pizza
Sandwich
French Fries
Momos
Ice Cream
Cake
Cheese Cake
Garlic Bread
MilkShake
## 4.3 Order Management
The system allows,
Add food items
Enter quantity
View the current order
Remove an item from the order
Total price of each item is calculated as,
Item Price × Quantity
## 4.4 Billing Management
The system calculates,
Subtotal
↓
Discount
↓
GST
↓
Grand Total
Discount Rules,
Below Rs. 500 → No discount
Rs. 500 or above → 10% discount
Rs. 1000 or above → 20% discount
GST is calculated at 5%.

## 4.5 Payment Management
The system provides 3 payment options
1. Cash
2. UPI
3. Card

## 4.6 Bill Generation
The system displays,
Order number
Customer name
Phone number
Date and time
Order type
Ordered items
Subtotal
Discount
GST
Grand total
Payment mode

## 4.7 Input Validation
The system provides basic input validation to avoid invalid entries.
Examples,
Customer name can not be empty.
Phone number must contain 10 digits.
Menu item number must be valid.
Quantity must be a positive number.
Payment option must be valid.
Bill can not be generated when order is empty.

# 5. Project Objective
The objective of this project is to develop a simple and organized cafe management application using python.

The project demonstrates how various python concepts can be utilized to develop a solution for a practical problem using a modular approach.