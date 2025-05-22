import mysql.connector

def process_book_return(member_id, isbn):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="library",
            port=3307
        )
        cursor = connection.cursor()

        # Fetch due date
        cursor.execute(
            "SELECT due_date FROM lending_records WHERE member_id = %s AND ISBN = %s ORDER BY due_date DESC LIMIT 1",
            (member_id, isbn)
        )
        result = cursor.fetchone()

        if result:
            due_date = result[0].strftime('%Y-%m-%d')

            # Delete record
            cursor.execute(
                "DELETE FROM lending_records WHERE member_id = %s AND ISBN = %s",
                (member_id, isbn)
            )
            connection.commit()

            return True, "Book returned successfully.", due_date
        else:
            return False, "No lending record found for this Member ID and ISBN.", None

    except mysql.connector.Error as err:
        return False, f"Database error: {err}", None

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
