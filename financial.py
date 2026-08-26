
class FinancialManager:

    def __init__(self):
        self.expenses = []

    def generate_bill(self, order, discount=0):
        """
        Calculate bill after discount.
        """

        subtotal = 0

        # Calculate the order subtotal.
        for item in order.items:
            subtotal += item.price

        # Validate the discount.
        if discount < 0:
            discount = 0

        if discount > subtotal:
            discount = subtotal

        order.total_price = subtotal - discount

        return order.total_price

    def calculate_revenue(self, global_orders):
        """
        Calculate total revenue .
        """

        total_revenue = 0

        # Add completed order totals.
        for order in global_orders:
            if order.status == "Completed":
                total_revenue += order.total_price

        return total_revenue

    def add_expense(self, description, amount):
        """
        Add a restaurant expense.
        """

        # Reject negative expense amounts.
        if amount < 0:
            return None

        expense = {
            "description": description,
            "amount": amount
        }

        self.expenses.append(expense)

        return expense

    def calculate_net_profit(self, global_orders):
        """
        Calculate net profit or loss .
        """

        revenue = self.calculate_revenue(global_orders)
        total_expenses = 0

        # Calculate total expenses.
        for expense in self.expenses:
            total_expenses += expense["amount"]

        return revenue - total_expenses

    def report(self, global_orders):
        """
        Display the financial report.
        """

        revenue = self.calculate_revenue(global_orders)

        total_expenses = 0

        # Calculate total expenses.
        for expense in self.expenses:
            total_expenses += expense["amount"]

        net_profit = revenue - total_expenses

        print("\n========== Financial Report ==========")
        print(f"Total Revenue:  {revenue:.2f}")
        print(f"Total Expenses: {total_expenses:.2f}")
        print(f"Net Profit:     {net_profit:.2f}")

        if net_profit > 0:
            print("Result: Profit")
        elif net_profit < 0:
            print("Result: Loss ")
        else:
            print("Result: Break-even")

        print("======================================")
def financial_menu(manager, global_orders):
    while True:
        print("\n========== Financial Manager ==========")
        print("1. Add Expense")
        print("2. Display Expenses")
        print("3. Calculate Revenue")
        print("4. Calculate Net Profit")
        print("5. Financial Report")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))

            result = manager.add_expense(description, amount)

            if result is not None:
                print("Expense added successfully.")
            else:
                print("Invalid expense amount.")

        elif choice == "2":
            if not manager.expenses:
                print("No expenses recorded.")
            else:
                print("\n========== Expenses ==========")

                for expense in manager.expenses:
                    print(f"Description: {expense['description']}")
                    print(f"Amount: {expense['amount']:.2f}")
                    print("------------------------------")

        elif choice == "3":
            print(
                f"Total Revenue: "
                f"{manager.calculate_revenue(global_orders):.2f}"
            )

        elif choice == "4":
            print(
                f"Net Profit: "
                f"{manager.calculate_net_profit(global_orders):.2f}"
            )

        elif choice == "5":
            manager.report(global_orders)

        elif choice == "6":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    manager = FinancialManager()
    global_orders = []

<<<<<<< HEAD
    financial_menu(manager, global_orders)
=======
    financial_menu(manager, global_orders)
>>>>>>> 1a4d4acc9ec38cb49b77512b536ae3e1bc840e39
