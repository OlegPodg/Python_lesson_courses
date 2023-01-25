""" Проверить является ли слова анаграммами - перестановка букв в слове, дающая новое слово"""


def anagram(word1, word2):
    if sorted(word1) == sorted(word2):
        print("Эти слова - анаграммы!")
    else:
        print("Слова не являются анаграммами!")


word_user1 = input("Введите первое слово: ")
word_user2 = input("Введите второе слово: ")

anagram(word_user1, word_user2)
