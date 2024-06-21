def find_word_occurrences(file_data, word, include_content):
    word = word.lower()
    occurrences = [
        {"linha": j + 1, "conteudo": line} if include_content
        else {"linha": j + 1}
        for j, line in enumerate(file_data["linhas_do_arquivo"])
        if word in line.lower()
    ]
    return occurrences


def get_search(word, instance, include_content=False):
    result = []
    for i in range(len(instance)):
        file_data = instance.search(i)
        occurrences = find_word_occurrences(file_data, word, include_content)
        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": file_data["nome_do_arquivo"],
                "ocorrencias": occurrences,
            })
    return result


def exists_word(word, instance):
    return get_search(word, instance)


def search_by_word(word, instance):
    return get_search(word, instance, include_content=True)
