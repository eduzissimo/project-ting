from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file, instance: Queue):
    for item in instance._items:
        if item['nome_do_arquivo'] == path_file:
            return
    lines = txt_importer(path_file)

    if lines is None:
        return
    data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(lines),
        'linhas_do_arquivo': lines
    }
    instance.enqueue(data)
    print(data)


def remove(instance):
    if instance.is_empty():
        print('Não há elementos')
    else:
        file_remvd = instance.dequeue()
        print(f"Arquivo {file_remvd['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        file_data = instance.search(position)
        print(file_data)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
