from datetime import datetime

import config
from dao.booking_dao import BookingDAO
from dao.user_dao import UserDAO
from models.user import User
from util import print_util


class UserManagement:

    # Initialize the user management class
    def __init__(self, db_connection):
        self.user_dao = UserDAO(db_connection)
        self.booking_dao = BookingDAO(db_connection)

    def register_user(self, username, password, email, role):
        user = User(None, username, password, email, role)
        user.create_by = config.current_username
        self.user_dao.create_user(user)

    def login_user(self, username, password):
        user = self.user_dao.get_user_by_username(username)
        if user and user.password == password:
            print(f"Welcome, {user.username}!")
            config.current_username = user.username
            config.current_user = user
            return user
        else:
            print("Invalid username or password.")
            return None

    def delete_user(self, user_id):
        # Check if the user has any active bookings
        active_bookings = self.booking_dao.get_active_bookings_by_user_id(user_id)

        if active_bookings:
            print("User has active bookings and cannot be deleted.")
            return        # Delete the user by user ID
        self.user_dao.delete_user(user_id)

    # Check if the user is an admin
    def is_admin(self, username, password):
        user = self.user_dao.get_user_by_username(username)
        if user and user.password == password and user.role == 'admin':
            return True
        else:
            return False

    def get_user_by_username(self, username):
        return self.user_dao.get_user_by_username(username)

    ## print all users by role user_id desc
    def view_users(self):
        all_user = self.user_dao.get_users_grouped_by_role()
        for role, users in all_user.items():
            print(f"Role: {role}")
            print_util.print_users(users)

    def query_by_user_id(self, user_id):
        return self.user_dao.get_user_by_id(user_id)

    def update_user(self, user_id, username=None, password=None, email=None, role=None):
        # query current user
        user = self.user_dao.get_user_by_id(user_id)
        if not user:
            print("User not found.")
            return None

        # 更新用户的相关信息
        if username:
            user.username = username
        if password:
            user.password = password
        if email:
            user.email = email
        if role:
            user.role = role

        # 设置更新信息
        user.update_by = config.current_username
        user.update_date = datetime.now()

        # 调用 DAO 层的方法来更新数据库中的用户记录
        self.user_dao.update_user(user)
        print(f"User {user.username} updated successfully.")

        return user

    def statics_by_user(self):
        user_statistics = self.user_dao.get_user_statistics()

        # Display the DataFrame in the console
        print_util.print_list_as_dataframe(user_statistics)
