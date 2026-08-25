# Restaurant Management System

## Description

This project is a restaurant management system developed using Python.
It allows the restaurant manager to manage employees, schedules, and
other restaurant operations.

## Features

- Add employees
- Remove employees
- Update employee information
- Display employees
- Manage employee schedules
- Manage chefs, waiters, and cashiers

## Employee Management

The system uses separate dictionaries to store:

- Chefs
- Waiters
- Cashiers

The `GeneralManager` class is responsible for managing employees.

### Adding an Employee

The `add_employee()` function adds a new employee according to their
position and stores their name, ID, position, and salary.

### Removing an Employee

The `remove_employee()` function searches for an employee using their
ID and removes them from the corresponding employee dictionary.

### Updating an Employee

The `update_employee()` function searches for an employee by ID and
updates their information.

## Employee Scheduling

The system uses a schedule dictionary to organize employees according
to the day and shift.

Example:

```python
schedule = {
    "Monday": {
        "Morning": ["100", "200", "300"],
        "Evening": ["101", "201"]
    }
}

