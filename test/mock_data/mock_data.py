import random
from datetime import timedelta

from faker import Faker

faker = Faker()

# Generating User Data
users = []
for i in range(20):
    # Create a username with a pattern, e.g., 'Customer1', 'Customer2', etc.
    username = f"Customer{i + 1}"

    user = {
        "user_id": i + 1,
        "username": username,
        "password": username,  # Password is the same as the username
        "email": faker.email(),
        "role": "customer",
        "is_del": False,
        "create_date": faker.date_this_year(),
        "create_by": "admin",
        "update_date": faker.date_this_year(),
        "update_by": "admin"
    }
    users.append(user)

# Generating Car Data
cars = []
for i in range(20):
    car = {
        "car_id": i + 1,
        "make": faker.company(),
        "model": faker.word(),
        "year": random.randint(2000, 2023),
        "license_plate": faker.license_plate(),
        "mileage": random.uniform(10000, 200000),
        "status": random.choice(["Available", "Booked", "Rented", "Maintenance"]),
        "is_del": False,
        "create_date": faker.date_this_year(),
        "create_by": "admin",
        "update_date": faker.date_this_year(),
        "update_by": "admin"
    }
    cars.append(car)

# Generating Booking Data
bookings = []
for i in range(200):
    user_id = random.choice(users)["user_id"]
    car_id = random.choice(cars)["car_id"]
    start_date = faker.date_between(start_date="-2y", end_date="today")
    period = random.randint(1, 30)
    end_date = start_date + timedelta(days=period)
    status = random.choice(["Pending", "Approved", "Denied"])
    rental_date = start_date if status == "Approved" else None
    return_date = end_date if status == "Approved" else None
    feedback = faker.sentence() if status == "Approved" else None

    booking = {
        "booking_id": i + 1,
        "user_id": user_id,
        "car_id": car_id,
        "start_date": start_date,
        "end_date": end_date,
        "status": status,
        "rental_date": rental_date,
        "return_date": return_date,
        "feedback": feedback,
        "is_del": False,
        "create_date": faker.date_this_year(),
        "create_by": "admin",
        "update_date": faker.date_this_year(),
        "update_by": "admin"
    }
    bookings.append(booking)

# Generating SQL Insert Statements
with open('test_data.sql', 'w') as f:
    # Users Insert Statements
    for user in users:
        f.write(
            f"INSERT INTO USERS (user_id, username, password, email, role, is_del, create_date, create_by, update_date, update_by) VALUES "
            f"({user['user_id']}, '{user['username']}', '{user['password']}', '{user['email']}', '{user['role']}', {user['is_del']}, "
            f"'{user['create_date']}', '{user['create_by']}', '{user['update_date']}', '{user['update_by']}');\n")

    # Cars Insert Statements
    for car in cars:
        f.write(
            f"INSERT INTO CARS (car_id, make, model, year, license_plate, mileage, status, is_del, create_date, create_by, update_date, update_by) VALUES "
            f"({car['car_id']}, '{car['make']}', '{car['model']}', {car['year']}, '{car['license_plate']}', {car['mileage']:.2f}, '{car['status']}', {car['is_del']}, "
            f"'{car['create_date']}', '{car['create_by']}', '{car['update_date']}', '{car['update_by']}');\n")

    # Bookings Insert Statements
    for booking in bookings:
        rental_date = f"'{booking['rental_date']}'" if booking['rental_date'] else 'NULL'
        return_date = f"'{booking['return_date']}'" if booking['return_date'] else 'NULL'
        feedback = f"'{booking['feedback']}'" if booking['feedback'] else 'NULL'

        f.write(
            f"INSERT INTO BOOKINGS_RENTALS (booking_id, user_id, car_id, start_date, end_date, status, rental_date, return_date, feedback, is_del, create_date, create_by, update_date, update_by) VALUES "
            f"({booking['booking_id']}, {booking['user_id']}, {booking['car_id']}, '{booking['start_date']}', '{booking['end_date']}', '{booking['status']}', "
            f"{rental_date}, {return_date}, {feedback}, {booking['is_del']}, '{booking['create_date']}', '{booking['create_by']}', "
            f"'{booking['update_date']}', '{booking['update_by']}');\n")

print("Test data SQL script generated successfully.")
