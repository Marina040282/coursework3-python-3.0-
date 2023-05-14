from pprint import pprint
from utils import get_data, get_filtrate_data, get_last_values, get_formed_data


def main():
    COUNT_VALUES = 5 #переменная для вывода определенного количества перевоов
    FILTERED_EMPTY_FROM = True #переменная для вывода необходимого или обратного значения

    data = get_data() #чтение и запись файла
    data = get_filtrate_data(data, FILTERED_EMPTY_FROM) #Фильтрация корректных значений
    data = get_last_values(data, COUNT_VALUES) #Сортировку данных по дате
    data = get_formed_data(data) #запись текста в необходимой форме

    for row in data:
        print(row, end='\n') #вывод текста на экран


if __name__ == "__main__":
    main()