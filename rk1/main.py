class Browser:
    def __init__(self, id, name, version, computer_id):
        self.id = id
        self.name = name
        self.version = version  # количественный признак
        self.computer_id = computer_id


class Computer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class BrowserComputer:
    def __init__(self, computer_id, browser_id):
        self.computer_id = computer_id
        self.browser_id = browser_id


computers = [
    Computer(1, "Игровой ПК 'Омега'"),
    Computer(2, "Ноутбук 'Lenovo IdeaPad'"),
    Computer(3, "Сервер 'Atlas'"),
    Computer(4, "Рабочая станция 'Delta'"),
]

browsers = [
    Browser(1, "Google Chrome", 120, 1),
    Browser(2, "Mozilla Firefox", 118, 1),
    Browser(3, "Яндекс.Браузер", 23, 2),
    Browser(4, "Opera", 102, 3),
    Browser(5, "Edge", 115, 4),
    Browser(6, "Браузеров", 5, 4),
]

browsers_computers = [
    BrowserComputer(1, 1),
    BrowserComputer(1, 2),
    BrowserComputer(2, 3),
    BrowserComputer(3, 4),
    BrowserComputer(4, 5),
    BrowserComputer(4, 6),
    BrowserComputer(1, 3),
    BrowserComputer(2, 1),
]


def main():
    # 1) Один-ко-многим
    one_to_many = [
        (b.name, b.version, c.name)
        for b in browsers
        for c in computers
        if b.computer_id == c.id
    ]

    print("--- Запрос Б1 ---")
    print("Список связанных браузеров и компьютеров (1:M), отсортированный по имени браузера:")
    res1 = sorted(one_to_many, key=lambda x: x[0])
    for browser, version, computer in res1:
        print(f"  Браузер: {browser}, Версия: {version}, Компьютер: {computer}")

    print("\n--- Запрос Б2 ---")
    print("Список компьютеров с количеством браузеров в каждом (1:M), отсортированный по количеству:")

    res2 = []
    for c in computers:
        count = len(list(filter(lambda x: x[2] == c.name, one_to_many)))
        if count > 0:
            res2.append((c.name, count))

    res2.sort(key=lambda x: x[1])
    for name, count in res2:
        print(f"  Компьютер: {name}, Количество браузеров: {count}")

    print("\n--- Запрос Б3 ---")
    print("Список браузеров, имя которых заканчивается на 'ов', и компьютеры (M:M):")

    many_to_many_temp = [
        (c.name, bc.computer_id, bc.browser_id)
        for c in computers
        for bc in browsers_computers
        if c.id == bc.computer_id
    ]

    many_to_many = [
        (b.name, comp_name)
        for comp_name, comp_id, browser_id in many_to_many_temp
        for b in browsers
        if b.id == browser_id
    ]

    res3 = sorted(
        [(name, comp) for name, comp in many_to_many if name.endswith("ов")],
        key=lambda x: x[0]
    )

    for browser, computer in res3:
        print(f"  Браузер: {browser}, Компьютер: {computer}")


if __name__ == "__main__":
    main()
