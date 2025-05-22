import mysql.connector

def lend_book(member_id, isbn, date_borrowed, due_date):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="library",
            port=3307
        )
        cursor = db.cursor()

        insert_query = """
            INSERT INTO lending_records (member_id, isbn, date_borrowed, due_date)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (member_id, isbn, date_borrowed, due_date))
        db.commit()
        db.close()

        return True, f"Book ISBN {isbn} lent to Member ID {member_id} on {date_borrowed}. Due on {due_date}."

    except mysql.connector.Error as err:
        return False, f"Error: {err}"
