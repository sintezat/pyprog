import time

# глобальные переменные игры
name = ""
health = 100
inventory = []
has_mask = False
has_flippers = False
treasures_found = 0


def slow_print(text):
    """Медленный вывод текста"""
    for char in text:
        print(char, end='')
        time.sleep(0.03)
    print("\n")


def get_choice(options):
    """Выбор варианта"""
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")

    while True:
        try:
            choice = int(input("\nТвой выбор: "))
            if 1 <= choice <= len(options):
                return choice
            print(f"Введи 1-{len(options)}")
        except:
            print("Введи число!")


def start():
    """Начало игры"""
    global name

    slow_print("ПОДВОДНОЕ ПРИКЛЮЧЕНИЕ")

    name = input("Как тебя зовут? ").strip()
    if name == "":
        name = "Ныряльщик"

    slow_print(f"\nПривет, {name}!")
    slow_print("Ты ныряльщик, который ищет затонувшие сокровища.")
    slow_print("Сегодня ты нашел старую карту...")
    time.sleep(1)

    beach()


def beach():
    """Пляж - начало"""
    slow_print("\n ПЛЯЖ")
    slow_print("Ты стоишь на берегу океана. Что будешь делать?")

    choice = get_choice([
        "Нырнуть в воду",
        "Поискать на пляже",
        "Поговорить с рыбаком"
    ])

    if choice == 1:
        dive()
    elif choice == 2:
        search_beach()
    else:
        talk_fisherman()


def search_beach():
    """Поиск на пляже"""
    global inventory, has_mask

    slow_print("\nПОИСК НА ПЛЯЖЕ")
    slow_print("Ты идешь вдоль берега и находишь...")

    if not has_mask:
        slow_print("МАСКУ для подводного плавания!")
        inventory.append("Маска")
        has_mask = True
        slow_print("Получено: Маска")
    else:
        slow_print("Только старые ракушки...")

    slow_print("\nТы возвращаешься на пляж.")
    beach()


def talk_fisherman():
    """Разговор с рыбаком"""
    global inventory, has_flippers

    slow_print("\nРЫБАК")
    slow_print("Старый рыбак сидит с удочкой.")
    slow_print("'Привет, ныряльщик! Слышал, ты ищешь сокровища?'")

    choice = get_choice([
        "Спросить про сокровища",
        "Спросить про снаряжение",
        "Попрощаться"
    ])

    if choice == 1:
        slow_print("Рыбак: 'Говорят, в пещере у рифа есть золото!'")
        slow_print("Получена подсказка: ищи пещеру у кораллового рифа")
    elif choice == 2 and not has_flippers:
        slow_print("Рыбак: 'Вот тебе ласты, пригодятся под водой!'")
        inventory.append("Ласты")
        has_flippers = True
        slow_print("Получено: Ласты")
    else:
        slow_print("Рыбак: 'Удачи в поисках!'")

    beach()


def dive():
    """Погружение"""
    slow_print("\nПОГРУЖЕНИЕ")
    slow_print("Ты ныряешь в прозрачную воду...")
    time.sleep(1)

    if not has_mask:
        slow_print("Без маски ничего не видно! Ты возвращаешься на берег.")
        beach()
        return

    slow_print("Вокруг плавают красивые рыбки и кораллы.")

    choice = get_choice([
        "Плыть к коралловому рифу",
        "Плыть к затонувшему кораблю",
        "Плыть в темную пещеру"
    ])

    if choice == 1:
        coral_reef()
    elif choice == 2:
        sunken_ship()
    else:
        underwater_cave()


