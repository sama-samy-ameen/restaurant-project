
#Standard shared classes.
#import classes.
from chef import Chef
from financial import FinancialManager
from GeneralManager import GeneralManager
from restaurant_common_data import Order,global_menu,global_orders,total_revenue


#a list of dicts containing staff members and their specifications.
staff_roster=[{"name": "Mariam", "role": "Chef", "status": "Active"},
              {"name": "Nicole", "role": "General Manager"}]

#create a user credentials database.
users_database= {
    "Chef1": {"password" : "1234", "role" : "Chef"}, 
    "fin1" : {"password": "123", "role": "Financial Manager"}
}

chefs = {
    1: {
        "name": "Ahmed Mohamed",
        "id": "100",
        "position": "chef",
        "salary": 5000
    },

    2: {
        "name": "Tamer Adel",
        "id": "101",
        "position": "chef",
        "salary": 5000
    },

    3: {
        "name": "Mohamed Hany",
        "id": "102",
        "position": "chef",
        "salary": 8000
    }
}

waiters = {
    1: {
        "name": "Mona Ahmed",
        "id": "200",
        "position": "waitress",
        "salary": 4500
    },

    2: {
        "name": "Ali Khaled",
        "id": "201",
        "position": "waiter",
        "salary": 4500
    },

    3: {
        "name": "Mohamed Moamen",
        "id": "202",
        "position": "Head waiter",
        "salary": 6500
    }
}

cashiers = {
    1: {
        "name": "Layla Walid",
        "id": "300",
        "position": "cashier",
        "salary": 3000
    },

    2: {
        "name": "Ibrahim Mohsen",
        "id": "301",
        "position": "cashier",
        "salary": 3000
    }
}
schedule = {
    "Monday": {
        "Morning": ["100", "200", "300"],
        "Evening": ["101", "201","301"]
    },

    "Tuesday": {
        "Morning": ["102","202","301"],
        "Evening": ["100", "200","300"]
    },

    "Wednesday": {
        "Morning": ["101", "201","300"],
        "Evening": ["300", "102","202"]
    },

    "Thursday":{
        "Morning":["100","200","301"],
        "Evening":["101","201","301"]
    },

    "Friday":{
        "Morning":["102","201","202"],
        "Evening":["100","202","300"]
    },

    "Saturday":{
        "Morning":["101","200","300"],
        "Evening":["102","201","301"]
    },

    "Sunday":{
            "Morning":["100","202","301"],
            "Evening":["101","200","300"]
        }

}

#creating seperate interfaces.+
#create chef interfaces.
def chef_interface(chef_user):
    while True:
        print(f" ----Chef Dashboard ({chef_user.name})----")
        print("1. View kitchen order queue")
        print("2. Update order status")
        print("3. Change menu item availability")
        print("4. Logout/ Back to role selection")
        option=input("Select option 1-4:").strip()
        match option:
            case "1":
                chef_user.view_pending_orders(global_orders)
            case "2":
                try:
                    order_id=int(input("Enter order ID to update:"))
                    new_status=input("Enter status (In progress/ Ready/ Completed)").strip()
                    chef_user.update_order_status(order_id, new_status, global_orders)
                except ValueError:
                    print("Invalid input! Order ID must be numeric.")
            case "3":
                try:
                    item_id=int(input("Enter menu item ID:"))
                    avail_input=input("Is it available? (y/n):").lower().strip()
                    availability=(avail_input=='y')
                    chef_user.change_item_availability(item_id, availability, global_menu)
                except ValueError:
                    print("Invalid input!")
            case "4":
                print(f"Logging out {chef_user.name}...")
                break
            case _:
                print("Invalid selection.")


# for other team members, please insert your part of the code here

#customer interface takes place after making the order

