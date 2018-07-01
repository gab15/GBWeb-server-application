from mongoengine import *

from web_server.models.base_models import ActivityModel


class UserIdentificationModel(EmbeddedDocument):
    user_id = StringField(max_length=36, required=True)
    facebook_id = StringField(max_length=1024, required=True, default="")
    google_id = StringField(max_length=1024, required=True, default="")


class UserAuthenticationModel(Document):
    email = StringField(max_length=1024, default="", null=False)
    username = StringField(max_length=1024, required=True)
    password = StringField(max_length=1024, required=True)
    email_authenticated = BooleanField(required=True, default=False)
    activity = EmbeddedDocumentField(ActivityModel)
    user_ids = EmbeddedDocumentField(UserIdentificationModel)

    meta = {
        "db_alias": "users",
        "collection": "user_authentication",
    }
