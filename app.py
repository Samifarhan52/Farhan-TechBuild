import os

from flask import Flask, render_template, request, redirect, session, url_for

from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = "farhan_secret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# USER MODEL

class User(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    fullname = db.Column(
        db.String(200),
        nullable=False
    )

    email = db.Column(
        db.String(200),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(300),
        nullable=False
    )



# EMPLOYEE MODEL

class Employee(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(200),
        nullable=False
    )

    role = db.Column(
        db.String(200),
        nullable=False
    )

    email = db.Column(
        db.String(200),
        nullable=False
    )

# CONTACT MODEL

class Contact(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(200)
    )

    email = db.Column(
        db.String(200)
    )

    message = db.Column(
        db.Text
    )

# CREATE DATABASE

with app.app_context():

    db.create_all()

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(200)
    )

    email = db.Column(
        db.String(200)
    )

    message = db.Column(
        db.Text
    )   

# HOME

@app.route('/')
def home():

    return render_template('index.html')

# PROJECTS

@app.route('/projects')
def projects():

    return render_template('projects.html')

# APPS

@app.route('/calculator')
def calculator():

    return render_template('calculator.html')

@app.route('/stopwatch')
def stopwatch():

    return render_template('stopwatch.html')

@app.route('/todo')
def todo():

    return render_template('todo.html')

@app.route('/tictactoe')
def tictactoe():

    return render_template('tictactoe.html')

@app.route('/weather')
def weather():

    return render_template('weather.html')

@app.route('/qrscanner')
def qrscanner():

    return render_template('qrscanner.html')

@app.route('/contact', methods=['GET','POST'])
def contact():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        whatsapp_message = (
            f"New Portfolio Client Message%0A"
            f"Name: {name}%0A"
            f"Email: {email}%0A"
            f"Message: {message}"
        )

        return redirect(
            f"https://wa.me/917676808068?text={whatsapp_message}"
        )

    return render_template('contact.html')

# FILE UPLOAD

@app.route('/upload', methods=['GET','POST'])
def upload():

    if request.method == 'POST':

        file = request.files['file']

        if file:

            filename = secure_filename(file.filename)

            file.save(
                os.path.join(
                    app.config['UPLOAD_FOLDER'],
                    filename
                )
            )

            return "File Uploaded Successfully"

    return render_template('upload.html')

  # VIEW MESSAGES

@app.route('/messages')
def messages():

    if 'user' not in session:

        return redirect('/login')

    all_messages = Contact.query.all()

    return render_template(
        'messages.html',
        messages=all_messages
    )  
# ADMIN PANEL

@app.route('/admin')
def admin():

    if 'user' not in session:

        return redirect('/login')

    return render_template(
        'admin.html',
        user=session['user']
    )

# EMPLOYEE MANAGEMENT

@app.route('/employees', methods=['GET','POST'])
def employees():

    if request.method == 'POST':

        name = request.form['name']

        role = request.form['role']

        email = request.form['email']

        employee = Employee(

            name=name,
            role=role,
            email=email
        )

        db.session.add(employee)

        db.session.commit()

    all_employees = Employee.query.all()

    return render_template(
        'employees.html',
        employees=all_employees
    )

    # DELETE EMPLOYEE

@app.route('/delete_employee/<int:id>')
def delete_employee(id):

    employee = Employee.query.get(id)

    db.session.delete(employee)

    db.session.commit()

    return redirect('/employees')

# STORE PAGE

@app.route('/store')
def store():

    return render_template('store.html')

# SOCIAL PLATFORM

@app.route('/social')
def social():

    return render_template('social.html')

# PROFILE PAGE

@app.route('/profile')
def profile():

    if 'user' not in session:

        return redirect('/login')

    return render_template(
        'profile.html',
        user=session['user']
    )

# CHAT PAGE

@app.route('/chat')
def chat():

    return render_template('chat.html')

# REGISTER

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        fullname = request.form.get('fullname')

        email = request.form.get('email')

        password = request.form.get('password')

        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:

            return "Email already exists"

        hashed_password = generate_password_hash(password)

        new_user = User(

            fullname=fullname,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)

        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')

# LOGIN

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')

        password = request.form.get('password')

        user = User.query.filter_by(
            email=email
        ).first()

        if user and check_password_hash(
            user.password,
            password
        ):

            session['user'] = user.fullname

            return redirect(url_for('dashboard'))

        else:

            return "Invalid email or password"

    return render_template('login.html')

# DASHBOARD

@app.route('/dashboard')
def dashboard():

    if 'user' not in session:

        return redirect(url_for('login'))

    return render_template(
        'dashboard.html',
        user=session['user']
    )

# LOGOUT

@app.route('/logout')
def logout():

    session.pop('user', None)

    return redirect(url_for('home'))

# RUN

if __name__ == '__main__':

    app.run(debug=True)