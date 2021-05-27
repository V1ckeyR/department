from flask import render_template
from models import model
from rest.app import app


def departments(data):
    return render_template("departments.html", deps=data)


def department(dep, data, avg):
    return render_template("department.html", dep=dep, data=data, avg=avg)


def department_add(form):
    return render_template("form_add_department.html", form=form)


def department_edit(dep):
    return render_template("form_edit_department.html", dep=dep)


@app.route('/employees')
def employees():
    return render_template("employees.html", emps=model.Employee.query.all())
