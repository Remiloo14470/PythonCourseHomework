class WordsFinder:
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            with open(file, encoding='utf-8') as f:
                strs = f.read().lower()
                symbols_to_remove = [',', '.', '=', '!', '?', ':', ';', '-']
                for symbol in symbols_to_remove:
                    strs = strs.replace(symbol, "")
                list1 = strs.split()
            all_words[file] = list1
        return all_words

    def find(self, word):
        new_dict = {}
        word_lower = word.lower()
        for name, words in self.get_all_words().items():
            for wrd in words:
                if word_lower == wrd:
                    index = words.index(wrd)
                    new_dict[name] = index
                    return new_dict

    def count(self, word):
        new_dict = {}
        word_lower = word.lower()
        for name, words in self.get_all_words().items():
            for wrd in words:
                if word_lower == wrd:
                    word_count = words.count(wrd)
                    new_dict[name] = word_count
                    return new_dict

finder2 = WordsFinder('test.txt', 'products.txt')
print(finder2.get_all_words())
print(finder2.find('кодировку'))
print(finder2.count('potato'))
