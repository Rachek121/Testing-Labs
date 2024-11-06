import pytest
import sqlite3
import os
import tempfile

@pytest.fixture(scope="function")
def db_connection():
    db_file = tempfile.NamedTemporaryFile(delete=True).name
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id_order INTEGER PRIMARY KEY,
        type_of_work TEXT,
        description TEXT,
        acceptance_date TEXT,
        customer TEXT,
        executor TEXT,
        status TEXT
    )
    ''')
    connection.commit()

    yield connection

    connection.close()


