import json

from mongoengine import ValidationError

from web_server.handlers.base import BaseHandler

from web_server.logic.user_login_logic import UserLoginLogic, UserDoesNotExistError, NoPasswordError, \
    NoUsernameError

from web_server.models.users_authentication import UserAuthenticationModel


class UserLoginHandler(BaseHandler):

    def initialize(self):
        super(UserLoginHandler, self).initialize()

        user_login_logic = UserLoginLogic(users_authentication_model=UserAuthenticationModel)

        setattr(self, "user_registration_logic", user_login_logic)

    def post(self):
        try:
            post_body = json.loads(self.request.body)

            result = getattr(self, "user_registration_logic").process_user_login(user_info=post_body)

        except ValidationError:
            return self.error_message(message="Mongodb Validation Error")

        except UserDoesNotExistError:
            return self.error_message(message="User Does Not Exist")

        except NoPasswordError:
            return self.error_message(message="Missing Password")

        except NoUsernameError:
            return self.error_message(message="Missing Username")

        except Exception as e:
            return self.error_message(message="Unexpected Error", **{"error": e})

        return self.write(json.dumps(result))
