class GeneralManager:
    def __init__(self, chefs, waiters, cashiers,schedules):
        self.chefs = chefs
        self.waiters = waiters
        self.cashiers = cashiers
        self.next_chef = 4
        self.next_waiter = 4
        self.next_cashier = 3
        self.schedules=schedules

    def get_employees(self, position):
        if position == "chef":
            return self.chefs
        elif position in ["waiter", "waitress"]:
            return self.waiters
        elif position == "cashier":
            return self.cashiers
        return None

    def get_all_employee_ids(self,id):
        if id >=300: #Ids of casheirs start from 300
            return self.cashiers[id]
        elif id>=200:
            return self.waiters[id]
        elif id>=100:
            return self.cashiers[id]
        return None

    def add_employee(self, name, employee_id, position, salary):
        employees = self.get_employees(position)
        if employees is None:
            print("Invalid position")
            return
        if position == "chef":
            key = self.next_chef
            self.next_chef += 1
        elif position in ["waiter", "waitress"]:
            key = self.next_waiter
            self.next_waiter += 1
        else:
            key = self.next_cashier
            self.next_cashier += 1
        employees[key] = {
            "name": name,
            "id": employee_id,
            "position": position,
            "salary": salary
        }
        self.display_employee()
        print("Added successfully")

    def remove_employee(self, employee_id, position):
        employees = self.get_employees(position)
        if employees is None:
            print("Invalid position")
            return
        for key, employee in employees.items():
            if employee["id"] == employee_id:
                del employees[key]
                self.display_employee()
                print("Removed successfully")
                return
        print("Can't find ID")

    def update_employee(self, employee_id, name, position, salary):
        employees = self.get_employees(position)
        if employees is None:
            print("Invalid position")
            return
        for employee in employees.values():
            if employee["id"] == employee_id:
                employee["name"] = name
                employee["position"] = position
                employee["salary"] = salary
                self.display_employee()
                print("Updated successfully")
                return
        print("Can't find ID")
    def schedule_employee(self, employee_id, day, shift):
        if employee_id not in self.get_all_employee_ids():
            print("Employee not found")
            return
        if employee_id in self.schedule:
            if self.schedule[employee_id]["day"] == day:
                print("Employee already has a shift on this day")
                return
            self.schedule[employee_id] = {
                "day": day,
                "shift": shift
            }
        print("Employee scheduled successfully")

    def display_employee(self):
        print("\n--- Chefs ---")
        print(self.chefs)
        print("\n--- Waiters ---")
        print(self.waiters)
        print("\n--- Cashiers ---")
        print(self.cashiers)

    def display_schedule(self):
        print("\n---Schedule of the week---")
        print(self.schedules)    
# ---------------- DATA ----------------
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
        "position": "Head chef",
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
        "Evening": ["101", "201"]
    },

    "Tuesday": {
        "Morning": ["102", "400"],
        "Evening": ["100", "202"]
    },

    "Wednesday": {
        "Morning": ["101", "201"],
        "Evening": ["300", "400"]
    }
}
# ---------------- TEST ----------------
employee = GeneralManager(chefs, waiters, cashiers,schedule)
employee.add_employee("Hassan Hassan", "103", "chef", 5000)
employee.remove_employee("103", "chef")
employee.update_employee("300", "Laila Walid", "cashier", 3000)
employee.display_schedule()
