from L3_smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79110001112"),
    Smartphone("Samsung", "Galaxy S24", "+79244440088"),
    Smartphone("One", "Plus 12", "+79996669966"),
    Smartphone("Xiaomi", "14 Ultra", "+79212221199"),
    Smartphone("Google", "Pixel 8", "+79269996666")
]
for phone in catalog:
    print(f"{phone.brend} - {phone.model}. {phone.number}")