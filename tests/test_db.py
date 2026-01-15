from db.mysql_connection import get_connection

def test_db_connection():
    conn = get_connection()
    assert conn.is_connected()
