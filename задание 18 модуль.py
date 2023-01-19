price_of_tickets = 0
tickets = int(input("Введите количество билетов:"))
x = [i for i in range(tickets)]
age = {}
for a in x:
    age[a] = int(input("Введите возраст:"))
for a, age_of_buyer in age.items():
    if age_of_buyer < 18:
        price_of_tickets += 0
    elif 18 >= age_of_buyer < 25:
        price_of_tickets += 990
    elif age_of_buyer >= 25:
        price_of_tickets += 1390
if tickets > 3:
    price_of_tickets *= 0.9
print(f'Сумма к оплате: {price_of_tickets} руб.')