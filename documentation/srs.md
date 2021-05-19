# Department

## Vision

"Department" is web-application which allows users to record information about departments and employees.

Application should provide:

* Storing departments and employees in database;
* Display list of departments;
* Updating list of departments (adding, editing, removing);
* Display list of employees;
* Updating list of employees (adding, editing, removing);
* Filtering by date for employees;

## 1. Departments

### 1.1 Display list of departments

The mode is designed to view the list of departments that are stored in database. It is also home page.

**Main scenario:**

* User selects item "Departments";
* Application displays list of departments.

![Departments mockup](https://ibb.co/XDrDYPs "Departments")
Pic. 1.1 View the departments list.

The list displays the following columns:

* Name - department's name;
* Average salary - calculated automatically.

### 1.2 Add department

**Main scenario:**

* User clicks the "+" button in the departments list view mode;
* Application displays form to enter department data;
* User enter department data and press "Submit" button;
* If error occurs, then error message is displaying;
* If new record is successfully added, then list of departments with new record is displaying.

**Cancel operation scenario**

* User clicks the "+" button in the departments list view mode;
* Application displays form to enter department data;
* User press "Cancel" button;
* Data don't save, list of records is displaying to user.

![Departments mockup](https://ibb.co/fv5jSCY "Add department")
Pic. 1.2 Add department.

When adding a department, the following details are entered:

* Name of department.

### 1.3 Edit department

**Main scenario:**

* User clicks the "Edit" button in the departments list view mode;
* Application displays form to enter department data;
* User enter department data and press "Submit" button;
* If error occurs, then error message is displaying;
* If new record is successfully edited, then list of departments with new record is displaying.

**Cancel operation scenario**

* User clicks the "Edit" button in the departments list view mode;
* Application displays form to enter department data;
* User press "Cancel" button;
* Data don't save, list of records is displaying to user.

![Departments mockup](https://ibb.co/fv5jSCY "Edit department")
Pic. 1.3 Edit department.

When editing a department, the following details are entered:

* Name of department.

Constraints for data validation:

* Name of department - maximum length of 100.

### 1.4 Remove department

**Main scenario:**

* User clicks the "Delete" button in the departments list view mode;
* A confirmation dialog is displayed;
* User confirms the removal of the department;
* Record is deleted from database;
* If error occurs, then error message is displaying;
* If record is successfully deleted, then list of departments without deleted one is displaying.

**Cancel operation scenario**

* User clicks the "Delete" button in the departments list view mode;
* A confirmation dialog is displayed;
* User press "Cancel" button;
* List of departments without changes is displaying.

![Departments mockup](https://ibb.co/CW5z1nS "Delete department")
Pic. 1.4 Delete department.

### 1.5 Department page

#### 1.5.1 Display list of employees

**Main scenario:**

* User clicks the "More" button in the departments list view mode;
* Application displays list of related employees and calculated average salary of them.

![Departments mockup](https://ibb.co/BfYcpvy "Department")
Pic. 1.5 Department page.

The list displays the following columns:

* Name - Employee's name;
* Surname - Employee's surname;
* Birthday - Employee's date of birth;
* Salary - Employee's salary.

#### 1.5.2 Add employee

**Main scenario:**

* User clicks the "+" button in the department view mode;
* Application displays form to enter employee data for current department;
* User enter data and press "Submit" button;
* If error occurs, then error message is displaying;
* If new record is successfully added, then new average salary and list of employees with new record is displaying;

**Cancel operation scenario**

* User clicks the "+" button in the department view mode;
* Application displays form to enter employee data;
* User press "Cancel" button;
* Data don't save, list of records is displaying to user.

![Departments mockup](https://ibb.co/VSJNgHP "Add employee")
Pic. 1.6 Add department.

When adding employee, the following details are entered:

* Name - Employee's name;
* Surname - Employee's surname;
* Date of birth - Employee's date of birth;
* Salary - Employee's salary.

#### 1.5.3 Edit employee

**Main scenario:**

* User clicks the "Edit" button in the department view mode;
* Application displays form to enter employee data for current department;
* User enter data and press "Submit" button;
* If error occurs, then error message is displaying;
* If new record is successfully edited, then new average salary and list of employees with new record is displaying;

**Cancel operation scenario**

* User clicks the "Edit" button in the department view mode;
* Application displays form to enter employee data;
* User press "Cancel" button;
* Data don't save, list of records is displaying to user.

![Departments mockup](https://ibb.co/VSJNgHP "Edit employee")
Pic. 1.7 Edit department.

When editing employee, the following details are entered:

* Name - Employee's name;
* Surname - Employee's surname;
* Date of birth - Employee's date of birth;
* Salary - Employee's salary.

#### 1.5.4 Remove employee

**Main scenario:**

* User clicks the "Delete" button in the department view mode;
* A confirmation dialog is displayed;
* User confirms the removal of the employee;
* Record is deleted from database;
* If error occurs, then error message is displaying;
* If record is successfully deleted, then list of employees without deleted one and new average salary is displaying.

**Cancel operation scenario**

* User clicks the "Delete" button in the department view mode;
* A confirmation dialog is displayed;
* User press "Cancel" button;
* Department page without changes is displaying.

![Departments mockup]( https://ibb.co/93qqgKM "Delete employee")
Pic. 1.8 Delete department.

## 2. Employees

### 2.1 Display list of employees

The mode is designed to view the list of employees that are stored in database.

**Main scenario:**

* User selects item "Employee";
* Application displays list of employees.

![Employee mockup](https://ibb.co/W38krDd "Employees")
Pic. 2.1 View the employees list.

The list displays the following columns:

* Name - Employee's name;
* Surname - Employee's surname;
* Birthday - Employee's date of birth;
* Salary - Employee's salary.

**Filtering by date:**

* In the employees list view mode, the user sets a date filter;
* Application will show employees only for a certain period of time.

Restrictions:

* Start date of the period should be less than end date of the period;
* If start date is blank, then filtering by end date only;
* If end date is blank, then filtering by start date only;

### 2.2 Add employees

**Main scenario:**

* User clicks the "+" button in the employees view mode;
* Application displays form to enter employee data;
* User enter data and press "Submit" button;
* If error occurs, then error message is displaying;
* If new record is successfully added, then list of employees with new record is displaying;

**Cancel operation scenario**

* User clicks the "+" button in the employees view mode;
* Application displays form to enter employee data;
* User press "Cancel" button;
* Data don't save, list of records is displaying to user.

![Employee mockup](https://ibb.co/hBnHWSK "Add employee")
Pic. 2.2 Add employee.

When adding employee, the following details are entered:

* Name - Employee's name;
* Surname - Employee's surname;
* Date of birth - Employee's date of birth;
* Department - Related department from list;
* Salary - Employee's salary.

### 2.3 Edit employees

**Main scenario:**

* User clicks the "Edit" button in the employees view mode;
* Application displays form to enter employee data;
* User enter data and press "Submit" button;
* If error occurs, then error message is displaying;
* If new record is successfully edited, then list of employees with new record is displaying;

**Cancel operation scenario**

* User clicks the "Edit" button in the employees view mode;
* Application displays form to enter employee data;
* User press "Cancel" button;
* Data don't save, list of records is displaying to user.

![Employee mockup](https://ibb.co/hBnHWSK "Edit employee")
Pic. 2.3 Edit employee.

When editing employee, the following details are entered:

* Name - Employee's name;
* Surname - Employee's surname;
* Date of birth - Employee's date of birth;
* Department - Related department from list;
* Salary - Employee's salary.

### 2.4 Remove employees

**Main scenario:**

* User clicks the "Delete" button in the employees list view mode;
* A confirmation dialog is displayed;
* User confirms the removal of the employee;
* Record is deleted from database;
* If error occurs, then error message is displaying;
* If record is successfully deleted, then list of employees without deleted one is displaying.

**Cancel operation scenario**

* User clicks the "Delete" button in the employees list view mode;
* A confirmation dialog is displayed;
* User press "Cancel" button;
* List of employees without changes is displaying.

![Employee mockup](https://ibb.co/WB4rTc2 "Delete employee")
Pic. 2.4 Delete employee.

### 2.5 Employee page

#### 2.5.1 Show employee data

**Main scenario:**

* User clicks the "More" button in the employees list view mode;
* Application displays employee data.

![Employee mockup](https://ibb.co/PTMzZw6 "Employee")
Pic. 2.5 Employee page.

#### 2.5.2 Edit employee

**Main scenario:**

* User clicks the "Edit" button in the employee view mode;
* Application displays form to enter employee data;
* User enter data and press "Submit" button;
* If error occurs, then error message is displaying;
* If new record is successfully edited, then employees with new record is displaying;

**Cancel operation scenario**

* User clicks the "Edit" button in the employee view mode;
* Application displays form to enter employee data;
* User press "Cancel" button;
* Data don't save, list of records is displaying to user.

![Employee mockup](https://ibb.co/J5hxNdP "Edit employee")
Pic. 2.6 Edit employee.

When editing employee, the following details are entered:

* Name - Employee's name;
* Surname - Employee's surname;
* Date of birth - Employee's date of birth;
* Department - Related department from list;
* Salary - Employee's salary.

#### 2.4 Remove employees

**Main scenario:**

* User clicks the "Delete" button in the employee view mode;
* A confirmation dialog is displayed;
* User confirms the removal of the employee;
* Record is deleted from database;
* If error occurs, then error message is displaying;
* If record is successfully deleted, then list of employees without deleted one is displaying.

**Cancel operation scenario**

* User clicks the "Delete" button in the employees list view mode;
* A confirmation dialog is displayed;
* User press "Cancel" button;
* Employee data without changes is displaying.

![Employee mockup](https://ibb.co/PTMzZw6 "Delete employee")
Pic. 2.7 Delete employee.