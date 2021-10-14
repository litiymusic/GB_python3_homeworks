def thesaurus_adv(*names):
    names_dict = {}
    for name in sorted(names):
        n, s = name.split()
        val = names_dict.setdefault(s[0], {n[0]: [name]})
        n_val = val.setdefault(n[0], [name])
        if name not in n_val:
            n_val.append(name)
    return names_dict

print(thesaurus_adv("Иван Акимов", "Мария Швейцова", "Петр Коростылев", "Владимир Иванов", "Николай Басков", "Елизавета Павловна",
                    "Ольга Козлова", "Олег Кензов", "Владислав Курыгин", "Илья Боровчук"))