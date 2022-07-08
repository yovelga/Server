import requests
from flask import render_template, redirect, url_for
from flask import Blueprint, request, session, jsonify, json
from utilities.db_manager import interact_db

assignment4 = Blueprint('assignment4', __name__,
                        static_folder='static',
                        static_url_path='/assignment4',
                        template_folder='templates')


#routes
@assignment4.route('/assignment4')
def assignment4_page():
    session['searched_user'] = ''
    return render_template('assignment4.html')




@assignment4.route('/assignment4/outer_source')
def outer_source_func():
    session['searched_user'] = ''
    return render_template('assignment4_outer_source.html')






#-------------------------------------------------------------------------------------------------------part a
#Insert User
@assignment4.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
         session['INSERTED'] = True
         session['DELETED'] = False
         session['UPDATE'] = False
         name = request.form['name']
         email = request.form['email']
         password = request.form['password']
         phone_number = request.form['phone_number']
         query = "select email from users"
         emails_list = interact_db(query, query_type='fetch')
         emails = []
         for user in emails_list:
             emails.append(user.email)

         # Enforcements
         if name == "" or email == "" or password == "" or phone_number == "":
             session['insert_message'] = "Please fill all details"

         elif email in emails:
             session['insert_message'] = "This email is already exist"

         elif len(password) < 8:
             session['insert_message'] = "Insertion Warning: Password must contain at least 8 characters"

         elif len(phone_number) != 10:
             session['insert_message'] = "Insertion Warning:  Phone number must contain  10 numbers"

             # create user
         else:
             query = "INSERT INTO users(name, email, password, phone_number) VALUES ('%s', '%s', '%s', '%s')" % (
             name, email, password, phone_number)
             interact_db(query=query, query_type='commit')
             session['insert_message'] = "User Inserted Successfully!"

         return redirect('/assignment4')

#------------- Delete User ---------------
@assignment4.route('/delete_user', methods=['POST'])
def delete_user():
    session['INSERTED'] = False
    session['DELETED'] = True
    session['UPDATE'] = False
    email = request.form['email']

    #email not provided
    if email == "":
        session['delete_message'] = "No email for deletion was provided"

    #email provided
    else:
        # get emails list to check if exists
        query = "select email from users"
        emails_list = interact_db(query, query_type='fetch')
        emails = []

        for user in emails_list:
            emails.append(user.email)

        # user exists
        if email in emails:
            query = "delete  from users where email='%s';" % email
            interact_db(query, query_type='commit')
            session['delete_message'] = "User Deleted Successfully!"


        # no such user
        else:
            session['delete_message'] = "There is no such user with this email"

    return redirect('/assignment4')


#Update User
@assignment4.route('/update_user', methods=['POST'])
def update_user():
    session['INSERTED'] = False
    session['DELETED'] = False
    session['UPDATE'] = True
    email_to_update = request.form['email_to_update']
    username = request.form['username']
    # email = request.form['email']
    password = request.form['password']
    phone_number = request.form['phone_number']

    #check if exist by email
    emails_query = "select email from users"
    emails_list = interact_db(emails_query, query_type='fetch')
    emails = []
    for user in emails_list:
        emails.append(user.email)


    #email field is empty
    if email_to_update == "":
        session['update_message'] = "No user email was provided "


    #can't find user by email
    elif email_to_update not in emails:
        session['update_message'] = " There is no such email"


    #Update only the appropriate fields
    else:
        if username != "":
            query = "update users set name='%s' where email='%s';" % (username, email_to_update)
            interact_db(query, query_type='commit')

        if phone_number != "":
            query = "update users set phone_number='%s' where email='%s';" % (phone_number, email_to_update)
            interact_db(query, query_type='commit')

        if password != "":
            query = "update users set password='%s' where email='%s';" % (password, email_to_update)
            interact_db(query, query_type='commit')

        session['update_message'] = "User Updated Successfully!"
    return redirect('/assignment4')




#  All Users ---------------------------------------------------------------------------------------------------------
@assignment4.route('/select_users')
def select_users():
    query = "select * from users"
    users_list = interact_db(query, query_type='fetch')
    return render_template('assignment4.html', users=users_list)






# USERS
@assignment4.route('/assignment4/users')
def get_users_in_json():
    query = "select * from users"
    users_list = interact_db(query, query_type='fetch')
    users_dict = {}
    for user in users_list:
        user_dict = {}
        user_id = user.id
        user_dict['email'] = user.email
        user_dict['username'] = user.name
        user_dict['password'] = user.password
        user_dict['phone_number'] = user.phone_number
        users_dict[user_id] = user_dict
    return jsonify(users_dict)

# Part B----------------------------------------------------------------------------------------------------------------
#-Back-End

@assignment4.route('/fetch_be')
def fetch_be_func():
    session['searched_user'] = ''

    if 'type' in request.args:
        id = int(request.args['user_num_fetch_be'])
        users = []
        user_to_save = []

        if request.args['type'] == 'sync':
            res = requests.get(f'https://reqres.in/api/users')
            users_data = res.json()
            users.append(users_data['data'])
        for user in users[0]:
            if user['id'] == id:
                users_dict = {
                    'first_name': user['first_name'],
                    'last_name': user['last_name'],
                    'email': user['email'],
                    'avatar': user['avatar']
                }
                user_to_save.append(users_dict)
                print(users_dict)
        session['searched_user'] = user_to_save

    else:
        session['searched_user'] = ''
    return render_template('assignment4_outer_source.html')








# Part C


@assignment4.route('/assignment4/restapi_users/', defaults={'id': 1})
@assignment4.route('/assignment4/restapi_users/<int:id>')
def get_users_restapi_func(id):
    query = 'select * from users where id=%s;' % id
    users = interact_db(query=query, query_type='fetch')
    if len(users) == 0:
        return_dict = {
            'message': f'user {id} not found'
        }
    else:
        return_dict = {
            'status': 'success',
            'id': users[0].id,
            'name': users[0].name,
            'email': users[0].email,
            'password': users[0].password
        }
    return jsonify(return_dict)
