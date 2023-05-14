from utils import get_data, get_filtrate_data, get_last_values, get_formed_data

""" 
Тестирование функции, отвечающей за чтение и запись файла
"""


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


"""
Тестирование функции, отвечающей за фильтрацию значений 
"""


def test_get_filtrate_data(test_data):
    assert len(get_filtrate_data(test_data[:5], filtered_empty_from=False)) == 3
    assert len(get_filtrate_data(test_data[:5], filtered_empty_from=True)) == 3


"""
Тестирование функции, отвечающей за сортировку данных
"""


def test_get_last_values(test_data):
    data = get_last_values(test_data, 5)
    assert [x["date"] for x in data] == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364', '2019-04-04T23:20:05.206878', '2019-03-23T01:09:46.296404', '2018-06-30T02:08:58.425572']


"""
Тестирование функции, отвечающей за вывод текста
"""


def test_get_formed_data(test_data):
    data = get_formed_data(test_data[:1])
    assert data == ['\n26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n        ']