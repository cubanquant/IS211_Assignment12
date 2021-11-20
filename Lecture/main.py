from flask import Flask, session, redirect, url_for, request, render_template, g
import re
import logging
from logging import FileHandler
from db_build import data_distribute
#http://opentechschool.github.io/python-flask/extras/sessions.html


app = Flask(__name__)

email_list = []

#logger stuff
file_handler = FileHandler('/Users/connorhanwick/Desktop/Python/Assignment_sketchpad/flaskpt2/logfile.log')
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

#key for sessions
app.secret_key = '\xbb\xcc\xdbS-\xcb\x99\xc3\xf5\xe7&\x87\xcc\xef\x98\x86\x80[\xcd\xad\x05\xf6\xfd\xd2'

#homepage
@app.route('/')
def index():
    return render_template('index.html', email_list=email_list)

#get some info from the homepage html fields and add it to some data structure stored in the python
@app.route('/email', methods=['GET', 'POST'])
def email():
    email = request.form['email']
    email_list.append(email)
    session['email'] = email
    app.logger.error(f'Email loaded -- {email}')
    return redirect('/')


if __name__ == "__main__":

    app.run(debug=True)

