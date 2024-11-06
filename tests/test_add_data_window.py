import pytest
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication
from database.scripts.db import Data
from app.addDataWin import AddDataWin


@pytest.fixture
def app(qtbot):
    test_app = QApplication([])
    window = AddDataWin()
    qtbot.addWidget(window)
    return window


def test_add_order_valid_data(app, qtbot):
    app.work_input.addItem(10, 1)
    app.executor_input.addItem(4, 1)
    app.status_input.addItem(1, 1)

    qtbot.keyClicks(app.acceptance_date_input, "2024-11-01")
    qtbot.keyClicks(app.customer_input, "Иван Смак")
    qtbot.keyClicks(app.description_input, "Замена термопасты")

    qtbot.mouseClick(app.add_button, Qt.LeftButton)

    assert app.db.data is not None


def test_update_order_valid_data(app, qtbot):
    existing_data = (1, 10, "Замена термопасты", "2024-11-01", "Иван Смак", 4, 1)
    app.data = existing_data
    app.upload_editable_data()

    qtbot.keyClicks(app.acceptance_date_input, "2024-11-02")
    qtbot.keyClicks(app.status_input, 2)

    qtbot.mouseClick(app.add_button, Qt.LeftButton)

    updated_order = app.db.get_all_orders(None, None)
    assert updated_order[0][3] == "2024-11-02"
    assert updated_order[0][6] == 2


def test_add_order_invalid_data(app, qtbot):
    app.work_input.addItem(10, 1)
    app.executor_input.addItem("Иван Смак", 1)
    app.status_input.addItem(1, 1)

    qtbot.keyClicks(app.acceptance_date_input, "Неправильная дата")

    qtbot.mouseClick(app.add_button, Qt.LeftButton)

    orders = app.db.get_all_orders(None, None)
    assert len(orders) == 0

