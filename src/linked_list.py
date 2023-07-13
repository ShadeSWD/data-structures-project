class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = None

    def __str__(self):
        return self.data


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        """Конструктор класса LinkedList"""
        self.head = None

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next_node

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if type(data) == dict:
            new_node = Node(data=data)
            new_node.next_node = self.head
            self.head = new_node
        else:
            print("Неверный тип данных")

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if type(data) == dict:
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                last = self.head
                while last.next_node:
                    last = last.next_node
                last.next_node = new_node
        else:
            print("Неверный тип данных")

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self):
        return [node.data for node in self]

    def get_data_by_id(self, value) -> dict | None:
        """
        Метод для получения первого словаря с указанным значением ключа 'id' из списка

        :param value: значение 'id' для поиска
        :return: словарь с указанным значением 'id' или None, если такого словаря не найдено
        """
        for node in self:
            try:
                if node.data['id'] == value:
                    return node.data
            except (TypeError, KeyError):
                print("Данные не являются словарем или в словаре нет id.")
        return None
