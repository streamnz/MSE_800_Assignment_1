from models.car import Car

class CarDAO:
    def __init__(self, db_connection):
        self.db = db_connection

    def add_car(self, car):
        cursor = self.db.cursor()
        query = ("INSERT INTO CARS (make, model, year, license_plate, mileage, status, create_date, create_by) "
                 "VALUES (%s, %s, %s, %s, %s, %s, CURDATE(), %s)")
        cursor.execute(query, (car.make, car.model, car.year, car.license_plate, car.mileage, car.status, car.create_by))
        self.db.commit()

    def get_car_by_id(self, car_id):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM CARS WHERE car_id = %s AND is_del = FALSE", (car_id,))
        result = cursor.fetchone()
        return Car(**result) if result else None

    def get_available_car_by_id(self,car_id):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM CARS WHERE car_id = %s AND is_del = FALSE AND status ='Available'", (car_id,))
        result = cursor.fetchone()
        return Car(**result) if result else None

    def update_car(self, car):
        cursor = self.db.cursor()
        query = ("UPDATE CARS SET make = %s, model = %s, year = %s, license_plate = %s, mileage = %s, status = %s, update_date = CURDATE(), update_by = %s "
                 "WHERE car_id = %s")
        cursor.execute(query, (car.make, car.model, car.year, car.license_plate, car.mileage, car.status, car.update_by, car.car_id))
        self.db.commit()

    def delete_car(self, car_id):
        cursor = self.db.cursor()
        cursor.execute("UPDATE CARS SET is_del = TRUE, update_date = CURDATE(), update_by = %s WHERE car_id = %s", (car_id, car_id))
        self.db.commit()

    def is_car_exist_by_license_plate(self, license_plate):
        cursor = self.db.cursor()
        query = "SELECT COUNT(*) FROM CARS WHERE license_plate = %s AND is_del = FALSE"
        cursor.execute(query, (license_plate,))
        result = cursor.fetchone()
        return result[0] > 0

    def get_car_by_license(self, license_plate):
        query = "SELECT * FROM CARS WHERE license_plate = %s AND is_del = FALSE"
        cursor = self.db.cursor()
        cursor.execute(query, (license_plate,))
        result = cursor.fetchone()
        if result:
            return Car(*result)
        else:
            return None

    def get_cars(self):
        query = ("SELECT * FROM CARS WHERE is_del = FALSE "
                 "ORDER BY car_id DESC ")
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(query)
        results = cursor.fetchall()
        cars = [Car(**result) for result in results]
        return cars

    def get_available_cars(self):
        query = ("SELECT * FROM CARS WHERE is_del = FALSE AND status ='Available' "
                 "ORDER BY update_date desc ,car_id DESC ")
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(query)
        results = cursor.fetchall()
        cars = [Car(**result) for result in results]
        return cars
