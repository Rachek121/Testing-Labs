import pytest
from PyQt6.QtWidgets import QApplication
from app.viewDataWin import ViewDataWin
from database.scripts.db import Data

@pytest.fixture
def app(qtbot):
    """Fixture to create a PyQt application."""
    test_app = QApplication([])
    window = ViewDataWin()
    qtbot.addWidget(window)
    window.show()
    return window

@pytest.fixture
def mock_database(mocker):
    """Fixture to mock methods of the Data class."""
    mock_data = mocker.patch.object(Data, 'get_all_orders', return_value=[
        (1, 10, 'Чистка компьютера', '2024-11-01', 'Иван Смак', 4, 1)
    ])
    mocker.patch.object(Data, 'delete_order', return_value="Запись удалена")
    return mock_data

def test_display_data(app, mock_database):
    """Тест на отображение данных в таблице."""
    app.load_data()
    assert app.table.rowCount() == 1
    assert app.table.item(0, 1).text() == 10

def test_delete_data(app, mock_database):
    """Тест на удаление данных в таблице."""
    app.load_data()
    assert app.table.rowCount() == 1
    app.table.selectRow(0)
    app.delite_order()
    assert app.table.rowCount() == 0

def test_update_data(app, mock_database):
    """Тест для проверки обновления данных в таблице."""
    app.load_data()
    assert app.table.rowCount() == 1
    app.edit_entry.click()
    app.load_data()
    assert app.table.item(0, 1).text() == 10

