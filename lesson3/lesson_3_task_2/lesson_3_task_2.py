from lesson3.lesson_3_task_2.smartphone import Smartphone

catalog = [
    Smartphone("Xiaomi", "Redmi 3", "+35794401111"),
    Smartphone("Xiaomi", "Redmi 7", "+35794401111"),
    Smartphone("Xiaomi", "Redmi 5", "+35794401111"),
    Smartphone("Xiaomi", "Redmi 4", "+35794401111"),
    Smartphone("Xiaomi", "Redmi 9", "+35794401111")
]

for smartphone in catalog:
    print(f"{smartphone.vendor}-{smartphone.model}-{smartphone.phone}")
