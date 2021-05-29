from flask import render_template


def departments(data):
    return render_template("departments.html", deps=data)


def department(dep, data, avg):
    return render_template("department.html", dep=dep, data=data, avg=avg)


def department_add(form):
    return render_template("form_add_department.html", form=form)


def department_edit(dep):
    return render_template("form_edit_department.html", dep=dep)


def employees(args, min_date, max_date, values):
    return render_template("employees.html", emps=args, min=min_date, max=max_date, values=values)


def employee(data):
    return render_template("employee.html", employee=data)


def employee_add(form):
    return render_template("form_add_employee.html", form=form)


def employee_edit(form, emp):
    return render_template("form_edit_employee.html", form=form, emp=emp)
