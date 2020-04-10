from flask import render_template, send_from_directory
from app import app
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/images/<path:filename>')
def custom_static(filename):
    return send_from_directory('images', filename)

