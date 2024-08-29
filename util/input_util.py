import re
from datetime import datetime, timedelta


def is_valid_email(email):
    # Define the regular expression for email
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email)


def input_valid_email(email):
    while True:
        if is_valid_email(email):
            return email
        else:
            print("Invalid email format. Please try again.")
            email = input("Enter your email: ")


def input_valid_password(password):
    while True:
        if len(password) >= 1:
            return password
        else:
            print("Invalid password format. Please try again.")
            password = input("Enter your password: ")


def input_exist_car_id(car_management):
    car_id = input("Enter car_id: ")
    while True:
        if car_id.isdigit():
            exist = car_management.query_by_car_id(car_id)
            if exist:
                return car_id
        car_id = input("Please enter an exist car_id:").strip()


def input_exist_available_car(car_management):
    car_id = input("Enter car_id: ")
    while True:
        if car_id.isdigit():
            exist = car_management.get_available_car_by_id(car_id)
            if exist:
                return exist
        car_id = input("Please enter an exist available car_id:").strip()


def input_valid_mileage():
    input_mileage = input("Enter mileage:").strip()
    while True:
        if input_mileage.isdigit():
            break
        else:
            input_mileage = input("Please enter a valid mileage:").strip()
    return input_mileage


def input_valid_year():
    current_year = datetime.now().year
    year_pattern = re.compile(r'^\d{4}$')
    input_year = input("Enter year (YYYY):").strip()
    while True:
        if year_pattern.match(input_year) and int(input_year) < current_year:
            return input_year
        else:
            input_year = input("Please enter a valid year (YYYY):").strip()


def input_valid_model():
    input_model = input("Enter model:").strip()
    while True:
        if input_model:
            break
        else:
            input_model = input("Please enter a valid model:").strip()
    return input_model


def input_valid_make():
    input_make = input("Enter make: ")
    while True:
        if input_make.isalpha():
            break
        else:
            input_make = input("Please enter a valid make:").strip()
    return input_make


def input_none_exist_license(car_management, exception_plate):
    input_license_plate = input("Enter license plate: ").strip()
    while True:
        if input_license_plate:
            exist = car_management.query_by_license(input_license_plate)
            if exist and exist.license_plate != exception_plate:
                input_license_plate = input("license plate exists, pls input another license: ")
            else:
                break
        else:
            input_license_plate = input("Please enter a valid license plate:").strip()
    return input_license_plate


# input_util.py

def input_not_exist_username(user_management, except_username=None):
    input_user_name = input("Enter user name: ").strip()
    while True:
        if input_user_name:
            exist = user_management.get_user_by_username(input_user_name)
            if exist and exist.username != except_username:
                input_user_name = input("User name exists, please input another user name: ").strip()
            else:
                break
        else:
            input_user_name = input("Please enter a valid user name: ").strip()
    return input_user_name


def input_exist_user_id(user_management):
    input_user_id = input("Enter user_id: ").strip()
    while True:
        if input_user_id:
            exist = user_management.query_by_user_id(input_user_id)
            if exist:
                break
            else:
                input_user_id = input("Please enter an existing user_id: ").strip()
        else:
            input_user_id = input("Please enter a valid user_id: ").strip()
    return input_user_id


def input_valid_future_date_within_month():
    date_format = "%m-%d"
    today = datetime.now()
    current_year = today.year
    max_date = today + timedelta(days=30)

    while True:
        input_date_str = input("Enter a date within the next 30 days (MM-dd): ").strip()
        try:
            # Parse the date input with the current year
            input_date = datetime.strptime(f"{current_year}-{input_date_str}", f"%Y-{date_format}")
            if today <= input_date <= max_date:
                return input_date.strftime(f"%Y-{date_format}")  # Return in "YYYY-MM-dd" format
            else:
                print(
                    f"Date must be within the next 30 days (from {today.strftime('%Y-%m-%d')} to {max_date.strftime('%Y-%m-%d')}).")
        except ValueError:
            print("Invalid date format. Please try again using MM-dd.")


def input_valid_number_within_30():
    while True:
        input_str = input("Enter a number (0-30): ").strip()
        if input_str.isdigit():
            number = int(input_str)
            if 0 <= number <= 30:
                return number
            else:
                print("The number must be between 0 and 30. Please try again.")
        else:
            print("Invalid input. Please enter a valid number between 0 and 30.")


def input_exist_booking_id(booking_management):
    input_booking_id = input("Enter booking_id: ").strip()
    while True:
        if input_booking_id.isdigit():
            exist = booking_management.get_booking_by_id(int(input_booking_id))
            if exist:
                return input_booking_id
            else:
                input_booking_id = input("Booking ID does not exist. Please enter an existing booking_id: ").strip()
        else:
            input_booking_id = input("Please enter a valid booking_id (must be a number): ").strip()


def input_reason_for_denial():
    reason = input("Enter the reason for denial (optional): ").strip()
    while True:
        if reason:
            return reason
        else:
            confirmation = input(
                "No reason provided. Do you want to continue without a reason? (yes/no): ").strip().lower()
        if confirmation == "yes":
            return None
        elif confirmation == "no":
            reason = input("Enter the reason for denial: ").strip()
        else:
            print("Please enter 'yes' or 'no'.")
