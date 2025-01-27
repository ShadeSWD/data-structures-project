class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

    def __str__(self):
        """Магический метод для строкового представления объекта"""

        return self.data


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def __str__(self):
        return "" if self.head is None else "\n".join([str(item) for item in self])

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next_node

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """

        if self.head is None:
            new_node = Node(data=data, next_node=None)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data=data, next_node=None)
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.tail is None:
            return None

        removed_node = self.head
        self.head = removed_node.next_node

        if self.head is None:
            self.tail = None

        return removed_node.data
