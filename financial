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
        Calculate net profit or loss.
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
            print("Result: Loss")
        else:
            print("Result: Break-even")

        print("======================================")