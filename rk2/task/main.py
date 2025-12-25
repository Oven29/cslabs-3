from models import Browser, Computer, BrowserComputer
from queries import *

def main():
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

    browser_computers = [
        BrowserComputer(1, 1),
        BrowserComputer(1, 2),
        BrowserComputer(2, 3),
        BrowserComputer(3, 4),
        BrowserComputer(4, 5),
        BrowserComputer(4, 6),
        BrowserComputer(1, 3),
        BrowserComputer(2, 1),
    ]

    res1 = query_one_to_many(browsers, computers)
    res2 = query_computers_with_browser_count(res1)
    res3 = query_many_to_many(browsers, computers, browser_computers)

    print(res1)
    print(res2)
    print(res3)

if __name__ == "__main__":
    main()
