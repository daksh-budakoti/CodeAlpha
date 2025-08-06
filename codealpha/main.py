import csv
from database import init_db, insert_data
from validator import is_duplicate

def load_data(file_path):
    with open(file_path, mode='r') as file:
        return list(csv.DictReader(file))

def main():
    init_db()
    data = load_data("data/input_data.csv")

    for row in data:
        name, email = row["name"], row["email"]
        if not is_duplicate(email):
            success = insert_data(name, email)
            print(f"Inserted: {name} - {email}") if success else print(f"Failed to insert: {email}")
        else:
            print(f"Duplicate found: {email}")

if __name__ == "__main__":
    main()
