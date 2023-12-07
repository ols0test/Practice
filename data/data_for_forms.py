from faker import Faker


class DataForForms:
    fake = Faker("en_US")
    first_name = fake.first_name()
