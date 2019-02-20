class IMM(object):
    def __init__(self, dic_path):
        self.dictionary = set()
        self.maximum = 0
        #read dict
        with open(dic_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # None,False,0,空列表[],空字典{},空元祖(),都相当于false
                if not line:
                    continue
                self.dictionary.add(line)
                self.maximum = len(line)
                
    def cut(self, text):
        result = []
        index = len(text)
        while index > 0:
            print(index)
            word = None
            for size in range(self.maximum, 0, -1):
                if index - size < 0:
                    continue
                piece = text[(index - size):index]
                if piece in self.dictionary:
                    word = piece
                    print(word)
                    result.append(word)
                    index -= size
                    break
            if word is None:
                index -= 1
        return result[::-1]