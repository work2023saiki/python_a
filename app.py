import os
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('ボス猫.html')

@app.route('/puzzle') 
def puzzle15():
    return render_template('15puzzle.html')

@app.route('/saturnvoyager') 
def saturnvoyager():
    return render_template('saturnvoyager.html')

if __name__ == '__main__':
    app.run()