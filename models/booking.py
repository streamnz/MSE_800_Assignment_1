from datetime import datetime


class Booking:
    def __init__(self, booking_id=None, user_id=None, car_id=None, start_date=None, end_date=None, status=None,
                 rental_date=None, return_date=None, feedback=None, is_del=False, create_by=None, create_date=None,
                 update_by=None, update_date=None):
        self.booking_id = booking_id
        self.user_id = user_id
        self.car_id = car_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.rental_date = rental_date
        self.return_date = return_date
        self.feedback = feedback
        self.is_del = is_del
        self.create_by = create_by
        self.create_date = create_date
        self.update_by = update_by
        self.update_date = update_date

    def to_dict(self):
        return {
            'Booking ID': self.booking_id,
            'User ID': self.user_id,
            'Car ID': self.car_id,
            'Start Date': self.start_date.strftime('%Y-%m-%d') if isinstance(self.start_date,
                                                                             datetime) else self.start_date,
            'End Date': self.end_date.strftime('%Y-%m-%d') if isinstance(self.end_date, datetime) else self.end_date,
            'Status': self.status,
            'Rental Date': self.rental_date.strftime('%Y-%m-%d') if isinstance(self.rental_date,
                                                                               datetime) else self.rental_date,
            'Return Date': self.return_date.strftime('%Y-%m-%d') if isinstance(self.return_date,
                                                                               datetime) else self.return_date,
            'Feedback': self.feedback,
            'Created By': self.create_by,
            'Created Date': self.create_date.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.create_date,
                                                                                         datetime) else self.create_date,
            'Updated By': self.update_by,
            'Updated Date': self.update_date.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.update_date,
                                                                                         datetime) else self.update_date
        }
