from tinydb import TinyDB
from fake import Faker

fake = Faker(locale='fr_FR')
db = TinyDB('db.json', indent=4)

db.insert({
    "first_name": fake.first_name(),
    "last_name": fake.last_name(),
    "score": fake.random_int()
})
