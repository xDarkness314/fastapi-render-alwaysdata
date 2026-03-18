from typing import Optional

import psycopg2
from psycopg2.extensions import connection as PgConnection

from app.config import settings


def get_connection() -> PgConnection:
    """
    Create and return a PostgreSQL connection using DATABASE_URL.
    """
    return psycopg2.connect(settings.database_url)


def check_database_connection() -> bool:
    """
    Return True if the database connection works correctly.
    """
    connection: Optional[PgConnection] = None

    try:
        connection = get_connection()
        return True
    except Exception:
        return False
    finally:
        if connection is not None:
            connection.close()


def get_database_time():
    """
    Execute a simple query against PostgreSQL and return the current DB time.
    """
    connection: Optional[PgConnection] = None

    try:
        connection = get_connection()

        with connection.cursor() as cursor:
            cursor.execute("SELECT NOW();")
            row = cursor.fetchone()

        return row[0] if row else None
    except Exception:
        return None
    finally:
        if connection is not None:
            connection.close()