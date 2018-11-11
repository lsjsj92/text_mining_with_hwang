'''

트와이스,,,0,NNP,*,F,트와이스,*,*,*,*
기초과학,,,0,NNP,*,F,기초과학,*,*,*,*
'''

mecab_words = []
with open('word_dic.txt', encoding='utf-8-sig') as f:
    words = f.readlines()
    for word in words:
        word = word.strip()
        word = word+",,,0,NNP,*,F,"+word+",*,*,*,*"
        mecab_words.append(word)
with open('user_dic.txt', 'a', encoding='utf-8') as f:
    for word in mecab_words:
        f.write(word+"\n")