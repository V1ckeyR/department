from views.app import db


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    employees = db.relationship('Employee', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Department id: {}, name: {}'.format(self.id, self.name)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    department = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Integer, nullable=False)

    def __init__(self, data):
        self.name, self.surname, self.department, self.date_of_birth, self.salary = data

    def __repr__(self):
        return 'Employee id: {}, name: {}, surname: {}, date: {}, salary: {}'.format(self.id, self.name, self.surname,
                                                                                     self.date_of_birth, self.salary)


db.create_all()
