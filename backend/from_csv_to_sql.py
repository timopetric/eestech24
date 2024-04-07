import csv
from datetime import datetime
import os
import sys
from sqlalchemy.sql import text

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from src.constants import OUT_PLANINSTVO_END
from sqlalchemy import create_engine

# Database connection URL (adjust as needed)
DATABASE_URL = "sqlite:///sql.db"


def connect_to_db():
    """Connects to the SQLite database and returns an engine object."""
    engine = create_engine(DATABASE_URL)
    return engine


def insert_data(engine, data):
    """Inserts a single data row into the 'predictions' table."""
    with engine.connect() as connection:
        # Assuming date format is YYYY-MM-DD
        # date = datetime.strptime(data[0], "%Y-%m-%d").date()
        date = data[0]
        sql_query = text("""
            INSERT INTO predictions (
                date, location_id, day_of_week, free_day, rr, ss, tg, month, pretocnost_7, pretocnost_3, pretocnost_q
            )
            VALUES (:date, :location_id, :day_of_week, :free_day, :rr, :ss, :tg, :month, :pretocnost_7, :pretocnost_3, :pretocnost_q)
            """)
        connection.execute(sql_query, {
            'date': date,
            'location_id': int(data[1]),
            'day_of_week': int(data[2]),
            'free_day': data[3],
            'rr': float(data[4]),
            'ss': float(data[5]),
            'tg': float(data[6]),
            'month': int(data[7]),
            'pretocnost_7': float(data[8]),
            'pretocnost_3': float(data[9]),
            'pretocnost_q': int(data[10])
        })
        connection.commit()


def main():
    """Main function to connect to the database, create table (if needed), and insert data from CSV."""
    connection = connect_to_db()

    with open(OUT_PLANINSTVO_END, "r") as csvfile:
        # Skip the header row (if it exists)
        next(csvfile)

        for row in csvfile:
            data = row.strip().split(",")
            print(float(data[4]))
            insert_data(connection, data)

    connection.dispose()
    print("Data uploaded successfully!")


if __name__ == "__main__":
    main()
