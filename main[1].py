"""Tyler Spring
Lab 8
This is the second part of the website project, lab 7.
Here the user is prompted to entry a user name and password in the correct format.
Once that is validated the user is granted access to 6 other pages of the website.
This includes a page with images, a table, and a registration form the user can
fill with an email and password, again having it validated.
It also now provides the user to login if they already have an account,
or to update their password, if they already have an account."""
import datetime

import flask as flask
import socket
from datetime import date
from flask import render_template, request, redirect, url_for

hostname = socket.gethostname()
IPAddr = socket.gethostname()
time = datetime.datetime.now()

app = flask.Flask(__name__)


@app.route('/')
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    """
Login method. First prompt to the user when accessing the website.
Allows them to register an account, update a password, or login.
    :rtype: object
    """
    if request.method == 'POST':
        # catches info user inputs to set to username and password
        username = request.form['username']
        password = request.form['password']
        f = open("logs.txt", "a")
        for ind in username.split(" "):
            f.write("%s %s \n" % (username, password))
            f.close()
            return render_template("page1.html", error="registered")
    else:
        # prints the date, time and IP address to fails file
        t = open("fails.txt", "a")
        ip = IPAddr
        t.write(ip)
        t.write(str(time))
        t.close()
        return render_template("login.html")


@app.route('/logger.html', methods=['GET', 'POST'])
def logger():
    """
Logger method for lab 8 is the method that lets the user login if they
alreay have an account.
    :rtype: object
    """
    if request.method == 'POST':
        # opens logs file to validate info inputted for existing account
        f = open("logs.txt", "r")
        logs = f.readlines()
        f.close()
        logs = [x.split() for x in logs]
        for item in logs:
            if request.form['username'] == item[0].strip() \
                    and request.form['password'] == item[1].strip():
                return redirect(url_for('page1'))
            else:
                # prints the date, time and IP address to fails file
                t = open("fails.txt")
                ip = IPAddr
                t.write(ip)
                t.write(str(time))
                t.close()
                error = "incorrect login"
                return render_template("logger.html", error=error)
    else:
        return render_template("logger.html")


@app.route('/page1.html')
def page1():
    """
Page 1 function. Is available after the logger is validated.
Provides links to other pages using the render
template function of the flask class.
    :rtype: object
    """
    return flask.render_template('page1.html', the_title='Page 1')


@app.route('/update.html', methods=['GET', 'POST'])
def update():
    """
This is the method that updates the password of an already
existing account. Can be accessed at a
    :rtype: object
    """
    if request.method == 'POST':
        # reads file of existing info to validate account with username and lets them add password
        f = open("logs.txt")
        logs = f.readlines()
        password = request.form['password']
        q = open("CP")
        shall = q.readlines()
        if password == q:
            # prints the date, time and IP address to fails file
            t = open("fails.txt")
            ip = IPAddr
            t.write(ip)
            t.write(str(time))
            t.close()
            return render_template(update, message="This on the list, please pick a new one.")
        q.close()
        f = open("logs.txt", "a")
        in_name = ""
        for ind in password.split(" "):
            f.write("%s \n" % password)
            f.close()
            return render_template("page1.html")
    else:
        return render_template("update.html")


@app.route('/page2.html')
def page2():
    """
Page 2 function. Is available after the logger is validated.
Provides links to other pages using the render
template function of the flask class.
:return:
    """
    return flask.render_template('page2.html', the_title='Page 2')


@app.route('/page3.html')
def page3():
    """
Page 3 function. Is available after the logger is validated.
Provides links to other pages using the render
template function of the flask class.
    :rtype: object
    """
    return flask.render_template('page3.html', the_title='Page 3')


@app.route('/page4.html')
def page4():
    """
Page 4 function. Is available after the logger is validated.
Provides links to other pages using the render
template function of the flask class.
    :rtype: object
    """
    return flask.render_template('page4.html', date=date.today())


@app.route('/page5.html')
def page5():
    """
Page 5 function. Is available after the logger is validated.
Provides links to other pages using the render
template function of the flask class.
    :rtype: object
    """
    return flask.render_template('page5.html', date=date.today())


@app.route('/page6.html')
def page6():
    """
Page 6 function. Is available after the logger is validated.
Provides links to other pages using the render
template function of the flask class.
    :rtype: object
    """
    return flask.render_template('page6.html', date=date.today())


if __name__ == '__main__':
    app.run(debug=True)
