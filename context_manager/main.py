import logging

from sqlite import open_db


def main():
    logging.basicConfig(level=logging.INFO)
    with open_db("cm.db") as db:
        db.execute("SELECT * FROM blog;")
        logging.info(db.fetchall())


if __name__ == "__main__":
    main()
