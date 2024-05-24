from flask import Flask, request
from flask import render_template, redirect, url_for, send_from_directory
import otpGenerator
import os
import sqlite
app = Flask(__name__)

@app.route('/<username>')
def welcome(username):
    with open('./secret_keys/' + username + '_secret_key.txt', 'r') as f:
        lines = f.readlines()
    return render_template('otpgenerator.html', otp=otpGenerator.totp(lines[0]))
    
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')









