import json
from datetime import datetime


def get_data():
    """ Функция - открытие и чтение файла json """
    with open("operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_filtrate_data(data,filtered_empty_from):
    """ Функфия фильтрует данные списка, чтобы статус перевода был выполнен """
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    return data


def get_last_values(data, count_values):
    """ Функция сортирует список по дате и запись 5 последних из них """
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:count_values]


def get_formed_data(data):
    """ Функция выводит на экран список из 5 последних выполненных клиентом операций в формате:
    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>"""

    formated_data = []
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]
        if "from" in row:
            sender = row["from"].split()
            from_bill = sender.pop(-1)
            from_bill = f"{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}"
            from_info = "".join(sender)
        else:
            from_info, from_bill = "Счет скрыт", ""
        recipient = row["to"].split()
        recipient_bill = recipient.pop(-1)
        recipient_bill = f"**{recipient_bill[-4:]}"
        to_info = " ".join(recipient)
        amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"
        formated_data.append(f"""
{date} {description}
{from_info} {from_bill} -> {to_info} {recipient_bill}
{amount}
        """)
    return formated_data
