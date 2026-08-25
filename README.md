# restaurant-project
OOP  and GIT task


Overview:

The system is divided into four main classes: Customer, Chef, Financial Manager, and General Manager, all preceded by the Menu and Order classes, so that each one can use them differently, whether by choosing an option from the menu, as in the Customer class, or by adding options, as in the Manager class.

Team Members:

Nicole ---> Main Manager branch
Menna ---> Financial Manager branch
Mariam ---> Chef branch
Sama ---> Customer branch

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



