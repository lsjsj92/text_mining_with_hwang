'''

트와이스,,,0,NNP,*,F,트와이스,*,*,*,*
기초과학,,,0,NNP,*,F,기초과학,*,*,*,*
'''

'''
['\ufeff홍준표,,,0,NNP,*,F,\ufeff홍준표,*,*,*,*'
뭐 이런게 나온다. 
with open('example.txt', 'r', encoding='utf-8-sig') as file:
이렇게 하면 된다고 한다.
'''
mecab_words = []
with open('word_dic_test.txt', encoding='utf-8-sig') as f:
    words = f.readlines()
    for word in words:
        word = word.strip()
        print(word)
        word = word+",,,0,NNP,*,F,"+word+",*,*,*,*"
        mecab_words.append(word)
print(mecab_words)
with open('user_dic_test.txt', 'a', encoding='utf-8') as f:
    for word in mecab_words:
        f.write(word+"\n")