from sqlite3 import Error
from connect import create_connection, database


def delete_task(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM tasks WHERE id=?' # Usuń zadanie o podanym id
    cur = conn.cursor()
    try:
        cur.execute(sql, (id,)) # Wykonaj zapytanie SQL z parametrem id w formie krotki
        conn.commit() # Zatwierdź zmiany w bazie danych SQLite
    except Error as e:
        print(e)
    finally:
        cur.close() # Zamknij kursor po zakończeniu operacji

if __name__ == '__main__':
    with create_connection(database) as conn:
        delete_task(conn, 1) # Usuń zadanie o id 1
