from models.booking import Booking


class BookingDAO:
    def __init__(self, db_connection):
        self.db = db_connection

    def add_booking(self, booking):
        cursor = self.db.cursor()
        query = ("INSERT INTO BOOKINGS_RENTALS (user_id, car_id, start_date, end_date, status, create_date, create_by) "
                 "VALUES (%s, %s, %s, %s, %s, CURDATE(), %s)")
        cursor.execute(query, (
            booking.user_id, booking.car_id, booking.start_date, booking.end_date, booking.status, booking.create_by))
        self.db.commit()

    def get_booking_by_id(self, booking_id):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM BOOKINGS_RENTALS WHERE booking_id = %s AND is_del = FALSE", (booking_id,))
        result = cursor.fetchone()
        return Booking(**result) if result else None

    def update_booking(self, booking):
        cursor = self.db.cursor()
        query = (
            "UPDATE BOOKINGS_RENTALS SET status = %s, rental_date = %s, return_date = %s, feedback = %s, update_date = CURDATE(), update_by = %s "
            "WHERE booking_id = %s")
        cursor.execute(query, (
            booking.status, booking.rental_date, booking.return_date, booking.feedback, booking.update_by,
            booking.booking_id))
        self.db.commit()

    def delete_booking(self, booking_id):
        cursor = self.db.cursor()
        cursor.execute(
            "UPDATE BOOKINGS_RENTALS SET is_del = TRUE, update_date = CURDATE(), update_by = %s WHERE booking_id = %s",
            (booking_id, booking_id))
        self.db.commit()

    def get_bookings_by_user_id(self, user_id):
        cursor = self.db.cursor(dictionary=True)
        query = "SELECT * FROM BOOKINGS_RENTALS WHERE user_id = %s AND is_del = FALSE ORDER BY booking_id DESC"
        cursor.execute(query, (user_id,))
        results = cursor.fetchall()

        # Convert the results to a list of Booking objects
        bookings = [Booking(**result) for result in results]

        return bookings

    def query_to_do_booking(self):
        cursor = self.db.cursor(dictionary=True)
        query = "SELECT * FROM BOOKINGS_RENTALS WHERE status = 'Pending' AND is_del = FALSE ORDER BY booking_id asc"
        cursor.execute(query)
        results = cursor.fetchall()

        # Convert the results to a list of Booking objects
        bookings = [Booking(**result) for result in results]

        return bookings

    def query_booking_history(self):
        cursor = self.db.cursor(dictionary=True)
        query = "SELECT * FROM BOOKINGS_RENTALS WHERE status in('Approved','Denied') AND is_del = FALSE ORDER BY booking_id asc"
        cursor.execute(query)
        results = cursor.fetchall()

        # Convert the results to a list of Booking objects
        bookings = [Booking(**result) for result in results]

        return bookings

    def get_active_bookings_by_user_id(self, user_id):
        cursor = self.db.cursor(dictionary=True)
        query = "SELECT * FROM BOOKINGS_RENTALS WHERE user_id = %s AND status IN ('Pending', 'Approved') AND is_del = FALSE ORDER BY booking_id DESC"
        cursor.execute(query, (user_id,))
        results = cursor.fetchall()

        # Convert the results to a list of Booking objects
        active_bookings = [Booking(**result) for result in results]

        return active_bookings if active_bookings else None

    def get_car_statistics(self):
        cursor = self.db.cursor(dictionary=True)

        query = """
         SELECT 
             C.car_id,
             C.make,
             C.model,
             C.license_plate,
             C.status,
             COUNT(B.booking_id) AS total_bookings,
             SUM(DATEDIFF(B.end_date, B.start_date)) AS total_rental_days,
             AVG(DATEDIFF(B.end_date, B.start_date)) AS average_rental_days
         FROM 
             CARS C
         LEFT JOIN 
             BOOKINGS_RENTALS B ON C.car_id = B.car_id
         WHERE 
             B.is_del = FALSE
         GROUP BY 
             C.car_id, C.make, C.model, C.license_plate, C.status
         ORDER BY 
             total_bookings DESC;
         """

        cursor.execute(query)
        results = cursor.fetchall()
        return results
