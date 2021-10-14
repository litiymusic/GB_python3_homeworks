translate = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
             "six": "шесть", "sуven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}

def translate_number(word):
    return translate.get(word)

print(translate_number(input("Напишите словом любое число от 0 до 10: ")))