class Word:
    def __init__(self, word, separated_word):
        self.word = word
        self.seperated_word = separated_word

    def word(self):
        return f"{self.word}"


def get_word_and_list():
    f = open('wordlist.txt')
    new_word = f.readline()
    word_list = list(new_word)
    # print(new_word)
    # print(word_list)
    word = Word(new_word, word_list)
    f.close()
    return word


get_word_and_list()
