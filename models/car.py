from datetime import datetime


class Car:
    def __init__(self, car_id=None, make=None, model=None, year=None, license_plate=None, mileage=None, status=None,
                 is_del=False, create_by=None, create_date=None, update_by=None, update_date=None):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.license_plate = license_plate
        self.mileage = mileage
        self.status = status
        self.is_del = is_del
        self.create_by = create_by
        self.create_date = create_date
        self.update_by = update_by
        self.update_date = update_date

    @staticmethod
    def _format_date(date_value):
        if isinstance(date_value, datetime):
            return date_value.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(date_value, str):
            try:
                # Attempt to parse string to datetime
                parsed_date = datetime.fromisoformat(date_value)
                return parsed_date.strftime('%Y-%m-%d %H:%M:%S')
            except ValueError:
                # If parsing fails, return original string
                return date_value
        else:
            # If date_value is of unexpected type, convert to string
            return str(date_value)
