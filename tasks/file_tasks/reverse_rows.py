"""
Написать функцию revert_rows, которая принимает путь к файлу и делает новый
файл. Создать новый файл, каждая строка которого получается из соответствующей
строки исходного файла перестановкой слов в обратном порядке.
"""


def revert_rows(path):
    with open('new_file.txt', 'a') as f1:
        for line in open(path):
            line = line.replace('\n', '')
            split_words = line.split(' ')
            split_words.reverse()
            inverted_line = ' '.join(split_words) + '\n'
            f1.write(inverted_line)


revert_rows('text.txt')
