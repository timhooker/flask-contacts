class Contact(Document):
    name = StringField(max_length=60, required=True, unique=True)
    address = StringField(max_length=60)
    birthday = DateTimeField()
    phone = StringField(max_length=20)
    email = StringField(max_length=35)