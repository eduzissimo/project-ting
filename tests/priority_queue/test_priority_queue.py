import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    pq = PriorityQueue()
    mock = [
        {
            "nome_do_arquivo": "arq1.txt",
            "qtd_linhas": 6,
            "linhas_do_arquivo": [""] * 6,
        },
        {
            "nome_do_arquivo": "arq2.txt",
            "qtd_linhas": 1,
            "linhas_do_arquivo": [""] * 1,
        },
        {
            "nome_do_arquivo": "arq3.txt",
            "qtd_linhas": 3,
            "linhas_do_arquivo": [""] * 3,
        },
    ]
    expected_mock = [1, 3, 6]

    for file in mock:
        pq.enqueue(file)

    assert len(pq) == 3

    for item, expected_test in enumerate(expected_mock):
        assert pq.search(item)["qtd_linhas"] == expected_test

    assert pq.dequeue() == mock[1]
    assert len(pq) == len(mock) - 1

    with pytest.raises(IndexError):
        pq.search(3)
