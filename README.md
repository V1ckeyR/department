# Department

| Build Status | [![Build Status](https://travis-ci.com/V1ckeyR/department.svg?branch=main)](https://travis-ci.com/V1ckeyR/department) | 
---: | ---:
| **Coverage Status** | [![Coverage Status](https://coveralls.io/repos/github/V1ckeyR/department/badge.svg?branch=main)](https://coveralls.io/github/V1ckeyR/department?branch=main) |

## Description
The simple web application for managing departments and employees. The web application use web service for storing data and reading from database. Created for educational purpose.

### Documentation
https://github.com/V1ckeyR/department/tree/main/documentation

### Built with
* [Flask](http://flask.pocoo.org/)
* [Flask-RESTfull](https://flask-restful.readthedocs.io/en/latest/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [MySQL](https://dev.mysql.com/doc/)

## How to build
1. Clone the repository:
~~~
git clone https://github.com/V1ckeyR/department.git
~~~
2. Make sure you have:
  * Ubuntu
  * [MySQL](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
  * [Gunicorn](https://docs.gunicorn.org/en/stable/install.html#ubuntu)
  * [Nginx](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04])
   
3. Run script from project directory:
~~~
./install.sh
~~~

## How to start
1. Setup [.env](/department-app/.env) with appropriate *db_user* and *db_password*
2. Run:
~~~
 sudo cp webapp/department.service /etc/systemd/system
 sudo systemctl start department.service
 sudo cp webapp/department /etc/nginx/sites-available/department
 sudo systemctl start nginx.service
~~~
3. Visit address

## Address
    127.0.0.1

*Address and domain can be changed in file /etc/nginx/sites-available/department. To apply changes run:*
~~~
sudo systemctl restart nginx.service
~~~
