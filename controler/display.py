class Display:
    @staticmethod
    def display_menu():
        print("\nCar Rental System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

    @staticmethod
    def display_role_menu():
        print("\nSelect Role")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")

    @staticmethod
    def display_customer_menu():
        print("\nCustomer Menu")
        print("1. View Available Cars")
        print("2. Book a Car")
        print("3. View Rental History")
        print("4. View Current User Info")
        print("5. Logout")

    @staticmethod
    def display_admin_menu():
        print("\nAdmin Menu")
        print("1. Car Management")
        print("2. User Management")
        print("3. Rental Management")
        print("4. Logout")

    @staticmethod
    def car_management_menu():
        print("\nCar Management")
        print("1. Add Car")
        print("2. Update Car")
        print("3. Delete Car")
        print("4. Back")

    @staticmethod
    def user_management_menu():
        print("\nUser Management")
        print("1. Add Customer")
        print("2. Add Admin")
        print("3. Update User")
        print("4. Delete User")
        print("5. View User Details")
        print("6. Back")

    @staticmethod
    def rental_management_menu():
        print("\nRental Management")
        print("1. Booking to do List")
        print("2. Booking history")
        print("3. Statics by Car")
        print("4. Statics by User")
        print("5. Back")

    @staticmethod
    def booking_approve_menu():
        print("\nRental Management")
        print("1. Approve")
        print("2. Deny")
        print("3. Back")
