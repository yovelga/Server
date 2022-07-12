from flask import Flask, redirect, render_template
from flask import url_for
from datetime import timedelta
from flask import request, session, jsonify
import requests
import mysql.connector
import time


app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.config['SESSION_PERMANENT'] = True
app.config['permanent_session_lifetime'] = timedelta(minutes=20)


##assignment4
from pages.assignment4.assignment4 import assignment4
app.register_blueprint(assignment4)


user_dict = {
    'user1': {'name': 'Yovelg', 'password': '1231', 'email': 'Yovelgani1@gmail.com',
              'PhoneNumber': '0548189817'},
    'user2': {'name': 'or', 'password': '1231', 'email': 'or@gmail.com',
              'PhoneNumber': '0511111111'},
    'user3': {'name': 'yossi', 'password': '1231', 'email': 'yossi@gmail.com',
              'PhoneNumber': '0522222222'},
    'user4': {'name': 'moshe', 'password': '1231', 'email': 'moshe@gmail.com',
              'PhoneNumber': '0533333333'},
    'user5': {'name': 'tamir', 'password': '1231', 'email': 'tamir@gmail.com',
              'PhoneNumber': '0544444444'}

}

catalog_dict = {
    'Book1': 'yovelg',
    'Book2': 'or',
    'Book3': 'tamir',
    'Book4': 'yovelg',
    'Book5': 'yossi',
}


@app.route('/assignment3_1')
def catalog_func():
    if 'product_name' in request.args:
        # The use of filters is reflected in this -- You can search in both upper and lower letters
        # And the result will always be displayed in capital letters
        product_name = request.args['product_name'].lower()
        # product_color = request.args['product_color'].lower()
        # product_size = request.args['product_size'].lower()
        print(product_name)
        if product_name == '':
            return render_template('assignment3_1.html',
                                   catalog_dict=catalog_dict)

        for k, v in catalog_dict.items():
            product_cotactName = v.upper()
            print(product_name)
            print(k.lower())
            print(5)

            if k.lower() == product_name:
                return render_template('assignment3_1.html',
                                       product_name=product_name,
                                       product_cotactName=product_cotactName, )

        else:
            return render_template('assignment3_1.html',
                                   message='Product not found.')

    return render_template('assignment3_1.html',
                           # catalog_dict=catalog_dict
                           )


@app.route('/contact')
def contact_page():
    return render_template('Contact.HTML')


@app.route('/fetch_backend')
def fetch_backend():
    return render_template('fetch_backend.HTML')

usersDetail = list(user_dict.values())

emails = []
for i in range(len(usersDetail)):
    userEmail = usersDetail[i]['email'].lower()
    emails.append(userEmail)
    print(userEmail)


def index_by_email(email):
    for i in range(len(emails)):
        if emails[i] == email:
            return i


@app.route('/log_in', methods=['GET', 'POST'])
def login_func():
    if request.method == 'POST':
        user_mail = request.form['Email'].lower()
        password = request.form['password']
        if user_mail == '':
            return render_template('log_in.html',
                                   user_dict=user_dict)
        if user_mail in emails:
            Index = index_by_email(user_mail)
            user_password = usersDetail[Index]['password']
            if user_password == password:
                username = usersDetail[Index]['name']
                PhoneNumber = usersDetail[Index]['PhoneNumber']
                email = usersDetail[Index]['email']
                session['PhoneNumber'] = PhoneNumber
                session['email'] = email
                session['name'] = username
                session['logedin'] = True
                return render_template('log_in.html',
                                       message='Success')
            else:
                return render_template('log_in.html',
                                       message='Wrong Password!')
        else:
            return render_template('log_in.html',
                                   message='Wrong Email!')

    return redirect(url_for('logout_func'))


@app.route('/log_out')
def logout_func():
    session['logedin'] = False
    return render_template('log_in.html')


usersDetail = list(user_dict.values())

names = []
for i in range(len(usersDetail)):
    userName = usersDetail[i]['name'].lower()
    names.append(userName)
    print(userName)


def index_by_userName(name):
    for i in range(len(names)):
        if names[i] == name:
            return i


@app.route('/assignment3_2')
def assignment3_2():
    if request.method == 'GET':
        if 'Username' in request.args:
            Username = request.args['Username'].lower()
            print(Username)
            if Username == '':
                print("hey '' ")
                return render_template('assignment3_2.html', user_dict=user_dict)
            if Username in names:
                print("found a name")
                IndexName = index_by_userName(Username)
                print(IndexName)
                username = usersDetail[IndexName]['name']
                email = usersDetail[IndexName]['email']
                PhoneNumber = usersDetail[IndexName]['PhoneNumber']
                return render_template('assignment3_2.html', username=username, email=email, phone_number=PhoneNumber)

            else:
                print("Wrong Name!")
                return render_template('assignment3_2.html',
                                       message='Wrong Name!')
        else:
            print("Wrong Name2!")
            return render_template('assignment3_2.html', )
    print("12313")
    return render_template('assignment3_2.html',
                           user_dict=user_dict)


@app.route('/')
@app.route('/home')
def index_func():
    return render_template('home.HTML')




if __name__ == '__main__':
    app.run()






