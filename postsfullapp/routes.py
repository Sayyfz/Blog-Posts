from flask import Flask,render_template,request,url_for, redirect,flash
from postsfullapp.models import User, Post
from postsfullapp.forms import RegistrationForm, LoginForm, UpdateAccountForm
from postsfullapp import app, bcrypt,db
from flask_login import login_user, logout_user , current_user, login_required
import secrets
import os
from PIL import Image


output_size = (125,125) #profile_pic size
posts = [
    {
        'author': 'Ahmed El-Shazly',
        'title': 'Post1',
        'content': 'First Post Content First Post ContenFirst Post ContenFirst Post ContenFirst Post ContenFirst Post ContenFirst Post ContenFirst Post ContenFirst Post ContenFirst Post ContenFirst Post Conten',
        'date_posted': 'April 20, 2017'
    },
    {
        'author': 'Seif Ashraf',
        'title': 'Post2',
        'content': 'Second Post Content',
        'date_posted': 'March 4, 2018'
    } ,
    {
        'author': 'Seif Ashraf',
        'title': 'Post2',
        'content': 'Second Post Content',
        'date_posted': 'March 4, 2018'
    } ,
    {
        'author': 'Seif Ashraf',
        'title': 'Post2',
        'content': 'Second Post Content',
        'date_posted': 'March 4, 2018'
    } ,
    {
        'author': 'Seif Ashraf',
        'title': 'Post2',
        'content': 'Second Post Content',
        'date_posted': 'March 4, 2018'
    } ,
    {
        'author': 'Seif Ashraf',
        'title': 'Post2',
        'content': 'Second Post Content',
        'date_posted': 'March 4, 2018'
    } ,
    {
        'author': 'Seif Ashraf',
        'title': 'Post2',
        'content': 'Second Post Content',
        'date_posted': 'March 4, 2018'
    } ,
    {
        'author': 'Seif Ashraf',
        'title': 'Post2',
        'content': 'Second Post Content',
        'date_posted': 'March 4, 2018'
    } ,
    {
        'author': 'Seif Ashraf',
        'title': 'Post2',
        'content': 'Second Post Content',
        'date_posted': 'March 4, 2018'
    } ,
    {
        'author': 'Seif Ashraf',
        'title': 'Post2',
        'content': 'Second Post Content',
        'date_posted': 'March 4, 2018'
    } ,
    {
        'author': 'Seif Ashraf',
        'title': 'Post2',
        'content': 'Second Post Content',
        'date_posted': 'March 4, 2018'
    } 
    
    
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)



@app.route("/about")
def about():
    return render_template('about.html', title = 'About')




@app.route("/register", methods = ['GET', 'POST'])
def register():
    if(current_user.is_authenticated):
        return redirect(url_for('home'))
    form = RegistrationForm()
    
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, password  = hashed_pw, email = form.email.data)
        db.session.add(user)
        db.session.commit()
        
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',  form = form)



@app.route("/login", methods = ['GET', 'POST'])
def login():
    if(current_user.is_authenticated):
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            flash('You have been logged in!', 'success')
            next_page =  request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
            
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
            
    return render_template('login.html',title='Login',  form = form)


@app.route("/logout", methods = ['GET'])
def logout():
    logout_user()
    return redirect(url_for('home'))
    
    
def save_picture(form_picture):
    random_hex = secrets.token_hex(10)
    _, f_ext = os.path.splitext(form_picture.filename) #split filename from the extension
    picture_fn = random_hex + f_ext 
    picture_path = os.path.join(app.root_path, 'static/profile_pics/', picture_fn)
    
    
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    
    prev_picture = os.path.join(app.root_path, 'static/profile_pics', current_user.image_file)
    if os.path.exists(prev_picture) and os.path.basename(prev_picture) != 'default.jpg':
        os.remove(prev_picture)
    i.save(picture_path)
    return picture_fn
    
@app.route("/account", methods = ['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
            
        
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('account'))
    
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    
    image_file = url_for('static', filename = 'profile_pics/' + current_user.image_file)
    return render_template('account.html', title = 'Account', image_file=image_file, form = form)