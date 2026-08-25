# restaurant-project
OOP  and GIT task


Overview:

The system is divided into four main classes: Customer, Chef, Financial Manager, and General Manager, all preceded by the Menu and Order classes, so that each one can use them differently, whether by choosing an option from the menu, as in the Customer class, or by adding options, as in the Manager class.

Team Members:

main manager (Nicole)------financial manager (Menna)-------chef (Mariam)------customer (sama)

------------------------------------------------------------------------------------------------------------------------------------------------

Main / Common code:
The ‘MainFile.py’ module defines the foundational classes and globel lists used across all staff branches.

1. “MenuItems” : 
    It represents an item which is available on the restaurant menu. It recieves attributes to define any menu item, they are as follows:
    item_id, item_name, price, availability.
2. “ Order”:
    It represents a customer’s order placed at a table. It recieves the following attributes:  order_id, table_number, item list, status , total_price.
3. Global data structures: 
    global_ menu which is a list holding all registered MenuItems objects and global_orders which is a shared system queue holding all active and completed orders.

As previously mentioned, the purpose of these shared classes are to establish a commonness between every staff class and allow the classes to work together well without overlapping eachother.

------------------------------------------------------------------------------------------------------------------------------------------------

Chef Class:
<> The chef class handles kitchen operations within the system. It acts as the interface for kitchen staff to track pending orders, update order progress and change the menu when an item is out of stock.

<> It consists of 3 methods: 

1. View pending orders:
    It displays all active orders in the kitchen queue that have not been completed yet as well as printing an error message if there are no active orders.
2. Update order status:
    This method takes a new status and updates the order status in the orders list and outputs a decriptive confirmation.
3. Change item availability:
    Allows the kitchen staff to mark menu items either as available or out of stock and updates the global menu list.
------------------------------------------------------------------------------------------------------------------------------------------------


Customer Branch:

<> The class constructor is a welcome message and shows the menu.

Menu items themselves were set through the Menu class. As mentioned, this will help to connect the same order with different classes.

<> The Customer has four methods:

-Make an order
-Take the bill
-Make a review
-Pay credit


<> Notes on Each Function:

1. Make an order:
The function should handle any unexpected inputs, whether by asking for the input again or by breaking and sending a message: "Error, resubmit your order."

2. Take the bill:
This function is mainly for displaying the items and their prices, while the main and total calculations after taxes and discounts are done by a function imported from the Financial Manager class, which is generate_bill.

3. Make a review:
If the rating is <= 3, the user is allowed to input their complaint due to the low rating.

4. Pay credit:
An optional feature, which is an attempt to connect a bank system with a restaurant system by withdrawing the bill amount from the user's bank account.

--------------------------------------------------------------------------------------------------------------------------------------------------



Financial Manager Branch:


<> The FinancialManager class handles the restaurant's basic financial operations, including bill generation, expense tracking, revenue calculation, profit calculation, and financial reporting.

<> Features :

- Bill Generation: Calculates an order's subtotal from its items and applies a validated discount.

- Discount Validation: Prevents negative discounts and ensures the discount does not exceed the order subtotal.

- Expense Tracking: Records restaurant expenses and amount while rejecting negative amounts.

- Revenue Calculation: Calculates total revenue from completed orders.

- Profit Calculation: Calculates net profit or loss by subtracting total expenses from total revenue.

- Financial Reporting: Displays total revenue, total expenses, net profit, and whether the restaurant made a profit, a loss, or broke even.


<> Main Functions :

-generate_bill()
-calculate_revenue()
-add_expense()
-calculate_net_profit()
-report()




