from flask import render_template
from models import model


def departments():
    return render_template("departments.html", deps=model.Department.query.all())


def employees():
    return render_template("employees.html", emps=model.Employee.query.all())
