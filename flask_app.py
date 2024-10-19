from flask import Flask, redirect, url_for
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('htop'))

@app.route('/htop')
def htop():
    name = "Sandeep Raveendra Kolli"
    try:
        username = os.getlogin()
    except Exception:
        username = os.getenv('USER', 'unknown')
    
    tz = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S %Z')
    
    try:
        top_output = subprocess.getoutput('top -bn1')
    except Exception as e:
        top_output = f"Error executing 'top': {e}"
    
    return f"""
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <h2>Top Output</h2>
    <pre>{top_output} : </pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
