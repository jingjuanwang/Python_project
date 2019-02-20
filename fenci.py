def get_content(path):
    with open(path, 'r', encoding='gbk', errors='ignore') as f:
        content = ''
        for l in f:
            l = l.strip()
            content += l
        return content

def get_TF(words, topK=10):
    tf_dic = {}
    for w in words:
        tf_dic[w] = tf_dic.get(w, 0) + 1
    return sorted(tf_dic.items(), key = lambda x:x[1], reverse = True)[:topK]


def main():
    import glob
    import random
    import jieba
    
    files = glob.glob('/home/sunao/pyfile/py_analysis/learning-nlp/chapter-3/data/news/C000013/*.txt')
    corpus = [get_content(x) for x in files]
    
    sample_inx = random.randint(0, len(corpus))
    split_words = list(jieba.cut(corpus[sample_inx]))
    print('sample', corpus[sample_inx])
    print('fenci', '/'.join(split_words))
    print('topK', get_TF(split_words))