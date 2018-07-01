import json

from web_server.handlers.base import BaseHandler

from web_server.logic.user_registration_logic import UserRegistrationLogic, UserExistsError, NoUsernameError

from web_server.models.users_authentication import UserAuthenticationModel


class UserRegistrationHandler(BaseHandler):

    def initialize(self):
        super(UserRegistrationHandler, self).initialize()

        user_registration_logic = UserRegistrationLogic(users_authentication_model=UserAuthenticationModel)

        setattr(self, "user_registration_logic", user_registration_logic)

    def post(self):
        try:
            post_body = json.loads(self.request.body)

            result = getattr(self, "user_registration_logic").register_user(user_info=post_body)

        except UserExistsError:
            return self.error_message(message="User Already Exists")

        except NoUsernameError:
            return self.error_message(message="Missing Username")

        except Exception as e:
            return self.error_message(message="Unexpected Error", **{"error": e})

        return self.write(json.dumps(result))
