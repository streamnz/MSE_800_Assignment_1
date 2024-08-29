from datetime import datetime

import config
import controler.display
from dictionary.car_state import CarState
from models.car import Car
from service.booking_management import BookingManagement
from service.car_management import CarManagement
from service.user_management import UserManagement
from util import input_util
from util.db_utils import DatabaseConnection


class Controller:
    def __init__(self):
        self.db_connection = DatabaseConnection().create_connection()
        self.user_management = UserManagement(self.db_connection)
        self.car_management = CarManagement(self.db_connection)
        self.booking_management = BookingManagement(self.db_connection)

    def register_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input_util.input_valid_email(input("Enter email: "))

        controler.display.Display.display_role_menu()
        role_choice = input("Select role: ")
        role = "customer" if role_choice == "1" else "admin" if role_choice == "2" else None

        if role_choice == "1":
            self.user_management.register_user(username, password, email, role)
            print(f"{username} with role:{role.capitalize()} registered successfully!")
        elif role_choice == "2":
            admin_name = input("Enter An admin username: ")
            admin_pwd = input("Enter An admin password: ")
            if self.user_management.is_admin(admin_name, admin_pwd):
                self.user_management.register_user(username, password, email, role)
                print(f"{username} with role:{role.capitalize()} registered successfully!")
            else:
                print("Invalid credentials.")
        else:
            print("Invalid role selected.")

    def login_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = self.user_management.login_user(username, password)

        if user:
            if user.role == "customer":
                self.customer_menu(user)
            elif user.role == "admin":
                self.admin_menu(user)
        else:
            print("Login failed. Check your credentials.")

    def customer_menu(self, user):
        while True:
            controler.display.Display.display_customer_menu()
            customer_choice = input("Enter choice number: ")
            if customer_choice == "1":
                self.car_management.view_available_cars()
            elif customer_choice == "2":
                # check available car id
                available_car = input_util.input_exist_available_car(self.car_management)
                user = config.current_user
                start_date = input_util.input_valid_future_date_within_month()
                period = input_util.input_valid_number_within_30()
                self.booking_management.book_car(user.user_id, available_car.car_id, start_date, period)
            elif customer_choice == "3":
                user = config.current_user
                self.booking_management.view_rental_history(user.user_id)
            elif customer_choice == "4":
                # View Current User Info
                print(config.current_user.print_out())
            elif customer_choice == "5":
                print("Logging out...")
                break
            else:
                print("Invalid choice.")

    def admin_menu(self, user):
        while True:
            controler.display.Display.display_admin_menu()
            admin_choice = input("Enter choice number: ")

            if admin_choice == "1":
                self.car_management_menu()
            elif admin_choice == "2":
                self.user_management_menu()
            elif admin_choice == "3":
                self.rental_management_menu()
            elif admin_choice == "4":
                print("Logging out...")
                break
            else:
                print("Invalid choice.")

    def car_management_menu(self):
        while True:
            self.car_management.view_cars()
            controler.display.Display.car_management_menu()
            car_choice = input("Enter choice number: ")

            if car_choice == "1":
                # add car info
                input_license_plate = input_util.input_none_exist_license(self.car_management, None)
                input_make = input_util.input_valid_make()
                input_model = input_util.input_valid_model()
                input_year = input_util.input_valid_year()
                input_mileage = input_util.input_valid_mileage()
                car = Car(None, input_make, input_model, input_year, input_license_plate, input_mileage,
                          CarState.AVAILABLE.value, False, config.current_username, datetime.now())
                self.car_management.save_car(car)
            elif car_choice == "2":
                # update car info
                input_car_id = input_util.input_exist_car_id(self.car_management)
                exist = self.car_management.query_by_car_id(input_car_id)
                input_license_plate = input_util.input_none_exist_license(self.car_management, exist.license_plate)
                input_make = input_util.input_valid_make()
                input_model = input_util.input_valid_model()
                input_year = input_util.input_valid_year()
                input_mileage = input_util.input_valid_mileage()
                car = Car(input_car_id, input_make, input_model, input_year, input_license_plate, input_mileage,
                          CarState.AVAILABLE.value, False, None, None, config.current_username, datetime.now())
                self.car_management.update_car(car)
            elif car_choice == "3":
                # delete a car
                input_car_id = input_util.input_exist_car_id(self.car_management)
                self.car_management.delete_car(input_car_id)
            elif car_choice == "4":
                break
            else:
                print("Invalid choice.")

    def user_management_menu(self):
        while True:
            self.user_management.view_users()
            controler.display.Display.user_management_menu()
            user_choice = input("Enter choice number: ")

            if user_choice == "1":
                # add customer
                input_user_name = input_util.input_not_exist_username(self.user_management)
                input_pwd = input_util.input_valid_password(input("Enter password: ").strip())
                input_email = input_util.input_valid_email(input("Enter email: ").strip())
                self.user_management.register_user(input_user_name, input_pwd, input_email, "customer")
            elif user_choice == "2":
                # add admin
                input_user_name = input_util.input_not_exist_username(self.user_management)
                input_pwd = input_util.input_valid_password(input("Enter password: ").strip())
                input_email = input_util.input_valid_email(input("Enter email: ").strip())
                self.user_management.register_user(input_user_name, input_pwd, input_email, "admin")
            elif user_choice == "3":
                # update user
                input_user_id = input_util.input_exist_user_id(self.user_management)
                exist = self.user_management.query_by_user_id(input_user_id)
                input_user_name = input_util.input_not_exist_username(self.user_management, exist.username)
                input_pwd = input_util.input_valid_password(input("Enter password: ").strip())
                input_email = input_util.input_valid_email(input("Enter email: ").strip())
                self.user_management.update_user(input_user_id, input_user_name, input_pwd, input_email)
            elif user_choice == "4":
                input_user_id = input_util.input_exist_user_id(self.user_management)
                self.user_management.delete_user(input_user_id)
            elif user_choice == "5":
                # user detail
                input_user_id = input_util.input_exist_user_id(self.user_management)
                user = self.user_management.query_by_user_id(input_user_id)
                print(user.print_out())
            elif user_choice == "6":
                # back
                break
            else:
                print("Invalid choice.")

    def rental_management_menu(self):
        while True:
            controler.display.Display.rental_management_menu()
            rental_choice = input("Enter choice number: ")
            if rental_choice == "1":
                # 1.list
                result = self.booking_management.view_booking_to_do_list()
                if "No Booking" == result:
                    continue
                # 2. select booking
                input_booking_id = input_util.input_exist_booking_id(self.booking_management)
                self.booking_to_do_list(input_booking_id)
            elif rental_choice == "2":
                # 2. Booking history
                self.booking_management.view_booking_history()
            elif rental_choice == "3":
                # statics by car
                self.booking_management.statics_by_car()
            elif rental_choice == "4":
                # statics by user
                self.user_management.statics_by_user()
            elif rental_choice == "5":
                # back
                break
            else:
                print("Invalid choice.")

    def booking_to_do_list(self,input_booking_id):
        while True:
            controler.display.Display.booking_approve_menu()
            rental_choice = input("Enter choice number: ")
            if rental_choice == "1":
                # 1. approve
                self.booking_management.booking_approve(input_booking_id)
                break
            elif rental_choice == "2":
                # 2. deny
                deny_reason = input_util.input_reason_for_denial()
                self.booking_management.booking_deny(input_booking_id,deny_reason)
                break
            elif rental_choice == "3":
                # back
                break
            else:
                print("Invalid choice.")

    def run(self):
        while True:
            controler.display.Display.display_menu()
            choice = input("Enter choice number: ")

            if choice == "1":
                self.register_user()
            elif choice == "2":
                self.login_user()
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
