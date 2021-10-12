prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]

print(f"\n\n{'*' * 60}\n")

for i in prices:
    rub, kop = int(i // 1), f"{i % 1:.02f}"[2:]
    print(f"{rub} руб {kop} коп,", end=" ")

print(f"\n\n{'*' * 60}\n")
print(f"ID до сортировки: {id(prices)} - {prices}")
prices.sort()
print(f"ID после сортировки по возр.: {id(prices)} - {prices}")

print(f"\n\n{'*' * 60}\n")
n_list = sorted(prices, reverse=True)
print(f"ID после сортировки по убыван.: {id(n_list)} - {n_list}")

print(f"\n\n{'*' * 60}\n")
print(f"{n_list[:5][::-1]}")