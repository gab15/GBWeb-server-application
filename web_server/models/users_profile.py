from mongoengine import *
import datetime

from web_server.models.users_authentication import UserAuthenticationModel


class UserProfileModel(Document):
    _id = ReferenceField(UserAuthenticationModel)
    email = ReferenceField(UserAuthenticationModel)
    username = ReferenceField(UserAuthenticationModel)
    bio = StringField(max_length=1024, required=False)
    activity = {
        "modified": DateTimeField(required=True, default=datetime.datetime.utcnow()),
        "created": DateTimeField(required=True),
    }

    meta = {
        "db_alias": "users",
        "collection": "user_profile"
    }
