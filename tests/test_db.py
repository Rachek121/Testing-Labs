import pytest
import sqlite3 as sq

class testing:
    @pytest.fixture
    def db_connection(self):
        conn = sq.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
        conn.commit()
        yield conn
        conn.close()

    def test_add(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES ('Vlad', 55)")
        db_connection.commit()
        cursor.execute("SELECT * FROM users WHERE name='Vlad'")
        result = cursor.fetchone()
        assert result is not None
        assert result[1] == 'Vlad'
        assert result[2] == 55

    def test_change(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES ('Ivan', 40)")
        db_connection.commit()
        cursor.execute("UPDATE users SET age=30 WHERE name='Ivan'")
        db_connection.commit()
        cursor.execute("SELECT age FROM users WHERE name='Ivan'")
        result = cursor.fetchone()
        assert result[0] == 30

    def test_delete(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES ('Maria', 25)")
        db_connection.commit()

        cursor.execute("DELETE FROM users WHERE name='Maria'")
        db_connection.commit()

        cursor.execute("SELECT * FROM users WHERE name='Maria'")
        result = cursor.fetchone()
        assert result is None

    def test_get_all(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES ('John', 30)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('Doe', 40)")
        db_connection.commit()

        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()

        assert len(results) == 2
        assert results[0][1] == 'John'
        assert results[1][1] == 'Doe'
