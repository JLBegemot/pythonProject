from lesson3.lesson_3_task_3.address import Address
from lesson3.lesson_3_task_3.mailing import Mailing


def print_mail(mail: Mailing):
    print(
        f"Отправление {mail.track} из {mail.from_address.zip}, "
        f"{mail.from_address.city}, {mail.from_address.street}, {mail.from_address.home} - {mail.from_address.apartment} "
        f"в {mail.to_address.zip}, {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.home} -{mail.to_address.apartment}. "
        f"Стоимость {mail.cost} рублей.")


mail = Mailing(
    Address(
        141700,
        "Moscow",
        "Lenina",
        "1/1",
        "1"
    ),
    Address(
        141700,
        "Moscow",
        "Lenina",
        "1/1",
        "2"
    ),
    "brrrbrrbbb"
)

print_mail(mail)

mail_second = Mailing(
    Address(
        141700,
        "Moscow",
        "Lenina",
        "1/1",
        "1"
    ),
    Address(
        141700,
        "Moscow",
        "Lenina",
        "1/1",
        "777"
    ),
    "brrrbrrbbb777"
)

mail_second.set_cost(777)

print_mail(mail_second)
