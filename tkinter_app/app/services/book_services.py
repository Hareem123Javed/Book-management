import mysql.connector

# Update with your database connection details
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",        # Put your MySQL password if any
        database="library",
        port=3307
    )

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            Title VARCHAR(255),
            Author VARCHAR(255),
            ISBN VARCHAR(50),
            Year INT
        )
    """)
    conn.commit()
    conn.close()

def add_book(title, author, isbn, year):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO books (Title, Author, ISBN, Year) VALUES (%s, %s, %s, %s)"
    values = (title, author, isbn, year)
    cursor.execute(query, values)
    conn.commit()
    conn.close()

def delete_book(title, author, isbn, year):
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM books WHERE Title = %s AND Author = %s AND ISBN = %s AND Year = %s LIMIT 1"
        values = (title, author, isbn, year)
        cursor.execute(query, values)
        conn.commit()
        conn.close()


def get_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Title, Author, ISBN, Year FROM books")
    books = cursor.fetchall()
    conn.close()
    return books

def update_book(old_title, old_author, old_isbn, old_year, new_title, new_author, new_isbn, new_year):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        UPDATE books
        SET Title = %s, Author = %s, ISBN = %s, Year = %s
        WHERE Title = %s AND Author = %s AND ISBN = %s AND Year = %s
    """
    values = (new_title, new_author, new_isbn, new_year, old_title, old_author, old_isbn, old_year)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
