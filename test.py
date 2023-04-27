from flask import Flask, render_template, url_for, flash, redirect
from form import Signup, Login, Home
from database import User

app = Flask(__name__)
app.config['SECRET_KEY'] = '9b697d95843954dbe028a70b2e4f7111' #help protect cookie attacks 

user_database = []

@app.route("/")
def home():
    form = Home()
    return render_template('home.html', form=form)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = Signup()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        user_database.append(user)
        #print(user_database)
        flash(f"Accout created for {form.username.data}", "success")
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route("/login")
def login():
    form = Login()
    if form.validate_on_submit():
        for user in user_database:
            if form.username.data == user.username and form.password.data == user.password:
                return redirect(url_for('home')) 
    return render_template('login.html', form=form)

@app.route("/results")
def results():
    return "<p>results!</p>"

@app.route("/account")
def account():
    return "<p>account</p>"

if __name__ == '__main__':
    app.run(debug=True)
