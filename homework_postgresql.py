import psycopg2

def connect_db():
    return psycopg2.connect(
        dbname="students_db",
        user="postgres",
        password="0000",
        host="localhost",
        port="5432"
    )

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            course_number INT,
            age INT
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

def add_student(first_name, last_name, course_number, age):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (first_name, last_name, course_number, age) VALUES (%s, %s, %s, %s)",
                   (first_name, last_name, course_number, age))
    conn.commit()
    cursor.close()
    conn.close()

def update_student(student_id, first_name, last_name, course_number, age):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET first_name=%s, last_name=%s, course_number=%s, age=%s WHERE id=%s",
                   (first_name, last_name, course_number, age, student_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    cursor.close()
    conn.close()

def read_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return students

def main():

    create_table()

    while True:
        print("\n1. Добавить студента")
        print("2. Изменить студента")
        print("3. Удалить студента")
        print("4. Показать всех студентов")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            first_name = input("Имя: ")
            last_name = input("Фамилия: ")
            course_number = int(input("Номер курса: "))
            age = int(input("Возраст: "))
            add_student(first_name, last_name, course_number, age)
            print("Студент добавлен.")

        elif choice == '2':
            student_id = int(input("ID студента для изменения: "))
            first_name = input("Новое имя: ")
            last_name = input("Новая фамилия: ")
            course_number = int(input("Новый номер курса: "))
            age = int(input("Новый возраст: "))
            update_student(student_id, first_name, last_name, course_number, age)
            print("Данные студента обновлены.")

        elif choice == '3':
            student_id = int(input("ID студента для удаления: "))
            delete_student(student_id)
            print("Студент удален.")

        elif choice == '4':
            students = read_students()
            for student in students:
                print(f"ID: {student[0]}, Имя: {student[1]}, Фамилия: {student[2]}, Номер курса: {student[3]}, Возраст: {student[4]}")

        elif choice == '5':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
