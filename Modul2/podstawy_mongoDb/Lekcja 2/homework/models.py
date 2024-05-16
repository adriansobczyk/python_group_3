# models.py

from mongoengine import Document, StringField, BooleanField

class Contact(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = StringField(required=True)
    email_sent = BooleanField(default=False)
