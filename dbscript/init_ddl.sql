CREATE TABLE USERS (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL,
    is_del BOOLEAN DEFAULT FALSE,
    create_date DATE NOT NULL,
    create_by VARCHAR(255),
    update_date DATE,
    update_by VARCHAR(255)
);

CREATE TABLE CARS (
    car_id INT PRIMARY KEY AUTO_INCREMENT,
    make VARCHAR(255) NOT NULL,
    model VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    license_plate VARCHAR(255) NOT NULL UNIQUE,
    mileage FLOAT NOT NULL,
    status VARCHAR(50) NOT NULL,
    is_del BOOLEAN DEFAULT FALSE,
    create_date DATE NOT NULL,
    create_by VARCHAR(255),
    update_date DATE,
    update_by VARCHAR(255)
);

CREATE TABLE DICTIONARY (
    dict_id INT PRIMARY KEY AUTO_INCREMENT,
    dict_type VARCHAR(50) NOT NULL,
    dict_code VARCHAR(50) NOT NULL,
    dict_value VARCHAR(255) NOT NULL,
    description TEXT,
    is_del BOOLEAN DEFAULT FALSE,
    create_date DATE NOT NULL,
    create_by VARCHAR(255),
    update_date DATE,
    update_by VARCHAR(255),
    UNIQUE (dict_type, dict_code)
);

CREATE TABLE BOOKINGS_RENTALS (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    car_id INT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status VARCHAR(50) NOT NULL,
    rental_date DATE,
    return_date DATE,
    feedback TEXT,
    is_del BOOLEAN DEFAULT FALSE,
    create_date DATE NOT NULL,
    create_by VARCHAR(255),
    update_date DATE,
    update_by VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES USERS(user_id),
    FOREIGN KEY (car_id) REFERENCES CARS(car_id)
);


ALTER TABLE USERS
    ADD FOREIGN KEY (role) REFERENCES DICTIONARY(dict_code)
    ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE CARS
    ADD FOREIGN KEY (status) REFERENCES DICTIONARY(dict_code)
    ON DELETE RESTRICT ON UPDATE CASCADE;
