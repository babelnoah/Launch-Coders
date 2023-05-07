from flask import *
from database import init_db, db_session
from models import *

app = Flask(__name__)

# Epic Secret key for session
app.secret_key = "Noah is Awesome"

# Routes and methods

# Route for the home page
@app.route('/home')
def home():
     return render_template('home.html')

# Route for the calendar page
@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

# Route for the login page and handling login requests
@app.route("/")
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['username'] = user.username
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

# Route for the signup page and handling signup requests
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists')
        else:
            new_user = User(username=username, password=password)
            db_session.add(new_user)
            db_session.commit()
            session['username'] = new_user.username
            return redirect(url_for('home'))
    return render_template('login.html')

# Route for handling logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

#main
if __name__ == "__main__":
    init_db()
    app.run(debug=True)