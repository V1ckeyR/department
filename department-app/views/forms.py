from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, InputRequired


class DepartmentForm(FlaskForm):
    name = StringField("Name of department:", validators=[DataRequired()])
    submit = SubmitField("Submit")


class EmployeeForm(FlaskForm):
    name = StringField("Name:", validators=[DataRequired()])
    surname = StringField("Surname:", validators=[DataRequired()])
    date = DateField("Date of birth:", format='%Y-%m-%d', validators=[DataRequired()])
    department = SelectField("Department:", validators=[InputRequired()])
    salary = IntegerField("Salary:", validators=[DataRequired()])
    submit = SubmitField("Submit")
