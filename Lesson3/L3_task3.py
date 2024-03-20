from L3_address import Address
from L3_mail import Mailing

to_address = Address("682920", "пгт.Хор", "ул.Ленина", "12", "23")
from_address = Address("196244", "Санкт-Петербург", "проспект Космонавтов", "50", "4")
mailing = Mailing(to_address, from_address, "RU682277243567", 1500)

print(f"Отправление {mailing.track} из {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house} - {to_address.apartment} в {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house} - {from_address.apartment}. Стоимость {mailing.cost} рублей.")