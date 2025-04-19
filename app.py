from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)
DATABASE = 'database/students.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                faculty TEXT NOT NULL
            )
        ''')
        conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students', methods=['POST'])
def register_student():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    faculty = data.get('faculty')

    if not name or not email or not faculty:
        return jsonify({'error': 'All fields are required'}), 400

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO students (name, email, faculty)
                VALUES (?, ?, ?)
            ''', (name, email, faculty))
            conn.commit()
        return jsonify({'message': 'Student registered successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Email already exists'}), 400

@app.route('/students', methods=['GET'])
def get_students():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, email, faculty FROM students')
        students = cursor.fetchall()
    if not students:
        return jsonify({'message': 'No students found'}), 404
    students = [{'id': student[0], 'name': student[1], 'email': student[2], 'faculty': student[3]} for student in students]
    print(f"Students list: {len(students)} students found")
    return jsonify(students), 200

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, email, faculty FROM students WHERE id = ?', (student_id,))
        student = cursor.fetchone()
    if student:
        print(f"Student found: {student}")
        student = {
            'id': student[0],
            'name': student[1],
            'email': student[2],
            'faculty': student[3]
        }
        return jsonify(student), 200
    else:
        return jsonify({'error': 'Student not found'}), 404

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        faculty = request.form['faculty']
        try:
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO students (name, email, faculty)
                    VALUES (?, ?, ?)
                ''', (name, email, faculty))
                conn.commit()
                print(f"Student {name} added successfully")
            return render_template('students_list.html', message='Student registered successfully')
        except sqlite3.IntegrityError:

            print(f"Error: Email {email} already exists")
            print(f"Student {name} not added")
            return render_template('add_student.html', error='Email already exists')
    return render_template('add_student.html')

@app.route('/students_list', methods=['GET'])
def students_list():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, email, faculty FROM students')
        students = cursor.fetchall()
        print(f"Students list: {len(students)} students found")
    if not students:
        print("No students found")
        return render_template('students_list.html', message='No students found')
    print(f"Students list avec lum: {students}")
    students = [{'id': student[0], 'name': student[1], 'email': student[2], 'faculty': student[3]} for student in students]
    return render_template('students_list.html', etudiant=students)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)