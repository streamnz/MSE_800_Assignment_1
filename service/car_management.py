from datetime import datetime

import config
import print_util
from dao.car_dao import CarDAO


class CarManagement:
    def __init__(self, db_connection):
        self.car_dao = CarDAO(db_connection)

    def save_car(self, car):
        exist = self.car_dao.get_car_by_license(car.license_plate)
        if exist:
            car.car_id = exist.car_id
            car.update_by = config.current_username
            car.update_date = datetime.now()
            self.car_dao.update_car(car)
        else:
            car.create_by = config.current_username
            car.create_date = datetime.now()
            self.car_dao.add_car(car)
        print(car.__dict__)

    def update_car(self, car):
        car.update_by = config.current_username
        car.update_date = datetime.now()
        self.car_dao.update_car(car)

    def delete_car(self, car_id):
        self.car_dao.delete_car(car_id)

    def view_cars(self):
        cars = self.car_dao.get_cars()
        print_util.print_cars(cars)

    def query_by_car_id(self, car_id):
        car = self.car_dao.get_car_by_id(car_id)
        return car

    def available_car_id(self, car_id):
        car = self.car_dao.get_available_car_by_id(car_id)
        return car

    def query_by_license(self, license):
        car = self.car_dao.get_car_by_license(license)
        return car

    def view_available_cars(self):
        cars = self.car_dao.get_available_cars()
        print_util.print_cars(cars)

    def get_available_car_by_id(self, car_id):
        car = self.car_dao.get_available_car_by_id(car_id)
        return car