def General_menu():
    employee = GeneralManager( chefs,waiters,cashiers, schedule)
    while True:
        print("\n================================")
        print("       RESTAURANT SYSTEM")
        print("================================")
        print("1. Add employee")
        print("2. Remove employee")
        print("3. Update employee")
        print("4. Update schedule")
        print("5. Display employees")
        print("6. Display schedule")
        print("7. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number")
            continue
        if choice == 1:
            name = input("Enter the name: ")
            employee_id = input("Enter ID: ")
            position = input("Enter position: ").lower()
            try:
                salary = int(input("Enter the salary: "))
            except ValueError:
                print("Salary must be a number")
                continue
            employee.add_employee(
                name,
                employee_id,
                position,
                salary
            )
        elif choice == 2:
            employee_id = input("Enter ID: ")
            position = input("Enter position: ").lower()
            employee.remove_employee(
                employee_id,
                position
            )
        elif choice == 3:
            name = input("Enter the name: ")
            employee_id = input("Enter ID: ")
            position = input("Enter position: ").lower()
            try:
                salary = int(input("Enter the salary: "))
            except ValueError:
                print("Salary must be a number")
                continue
            employee.update_employee(
                name,
                employee_id,
                position,
                salary
            )
        elif choice == 4:
            employee_id = input("Enter ID: ")
            day = input("Enter day: ")
            shift = input("Enter shift (morning/evening): ")
            employee.schedule_employee(
                employee_id,
                day,
                shift
            )
        elif choice == 5:
            employee.display_employee()
        elif choice == 6:
            employee.display_schedule()
        elif choice == 7:
            print("Exit program successfully!")
            break
        else:
            print("Invalid choice")




#create financial interface
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








#=======Authentication and system entry====
def handle_role_portal(role):
    # submenu for chosen role
    while True:
        print("=====================")
        print(f" {role} Portal")
        print("=====================")
        print("1. Login")
        print(f"2. Register New {role} Account")
        print("3. Back to role selection")
        choice=input("Select option 1-3:").strip()
        match choice:
            case "1":
                login(role)
            case "2":
                register_account(role)
            case "3":
                break
            case _:
                print("Invalid choice! Please select a number between 1 and 3")


def login(role):
    print("----User Login----")
    username=input("Username:").strip()
    password=input("Password:").strip()

    if username in users_database and users_database[username]["password"]==password:
        user_role= users_database[username]["role"]
        if user_role==role:
            print(f"Login successful! Welcome, {username} ({role}).")
            route_user(username, role)
        else:
            print(f"Access denied! Your account '{username}' is registered as [{user_role}], not [{role}].")     
    else:
        print("Invalid username or password!")


def main():
    while True:
        print("=======================================")
        print("Welcome to restaurant management system")
        print("=======================================")
        print("1. General Manager")
        print("2. Financial Manager")
        print("3. Chef")
        print("4. Customer")
        print("5. Exit program")
        choice=input("Select your role:").strip()
        match choice:
            case "1":
                handle_role_portal("General Manager")
            case "2":
                handle_role_portal("Financial Manager")
            case "3":
                handle_role_portal("Chef")
            case "4":
                handle_role_portal("Customer")
            case "5":
                print("Shutting down system!")
                break
            case _:
                print("Invalid option! Please enter a number between 1 and 5")

def register_account(role):
    print("---Account Registration---")
    while True:
        username=input("Enter desired username:").strip()

        #check if username is already taken.
        if username in users_database:
            print(f"Error! The username {username} already exists!")
            print("Select from the following options:")
            print("1. Login with this username")
            print("2. Try a different username")
            print("3. Cancel and return to main menu")
            choice=input("Select option 1-3:").strip()
            match choice:
                case "1":
                    login(role)
                    return
                case "2":
                    continue
                case "3":
                    return
                case _:
                    print("Invalid option! Returning to main menu")
                    continue

        password=input("Enter password:").strip()
        users_database[username]= {"password": password, "role": role}
        print(f"Success! Account created for '{username}' as [{role}].")
        # extra option to go straight to login after registering.
        while True:
            start_now = input("Would you like to login now? (y/n):").lower().strip()
            if start_now =='y':
                route_user(username, role)
            return
  



def route_user(username, role):
    match role:
        case "Chef":
            chef_obj= Chef(username, "Head Chef")
            chef_interface(chef_obj)
        case "Financial Manager":
            fin_obj=FinancialManager()
            financial_menu(fin_obj, global_orders)
        case "General Manager":
            Genmang_obj=GeneralManager(chefs, waiters ,cashiers, schedule)
            General_menu()

        case "Customer":
            from customer import Customer
            cus_obj=Customer()
        case _:
            print ("Unknown user role.")



if __name__ == "__main__" :
    main()



