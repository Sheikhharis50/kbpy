import logging
import sqlite3
from contextlib import contextmanager


class SQLite:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        logging.info("Creating connection...")
        self.connection = sqlite3.connect(file_name)

    def __enter__(self):
        logging.info("Building cursor...")
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_value, trace):
        logging.info("Commiting changes...")
        self.connection.commit()
        logging.info("Closing connection...")
        self.connection.close()


@contextmanager
def open_db(file_name: str):
    connection = sqlite3.connect(file_name)
    logging.info("Creating connection...")
    try:
        logging.info("Building cursor...")
        yield connection.cursor()
    except sqlite3.DatabaseError as e:
        logging.error(e)
    finally:
        logging.info("Commiting changes...")
        connection.commit()
        logging.info("Closing connection...")
        connection.close()
