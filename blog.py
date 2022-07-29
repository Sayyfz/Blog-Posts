from flask import Flask, flash,redirect
from flask import Flask,render_template,request,url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'cffd88e7a1063b2a76e356cc59551da0'

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',  form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
            
    return render_template('login.html',title='Login',  form = form)


if __name__ == '__main__':
     app.run(debug = True)