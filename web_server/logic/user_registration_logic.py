import uuid
import datetime
import bcrypt


class NoUsernameError(Exception):
    pass


class UserExistsError(Exception):
    pass


class UserRegistrationLogic:
    def __init__(self, users_authentication_model):
        self.users_authentication_model = users_authentication_model

    def register_user(self, user_info):
        username = user_info.get("username")

        # An AttributeError will be thrown if the password is empty or not a string
        password = bcrypt.hashpw(password=user_info.get("password").encode("utf-8"), salt=bcrypt.gensalt())

        if not username:
            raise NoUsernameError

        if self.users_authentication_model.objects(username=username):
            raise UserExistsError

        return self._update_registration_model(username=username, password=password, email=user_info.get("email", ""))

    def _update_registration_model(self, username, password, email):
        user_id = str(uuid.uuid4())

        user_document = {
                "username": username,
                "password": password,
                "email": email,
                "user_ids": {
                    "user_id": user_id
                },
                "activity": {
                    "created": datetime.datetime.utcnow(),
                    "modified": datetime.datetime.utcnow(),
                }
            }

        self.users_authentication_model(**user_document).save()

        return {"user_id": user_id}
