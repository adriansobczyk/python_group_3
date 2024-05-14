import psycopg2

def connect_to_postgres(host, port, database, user):
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user
        )
        print("Connected to PostgreSQL database!")

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Example: Execute a SQL query
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("PostgreSQL database version:", db_version)

        # Close the cursor and connection
        cursor.close()
        conn.close()
        print("Connection to PostgreSQL database closed.")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL database:", error)

# Usage example
if __name__ == "__main__":
    # Update these values with your PostgreSQL Docker container details
    host = "localhost"
    port = "5432"
    database = "postgres"
    user = "postgres"

    # Call the function to connect to PostgreSQL
    connect_to_postgres(host, port, database, user)
