from collections.abc import Iterator

from faker import Faker

from apps.contact_book import models
from apps.contact_book.typing import T_NAME

fake = Faker()


def get_name() -> T_NAME:
    name = fake.unique.name()
    return name


def get_phone():
    phone = f"{fake.country_calling_code()} {fake.msisdn()}"
    return str(phone)


def get_birthday():
    birthday = fake.date()
    return birthday


def fake_data(amount: int) -> Iterator[models.Contact_book]:
    for _ in range(amount):
        name = get_name()
        phone = get_phone()
        birthday = get_birthday()
        yield models.Contact_book(name=name, phone=phone, birthday=birthday)
