from controler.controller import Controller


def print_welcome_message():
    print("====================================")
    print("Welcome to the HAO Car Rental System!")
    print("====================================")
    print("Features Available:")
    print("1. User Management: Register, Login, and Role-Based Access Control")
    print("2. Car Management: Add, Update, Delete, and View Car Details")
    print("3. Booking Management: Book Cars, View Rental History, and Manage Bookings")
    print("4. Admin Features: Approve/Deny Bookings, Manage Users and Cars")
    print("5. Advanced Statistics: User-Level and Vehicle-Level Data Insights")
    print("6. Machine Learning Integration: Intelligent Decision-Making")
    print("Ready to streamline your car rental experience? Let's get started!")
    print("====================================")
    print("Starting the system...")


if __name__ == "__main__":
    print_welcome_message()
    controller = Controller()
    controller.run()
