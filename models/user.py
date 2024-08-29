from datetime import datetime


class User:
    def __init__(self, user_id = None, username = None, password =None, email=None, role=None, is_del=False,create_by=None,create_date=None,update_by=None,update_date=None):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.role = role
        self.is_del = is_del
        self.create_by = create_by
        self.create_date = create_date
        self.update_by = update_by
        self.update_date = update_date

    def print_out(self):
        # Format the creation and update dates
        create_date_str = self.create_date.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.create_date,
                                                                                       datetime) else self.create_date
        update_date_str = self.update_date.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.update_date,
                                                                                       datetime) else self.update_date

        # Prepare a list of fields, excluding is_del and password
        fields = [
            ('User ID', self.user_id),
            ('Username', self.username),
            ('Email', self.email),
            ('Created By', self.create_by),
            ('Created Date', create_date_str),
            ('Updated Date', update_date_str)
        ]

        # Construct the output string, including only non-empty fields
        output = ", ".join(f"{name}: {value}" for name, value in fields if value is not None)

        return output