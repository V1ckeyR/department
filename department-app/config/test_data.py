"""Test data for DB"""
from datetime import datetime

departments_data = ['HUMAN RESOURCE', 'SALES', 'PRODUCTION', 'INFORMATION AND TECHNOLOGY SUPPORT',
                    'MARKETING', 'RESEARCH AND DEVELOPMENT', 'ADMINISTRATIVE AND MANAGEMENT']

employees_data = [('Myrtle', 'Conley', 7, datetime.strptime('1999-10-01', '%Y-%m-%d').date(), 1000),
                  ('George', 'Guerra', 1, datetime.strptime('1998-11-05', '%Y-%m-%d').date(), 5000),
                  ('Elliot', 'Rivers', 2, datetime.strptime('2000-01-01', '%Y-%m-%d').date(), 900),
                  ('Caitlin', 'Ashton', 3, datetime.strptime('2000-04-07', '%Y-%m-%d').date(), 500),
                  ('Rosa', 'McGhee', 4, datetime.strptime('1998-08-09', '%Y-%m-%d').date(), 1000),
                  ('Markus', 'Walker', 5, datetime.strptime('1997-06-04', '%Y-%m-%d').date(), 500),
                  ('Ishaan', 'Gregory', 6, datetime.strptime('1994-02-02', '%Y-%m-%d').date(), 1100),
                  ('Liana', 'Cantrell', 7, datetime.strptime('1999-09-09', '%Y-%m-%d').date(), 1000),
                  ('Lilia', 'Raymond', 1, datetime.strptime('1998-05-05', '%Y-%m-%d').date(), 600),
                  ('Sonia', 'Forbes', 2, datetime.strptime('2000-08-05', '%Y-%m-%d').date(), 800),
                  ('Isabell', 'Zimmerman', 3, datetime.strptime('2000-04-04', '%Y-%m-%d').date(), 900),
                  ('Charlie', 'Freenet', 4, datetime.strptime('1989-07-07', '%Y-%m-%d').date(), 500),
                  ('Marie', 'Collins', 5, datetime.strptime('1999-10-01', '%Y-%m-%d').date(), 1000),
                  ('Rea', 'Hurst', 6, datetime.strptime('1988-06-05', '%Y-%m-%d').date(), 540),
                  ('Murray', 'Workman', 7, datetime.strptime('1984-01-25', '%Y-%m-%d').date(), 500),
                  ('Nicola', 'Mcgregor', 1, datetime.strptime('1995-04-01', '%Y-%m-%d').date(), 700),
                  ('Ursula', 'Powell', 2, datetime.strptime('1986-11-11', '%Y-%m-%d').date(), 600),
                  ('Andrew', 'Velasquez', 3, datetime.strptime('1985-02-03', '%Y-%m-%d').date(), 800),
                  ('Blaine', 'Richmond', 4, datetime.strptime('1985-10-28', '%Y-%m-%d').date(), 1400),
                  ('Hal', 'Prince', 5, datetime.strptime('1995-04-03', '%Y-%m-%d').date(), 900),
                  ('Calvin', 'Samuele', 6, datetime.strptime('1982-12-24', '%Y-%m-%d').date(), 1300),
                  ('Dominick', 'Quintana', 7, datetime.strptime('2000-09-08', '%Y-%m-%d').date(), 700)]
