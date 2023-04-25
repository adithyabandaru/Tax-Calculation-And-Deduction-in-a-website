from flask import Flask, request, render_template, jsonify
import sqlite3
import json

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['MIME_TYPES'] = {'application/javascript': ['.js']}
app = Flask(__name__, static_url_path='/static')
app = Flask(__name__, static_folder='static')
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Connect to database and check login credentials
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?",
                  (username, password))
        user = c.fetchone()
        conn.close()
        
        # Check if user exists and password matches
        if user:
            return render_template('indexh.html')
        else:
            return 'Invalid Login'
    
    # Render the login page
    return render_template('index.html')
# Route to handle form submission
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Retrieve user data from the request body
        data = json.loads(request.data)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        # Validate that all required keys are present in the request body
        if not all([username, email, password]):
            return 'Please provide all required data'

        # Connect to the database and insert the user data
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        conn.close()
        print(data)

        return 'User created successfully!'
    
    # Render the signup page if the request method is GET
    return render_template('signup.html')


# Route to handle user authentication
@app.route('/authenticate', methods=['POST'])
def authenticate():
    # Retrieve user credentials from the request body
    data = json.loads(request.data)
    username = data.get('username')
    password = data.get('password')

    # Validate that all required keys are present in the request body
    if not all([username, password]):
        return 'Please provide all required data'

    # Connect to the database and retrieve the user with the given username and password
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()

    # If the user exists, return a success response with the user data
    if user:
        return jsonify({'success': True, 'user': {'username': user[0], 'email': user[1]}})
    else:
        # Otherwise, return an error response
        return jsonify({'success': False, 'error': 'Invalid username or password'})
    
@app.route('/indexh')
def indexh():
    return render_template('indexh.html')
@app.route('/entrance')
def entrance():
    return render_template('entrance.html')
@app.route('/job')
def job():
    return render_template('job.html')
@app.route('/abroad')
def abroad():
    return render_template('abroad.html')
@app.route('/indexhome')
def indexhome():
    return render_template('indexhome.html')
@app.route('/indexc')
def indexc():
    return render_template('indexc.html')
@app.route('/indext')
def indext():
    return render_template('indext.html')
if __name__ == '__main__':
    app.run()
