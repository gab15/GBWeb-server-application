import datetime

from mongoengine import *


class ActivityModel(EmbeddedDocument):
    created = DateTimeField(required=True, default=datetime.datetime.utcnow())
    modified = DateTimeField(required=True, default=datetime.datetime.utcnow())
