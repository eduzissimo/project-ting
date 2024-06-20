from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._items = []
    # Método que retorna o tamanho da fila

    def __len__(self):
        return len(self._items)
    # retorna se a fila está vazia

    def enqueue(self, value):
        self._items.append(value)
    # adiciona elemento na fila

    def dequeue(self):
        if not self._items:
            return None
        return self._items.pop(0)
    # remove o primeiro elemento da fila

    def search(self, index):
        if index < 0 or index >= len(self._items):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._items[index]
    # busca
