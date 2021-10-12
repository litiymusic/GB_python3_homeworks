duration = int(input("Введите время в секундах: "))

days = duration // 3600 // 24
hours = duration // 3600 - days * 24
minutes = duration // 60 % 60
seconds = duration % 60

print("Дней: ", days, ",", " Часов: ", hours, ",", " Минут: ", minutes, ",", " Секунд: ", seconds, ".", sep="")
