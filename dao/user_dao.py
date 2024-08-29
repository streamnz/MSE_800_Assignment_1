from models.user import User


class UserDAO:
    def __init__(self, db_connection):
        self.db = db_connection

    def create_user(self, user):
        cursor = self.db.cursor()
        query = ("INSERT INTO USERS (username, password, email, role, create_date, create_by) "
                 "VALUES (%s, %s, %s, %s, CURDATE(), %s)")
        cursor.execute(query, (user.username, user.password, user.email, user.role, user.username))
        self.db.commit()

    def get_user_by_id(self, user_id):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(
            "SELECT user_id, username, password, email, role FROM USERS WHERE user_id = %s AND is_del = FALSE",
            (user_id,))
        result = cursor.fetchone()
        return User(**result) if result else None

    def get_user_by_username(self, username):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM USERS WHERE username = %s AND is_del = FALSE",
            (username,))
        result = cursor.fetchone()
        return User(**result) if result else None

    def update_user(self, user):
        cursor = self.db.cursor()
        query = ("UPDATE USERS SET password = %s, email = %s, role = %s, update_date = CURDATE(), update_by = %s "
                 "WHERE user_id = %s")
        cursor.execute(query, (user.password, user.email, user.role, user.username, user.user_id))
        self.db.commit()

    def delete_user(self, user_id):
        cursor = self.db.cursor()
        cursor.execute("UPDATE USERS SET is_del = TRUE, update_date = CURDATE(), update_by = %s WHERE user_id = %s",
                       (user_id, user_id))
        self.db.commit()

    def get_users_grouped_by_role(self):
        cursor = self.db.cursor(dictionary=True)
        query = ("SELECT * FROM USERS WHERE is_del = FALSE "
                 "ORDER BY role, user_id DESC")
        cursor.execute(query)
        results = cursor.fetchall()

        # 按角色分组
        grouped_users = {}

        for result in results:
            role = result['role']
            if role not in grouped_users:
                grouped_users[role] = []
            grouped_users[role].append(User(**result))
        return grouped_users

    def get_user_statistics(self):
        cursor = self.db.cursor(dictionary=True)

        query = """
           SELECT 
               U.user_id,
               U.username,
               U.email,
               COUNT(B.booking_id) AS total_bookings,
               SUM(DATEDIFF(B.end_date, B.start_date)) AS total_rental_days,
               AVG(DATEDIFF(B.end_date, B.start_date)) AS average_rental_days
           FROM 
               USERS U
           LEFT JOIN 
               BOOKINGS_RENTALS B ON U.user_id = B.user_id
           WHERE 
               B.is_del = FALSE
           GROUP BY 
               U.user_id, U.username, U.email
           ORDER BY 
               total_bookings DESC;
           """

        cursor.execute(query)
        results = cursor.fetchall()
        return results