def coral_reef():
    """Коралловый риф"""
    global health

    slow_print("\nКОРАЛЛОВЫЙ РИФ")
    slow_print("Красивое место! Повсюду разноцветные кораллы.")

    choice = get_choice([
        "Искать сокровища",
        "Понаблюдать за рыбками",
        "Вернуться"
    ])

    if choice == 1:
        slow_print("Ты находишь старую монету в кораллах!")
        treasures_found += 1
        inventory.append("Старая монета")
        slow_print("Найдено сокровище!")
    elif choice == 2:
        slow_print("Ты видишь редкую рыбку-клоуна! Она показывает путь к пещере.")
        slow_print("Подсказка: пещера находится за большим кораллом")
    else:
        dive()


def sunken_ship():
    """Затонувший корабль"""
    global health

    slow_print("\nЗАТОНУВШИЙ КОРАБЛЬ")
    slow_print("Перед тобой старый корабль, покрытый водорослями.")

    choice = get_choice([
        "Заплыть внутрь",
        "Осмотреть снаружи",
        "Вернуться"
    ])

    if choice == 1:
        slow_print("Внутри темно и страшно...")

        if has_flippers:
            slow_print("С ластами ты быстро проплываешь и находишь сундук!")
            treasures_found += 2
            inventory.append("Сундук с золотом")
            slow_print("Найдено сокровище!")
        else:
            slow_print("Ты застреваешь в узком проходе и теряешь много воздуха!")
            health -= 40
            slow_print(f"Здоровье: {health}/100")

            if health <= 0:
                game_over("Ты не можешь продолжать поиски...")
                return
    else:
        dive()


def underwater_cave():
    """Подводная пещера"""
    global treasures_found

    slow_print("\nПОДВОДНАЯ ПЕЩЕРА")
    slow_print("Темная пещера. Вход охраняет огромный осьминог!")

    choice = get_choice([
        "Попробовать проплыть мимо",
        "Подружиться с осьминогом",
        "Вернуться"
    ])

    if choice == 1:
        slow_print("Осьминог выпускает чернила! Ты ничего не видишь и уплываешь.")
    elif choice == 2:
        slow_print("Ты даешь осьминогу ракушку. Он рад и пропускает тебя!")
        slow_print("В глубине пещеры ты находишь ЗОЛОТОЙ КУБОК!")
        treasures_found += 3
        inventory.append("Золотой кубок")
        slow_print("ВЕЛИКОЛЕПНОЕ СОКРОВИЩЕ!")
    else:
        dive()


def game_over(reason):
    """Конец игры"""
    slow_print(f"\n{reason}")
    play_again()


def final_ending():
    """Финальный подсчет"""
    slow_print("\nВОЗВРАЩЕНИЕ НА БЕРЕГ")
    slow_print(f"Ты выныриваешь на поверхность, {name}!")

    if treasures_found >= 5:
        slow_print("\nВЕЛИКОЛЕПНО!")
        slow_print("Ты нашел несметные сокровища!")
        slow_print("Все в порту говорят о твоей удаче!")
    elif treasures_found >= 2:
        slow_print("\nНЕПЛОХО!")
        slow_print("Ты нашел несколько ценных вещей.")
        slow_print("Теперь у тебя есть деньги на новое снаряжение!")
    elif treasures_found >= 1:
        slow_print("\nМАЛОВАТО...")
        slow_print("Ты нашел одну монету, но этого хватит на обед.")
        slow_print("В следующий раз повезет больше!")
    else:
        slow_print("\ПУСТО")
        slow_print("Ты ничего не нашел...")
        slow_print("Нужно больше тренироваться!")

    slow_print(f"\nСокровищ найдено: {treasures_found}")
    slow_print(f"Предметы: {inventory}")

    play_again()


def play_again():
    """Сыграть еще раз?"""
    choice = get_choice([
        "Сыграть еще раз",
        "Выйти"
    ])

    if choice == 1:
        # Сброс переменных
        global health, inventory, has_mask, has_flippers, treasures_found
        health = 100
        inventory = []
        has_mask = False
        has_flippers = False
        treasures_found = 0
        start()
    else:
        slow_print("\nСпасибо за игру! До встречи в океане!")


# Запуск
start()
