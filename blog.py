from flask import Flask,render_template,request
app = Flask(__name__)


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
    } 
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts = posts)

@app.route("/about")
def about():
    return render_template("about.html", title = 'About')

if __name__ == '__main__':
     app.run(debug = True)