import pytest

from task.models import Browser, Computer, BrowserComputer


@pytest.fixture
def data():
    computers = [
        Computer(1, "PC1"),
        Computer(2, "PC2"),
    ]

    browsers = [
        Browser(1, "Chrome", 120, 1),
        Browser(2, "Firefox", 118, 1),
        Browser(3, "Браузеров", 5, 2),
    ]

    relations = [
        BrowserComputer(1, 1),
        BrowserComputer(1, 2),
        BrowserComputer(2, 3),
    ]

    return browsers, computers, relations
