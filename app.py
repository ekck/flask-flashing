from flask import Flask, render_template, redirect, url_for, flash, request

app = Flask(__name__)
app.secret_key = b'secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        flash('You were successfully logged in', 'info')
        return redirect(url_for('index'))
    return render_template('login.html', error=error)