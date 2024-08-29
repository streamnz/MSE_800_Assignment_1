from datetime import timedelta, datetime

import config
from dao.booking_dao import BookingDAO
from dao.car_dao import CarDAO
from dictionary.car_state import CarState
from models.booking import Booking
from util import print_util


class BookingManagement:
    def __init__(self, db_connection):
        self.booking_dao = BookingDAO(db_connection)
        self.car_dao = CarDAO(db_connection)

    def create_booking(self, user_id, car_id, start_date, end_date, create_by):
        booking = Booking(None, user_id, car_id, start_date, end_date, "Pending")
        booking.create_by = create_by
        self.booking_dao.add_booking(booking)

    def update_booking(self, booking_id, status, rental_date, return_date, feedback, update_by):
        booking = self.booking_dao.get_booking_by_id(booking_id)
        booking.status = status
        booking.rental_date = rental_date
        booking.return_date = return_date
        booking.feedback = feedback
        booking.update_by = update_by
        self.booking_dao.update_booking(booking)

    def cancel_booking(self, booking_id):
        self.booking_dao.delete_booking(booking_id)

    def book_car(self, user_id, car_id, start_date_str, period):
        # Convert start_date_str to a datetime object
        date_format = "%Y-%m-%d"
        try:
            start_date = datetime.strptime(start_date_str, date_format)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        # Check if the car is available
        car = self.car_dao.get_car_by_id(car_id)
        if not car or car.status != CarState.AVAILABLE.value:
            print("Car is not available for booking.")
            return

        # Calculate the end_date
        end_date = start_date + timedelta(days=period)

        # Create a new booking
        booking = Booking(None, user_id, car_id, start_date, end_date, "Pending")
        booking.create_by = user_id  # Assuming the user is the creator
        self.booking_dao.add_booking(booking)

        # Update car status to 'Booked'
        car.status = CarState.BOOKED.value
        car.update_date = datetime.now()
        car.update_by = user_id
        self.car_dao.update_car(car)

        print("Booking confirmed. Car has been booked successfully.")

    def view_rental_history(self, user_id):
        # Retrieve all bookings for the given user ID
        bookings = self.booking_dao.get_bookings_by_user_id(user_id)

        # Check if there are any bookings for the user
        if not bookings:
            print(f"No rental history found for user ID: {user_id}.")
            return

        # Print out each booking's details
        print(f"Rental history for user ID: {user_id}:")
        for booking in bookings:
            print(booking.print_out())

    def view_booking_to_do_list(self):
        bookings = self.booking_dao.query_to_do_booking()

        # Check if there are any bookings for the user
        if not bookings:
            print(f"No Booking need to approve.")
            return "No Booking"

        # Print out each booking's details
        print_util.print_bookings(bookings)

    def view_booking_history(self):
        bookings = self.booking_dao.query_booking_history()

        # Check if there are any bookings for the user
        if not bookings:
            print(f"No Booking need to approve.")
            return

        # Print out each booking's details
        print_util.print_bookings(bookings)

    def booking_approve(self, booking_id):
        # Retrieve the corresponding booking record
        booking = self.booking_dao.get_booking_by_id(booking_id)
        if not booking:
            print(f"Booking with ID {booking_id} does not exist.")
            return

        # Check if the current booking status allows approval
        if booking.status != "Pending":
            print(f"Booking with ID {booking_id} is not in a state that can be approved.")
            return

        # Update booking status to Approved and set rental date
        booking.status = "Approved"
        booking.rental_date = datetime.now()
        booking.update_by = config.current_username
        booking.update_date = datetime.now()

        # Update booking information in the database
        self.booking_dao.update_booking(booking)

        # Update car status to Rented
        car = self.car_dao.get_car_by_id(booking.car_id)
        if car:
            car.status = CarState.RENTED.value
            car.update_by = config.current_username
            car.update_date = datetime.now()
            self.car_dao.update_car(car)
        print(f"Booking with ID {booking_id} has been approved successfully.")

    def booking_deny(self, booking_id, reason=None):
        # Retrieve the corresponding booking record
        booking = self.booking_dao.get_booking_by_id(booking_id)
        if not booking:
            print(f"Booking with ID {booking_id} does not exist.")
            return

        # Check if the current booking status allows denial
        if booking.status != "Pending":
            print(f"Booking with ID {booking_id} is not in a state that can be denied.")
            return

        # Update booking status to Denied and set the return date
        booking.status = "Denied"
        booking.return_date = datetime.now()  # Assuming denial closes the booking
        booking.update_by = config.current_username
        booking.update_date = datetime.now()

        # Optionally record the reason for denial
        if reason:
            booking.feedback = reason

        # Update booking information in the database
        self.booking_dao.update_booking(booking)

        # Optionally, reset the car status to Available if it was associated with this booking
        car = self.car_dao.get_car_by_id(booking.car_id)
        if car and car.status == CarState.BOOKED.value:
            car.status = CarState.AVAILABLE.value
            car.update_by = config.current_username
            car.update_date = datetime.now()
            self.car_dao.update_car(car)

        print(f"Booking with ID {booking_id} has been denied successfully.")

    def get_booking_by_id(self, booking_id):
        return self.booking_dao.get_booking_by_id(booking_id)

    def statics_by_car(self):
        car_statistics = self.booking_dao.get_car_statistics()

        print_util.print_list_as_dataframe(car_statistics)
