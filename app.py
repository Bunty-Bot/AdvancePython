from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.update(
    MySQL_HOST = 'localhost',
    MySQL_USER = 'root',
    MySQL_PASSWORD = 'root123',
    MySQL_DB = 'disease_management'
)

mysql = MySQL(app)

@app.route('/')
def index():
    return '<h1>Disease Management</h1><a href="/conditions">Conditions</a> | <a href="/patients">Patients</a>'

@app.route('/conditions')
def conditions():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM medical_conditions')
    return render_template('condition.html', data=cursor.fetchall())

@app.route('/add_condition', methods = ['POST'])
def add_condition():
    cursor = mysql.connection.cursor
    cursor.execute('INSERT INTO medical_conditions (name, symptoms, description) VALUES (%s, %s, %s)',
                   (request.form['name'], request.form['symptoms'], request.form['description']))
    mysql.connection.commit()
    return redirect('/conditions')

@app.route('/patients')
def patients():
    cursor = mysql.connection.cursor
    cursor.execute('SELECT patients.name, age, gender, medical_conditions.name'
                   'FROM patients LEFT JOIN medical_conditions ON patients.condition_id = medical_conditions.id')
    return render_template('patients.html', data=cursor.fetchall())

@app.route('/add_patient', methods=['POST'])
def add_patient():
    cursor = mysql.connection.cursor
    cursor.execute('INSERT INTO medical_conditions (name, age, gender, condition_id) VALUES (%s, %s, %s, %s)',
                   (request.form['name'], request.form['age'], request.form['gender'], request.form['condition_id']))
    mysql.connection.commit()
    return redirect('/patients')

if __name__ == '__main__':
    app.run(debug=True)