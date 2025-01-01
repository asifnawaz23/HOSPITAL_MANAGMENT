from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/register')
def register():
    return render_template('register.html')
    

if __name__ == '__main__':
    app.run(debug=True)
