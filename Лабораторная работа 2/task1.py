money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0
agents = 0
while money_capital + agents > 0:
    agents = agents + (salary - spend)
    spend = spend * (1 + increase)
    count+=1
count-=1
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", count)
