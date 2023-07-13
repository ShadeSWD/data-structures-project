import pytest
from src.linked_list import *


@pytest.fixture()
def node1():
    return Node(5)


@pytest.fixture()
def node2(node1):
    node = Node('a')
    node.next_node = node1
    return node


@pytest.fixture()
def empty_linked_list():
    return LinkedList()


def test_node_init(node1, node2):
    assert node1.data == 5
    assert node2.data == 'a'


def test_linked_list_init(empty_linked_list):
    assert empty_linked_list.head is None


def test_linked_list_insert_beginning(empty_linked_list):
    empty_linked_list.insert_beginning({'id': 1})
    empty_linked_list.insert_beginning({'id': 0})
    assert empty_linked_list.head.data == {'id': 0}


def test_linked_list_insert_at_end(empty_linked_list):
    empty_linked_list.insert_at_end({'id': 2})
    empty_linked_list.insert_at_end({'id': 3})
    assert empty_linked_list.head.data == {'id': 2}


def test_linked_list_str(empty_linked_list):
    assert str(empty_linked_list) == 'None'
    empty_linked_list.insert_beginning({'id': 1})
    empty_linked_list.insert_at_end({'id': 2})
    empty_linked_list.insert_at_end({'id': 3})
    empty_linked_list.insert_beginning({'id': 0})
    assert str(empty_linked_list) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"


def test_linked_list_to_list(empty_linked_list):
    empty_linked_list.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    empty_linked_list.insert_at_end({'id': 2, 'username': 'mik.roz'})
    empty_linked_list.insert_at_end({'id': 3, 'username': 'mosh_s'})
    empty_linked_list.insert_at_end('idusername')
    empty_linked_list.insert_at_end([1, 2, 3])
    empty_linked_list.insert_beginning({'id': 0, 'username': 'serebro'})

    # метод to_list()
    lst = empty_linked_list.to_list()
    assert lst == [{'id': 0, 'username': 'serebro'}, {'id': 1, 'username': 'lazzy508509'},
                   {'id': 2, 'username': 'mik.roz'}, {'id': 3, 'username': 'mosh_s'}]


def test_linked_list_get_data_by_id(empty_linked_list):
    empty_linked_list.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    empty_linked_list.insert_at_end({'id': 2, 'username': 'mik.roz'})
    empty_linked_list.insert_at_end({'id': 3, 'username': 'mosh_s'})
    empty_linked_list.insert_beginning({'id': 0, 'username': 'serebro'})
    empty_linked_list.insert_at_end({'id': 2, 'username': 'mosh_s'})

    assert empty_linked_list.get_data_by_id(2) == {'id': 2, 'username': 'mik.roz'}
