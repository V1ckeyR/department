"""This module contains view functions that return HTML content of Web page"""

from flask import render_template

from config.logger import logger


def departments(data):
    """Departments page"""
    logger.info('Rendering template "departments.html" with args: %s', data)
    return render_template("departments.html", deps=data)


def department(dep, data, avg):
    """Specific department page"""
    logger.info('Rendering template "departments.html" with args:\n%s\n%s\n%s', dep, data, avg)
    return render_template("department.html", dep=dep, data=data, avg=avg)


def department_add(form):
    """Form for creating new department"""
    logger.info('Rendering template "departments.html" with args: %s', form)
    return render_template("form_add_department.html", form=form)


def department_edit(dep):
    """Form for updating existing department"""
    logger.info('Rendering template "departments.html" with args: %s', dep)
    return render_template("form_edit_department.html", dep=dep)


def employees(args, min_date, max_date, values):
    """Employees page"""
    logger.info('Rendering template "departments.html" with args:\n%s\n%s\n%s\n%s', args, min_date, max_date, values)
    return render_template("employees.html", emps=args, min=min_date, max=max_date, values=values)


def employee(data):
    """Specific employee page"""
    logger.info('Rendering template "departments.html" with args: %s', data)
    return render_template("employee.html", employee=data)


def employee_add(form):
    """Form for creating new employee"""
    logger.info('Rendering template "departments.html" with args: %s', form)
    return render_template("form_add_employee.html", form=form)


def employee_edit(form, emp):
    """Form for updating existing employee"""
    logger.info('Rendering template "departments.html" with args:\n%s\n%s', form, emp)
    return render_template("form_edit_employee.html", form=form, emp=emp)
