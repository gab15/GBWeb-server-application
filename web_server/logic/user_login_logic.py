import uuid
import datetime
import bcrypt


class NoUsernameError(Exception):
    pass


class NoPasswordError(Exception):
    pass


class UserDoesNotExistError(Exception):
    pass


class WrongPasswordError(Exception):
    pass


class UserLoginLogic:
    def __init__(self, users_authentication_model):
        self.users_authentication_model = users_authentication_model

    def process_user_login(self, user_info):

        username = user_info.get("username")

        user_auth = self.users_authentication_model.objects.get(username=username)

        if not bcrypt.checkpw(password=user_info.get("password").encode("utf-8"),
                              hashed_password=user_auth.password.encode("utf-8")):
            raise WrongPasswordError

        return {"user_id": user_auth.user_ids.user_id, "access_token": "placeholder1", "refresh_token": "placeholder2"}
