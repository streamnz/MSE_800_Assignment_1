from datetime import datetime

import pandas as pd

from car_state import CarState


def print_list_as_dataframe(data_list):
    if not data_list:
        print("No data to display.")
        return

    # Convert the list to a DataFrame
    df = pd.DataFrame(data_list)

    # Set display options
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', 100)
    pd.set_option('display.width', 1000)

    # Display the DataFrame in the console
    print(df)


def print_bookings(bookings):
    # Convert the list of Booking objects to a list of dictionaries
    bookings_dict_list = [booking.to_dict() for booking in bookings]

    # Create a pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(bookings_dict_list)

    # Set display options to show the full table in the console
    pd.set_option('display.max_rows', None)  # 显示所有行
    pd.set_option('display.max_columns', None)  # 显示所有列
    pd.set_option('display.expand_frame_repr', False)  # 防止换行
    pd.set_option('max_colwidth', None)  # 显示所有列内容
    pd.set_option('display.width', None)  # 自动调整显示宽度

    # Print the DataFrame in the console
    print(df)


def print_cars(cars):
    # Convert the list of Car objects to a list of dictionaries
    car_info_list = []

    for car in cars:
        car_info = {
            'Car ID': car.car_id,
            'Make': car.make,
            'Model': car.model,
            'Year': car.year,
            'License Plate': car.license_plate,
            'Mileage': car.mileage,
            'Status': car.status.name if isinstance(car.status, CarState) else car.status,
            'Created By': car.create_by,
            'Created Date': car._format_date(car.create_date),
            'Updated By': car.update_by,
            'Updated Date': car._format_date(car.update_date)
        }
        car_info_list.append(car_info)

    # Create a pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(car_info_list)

    # Set display options to show the full table in the console
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('max_colwidth', None)
    pd.set_option('display.width', 1000)

    # Print the DataFrame in the console
    print(df)


def print_users(users):
    # Convert the list of User objects to a list of dictionaries
    users_dict_list = []
    for user in users:
        user_dict = {
            'User ID': user.user_id,
            'Username': user.username,
            'Email': user.email,
            'Created By': user.create_by,
            'Created Date': user.create_date.strftime('%Y-%m-%d %H:%M:%S') if isinstance(user.create_date,
                                                                                         datetime) else user.create_date,
            'Updated By': user.update_by,
            'Updated Date': user.update_date.strftime('%Y-%m-%d %H:%M:%S') if isinstance(user.update_date,
                                                                                         datetime) else user.update_date,
        }
        users_dict_list.append(user_dict)

    # Create a pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(users_dict_list)

    # Set display options to show the full table in the console
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('max_colwidth', None)
    pd.set_option('display.width', 1000)

    # Print the DataFrame in the console
    print(df)
