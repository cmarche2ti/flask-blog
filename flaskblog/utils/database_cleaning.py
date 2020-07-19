import sqlite3


def deleteSqliteRecords():
    try:
        sqliteConnection = sqlite3.connect("site.db")
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_post = """DELETE from post where user_id != ?"""
        cursor.execute(sql_update_post, (3,))
        sql_update_user = """DELETE from user where id != ?"""
        cursor.execute(sql_update_user, (3,))
        sqliteConnection.commit()
        print("Record(s) deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete record from a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")


deleteSqliteRecords()
