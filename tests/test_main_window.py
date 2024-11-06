import pytest
from app.mainWin import MainWin

@pytest.fixture
def main_win():
    return MainWin()

def test_widgets_existence(main_win):
    assert main_win.s_widget is not None
    assert main_win.an_widget is not None

def test_button_view_data(main_win):
    button = main_win.view_data_button
    assert button.text() == 'Просмотреть'

def test_button_add_data(main_win):
    button = main_win.add_data_button
    assert button.text() == 'Добавить'
