from RandomIDs import generate_4_digit_id
class GeneralManager:
    def __init__(self, chefs, waiters, cashiers, schedules):
        self.chefs = chefs
        self.waiters = waiters
        self.cashiers = cashiers
        self.next_chef = 4
        self.next_waiter = 4
        self.next_cashier = 3
        self.schedules = schedules
    def get_employees(self, position):
        position = position.lower()
        if position in ["chef","head chef"]:
            return self.chefs
        elif position in ["waiter", "waitress", "head waiter"]:
            return self.waiters
        elif position == "cashier":
            return self.cashiers
        return None
    def get_employee_by_id(self, employee_id):
        employee_id = str(employee_id)
        for employee in self.chefs.values():
            if employee["id"] == employee_id:
                return employee
        for employee in self.waiters.values():
            if employee["id"] == employee_id:
                return employee
        for employee in self.cashiers.values():
            if employee["id"] == employee_id:
                return employee
        return None
    
    def add_employee(self, name, position, salary):
        position = position.lower()
        employees = self.get_employees(position)
        if employees is None:
            print("Invalid position")
            return
        if position == "chef":
            key = self.next_chef
            self.next_chef += 1
        elif position in ["waiter", "waitress", "head waiter"]:
            key = self.next_waiter
            self.next_waiter += 1
        else:
            key = self.next_cashier
            self.next_cashier += 1
        employees[key] = {"name": name,"id": str(generate_4_digit_id()),
            "position": position,"salary": salary}
        print("Added successfully")
    def remove_employee(self, employee_id, position):
        position = position.lower()
        employees = self.get_employees(position)
        if employees is None:
            print("Invalid position")
            return
        employee_id = str(employee_id)
        for key, employee in list(employees.items()):
            if employee["id"] == employee_id:
                self.remove_from_schedule(employee_id)
                del employees[key]
                print("Removed successfully")
                return
        print("Can't find ID")
    def update_employee(self, name, employee_id, position, salary):
        position = position.lower()
        employee = self.get_employee_by_id(employee_id)
        if employee is None:
            print("Can't find ID")
            return
        if self.get_employees(position) is None:
            print("Invalid position")
            return
        employee["name"] = name
        employee["position"] = position
        employee["salary"] = salary
        print("Updated successfully")
    def schedule_employee(self, employee_id, day, shift):
        employee_id = str(employee_id)
        day = day.capitalize()
        shift = shift.capitalize()
        if self.get_employee_by_id(employee_id) is None:
            print("Employee not found")
            return
        valid_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        if day not in valid_days:
            print("Invalid day")
            return
        if shift not in ["Morning", "Evening"]:
            print("Invalid shift")
            return
        if day not in self.schedules:
            self.schedules[day] = {
                "Morning": [],
                "Evening": []
            }
        if shift not in self.schedules[day]:
            self.schedules[day][shift] = []
        for existing_shift in self.schedules[day]:
            if employee_id in self.schedules[day][existing_shift]:
                print("Employee already has a shift on this day")
                return
        self.schedules[day][shift].append(employee_id)
        print("Employee scheduled successfully")
    def remove_from_schedule(self, employee_id):
        employee_id = str(employee_id)
        for day in self.schedules:
            for shift in self.schedules[day]:
                if employee_id in self.schedules[day][shift]:
                    self.schedules[day][shift].remove(employee_id)
    def display_employee(self):
        print("\n--- Chefs ---")
        for employee in self.chefs.values():
            print(employee)
        print("\n--- Waiters ---")
        for employee in self.waiters.values():
            print(employee)
        print("\n--- Cashiers ---")
        for employee in self.cashiers.values():
            print(employee)
    def display_schedule(self):
        print("\n--- Schedule of the week ---")
        for day, shifts in self.schedules.items():
            print(f"\n{day}:")
            for shift, employees in shifts.items():
                print(f"  {shift}: {employees}")
# =====================================================
# DATA
# =====================================================
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
        print("Please enter a number:")
        continue
    if choice == 1:
        try:
            name = input("Enter the name: ")
        except ValueError:
            print("Please enter characters:")
            continue
        try:
            position = input("Enter position: ").lower()
        except ValueError:
            print("Please enter characters:")
            continue
        try:
            salary = int(input("Enter the salary: "))
        except ValueError:
            print("Salary must be a number")
            continue
        employee.add_employee(name,position,salary)
    elif choice == 2:
        try:
            employee_id = input("Enter ID: ")
        except ValueError:
            print("Please enter a valid ID:")
            continue
        try:
            position = input("Enter position: ").lower()
        except ValueError:
            print("Please enter characters:")
            continue
        employee.remove_employee(employee_id,position)
    elif choice == 3:
        try:
            name = input("Enter the name: ")
        except ValueError:
            print("Please enter characters:")
            continue
        try:
            employee_id = input("Enter ID: ")
        except ValueError:
            print("Please enter a valid ID:")
            continue
        try:
            position = input("Enter position: ").lower()
        except ValueError:
            print("Please enter characters:")
            continue
        try:
            salary = int(input("Enter the salary: "))
        except ValueError:
            print("Salary must be a number")
            continue
        employee.update_employee(name,employee_id,position,salary)
    elif choice == 4:
        try:
            employee_id = input("Enter ID: ")
        except ValueError:
            print("Please enter a valid ID:")
            continue
        try:
            day = input("Enter day: ")
        except ValueError:
            print("Please enter a valid day:")
            continue
        try:
            shift = input("Enter shift (morning/evening): ")
        except ValueError:
            print("Please enter a valid shift:")
            continue
        employee.schedule_employee(employee_id,day,shift)
    elif choice == 5:
        employee.display_employee()
    elif choice == 6:
        employee.display_schedule()
    elif choice == 7:
        print("Exit program successfully!")
        break
    else:
        print("Invalid choice")