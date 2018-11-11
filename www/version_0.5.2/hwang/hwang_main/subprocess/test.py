from gensim.models import word2vec
model = word2vec.Word2Vec.load("./word2vec.model")
b = {}
cnt = 0
while True:

    word = input("단어를 입력해보세요! : ")
    if word == "":
        break
    try:
        a = model.most_similar(positive=[word])
        b[cnt] = a
        cnt += 1

    except:
        print("해당 되는 단어가 없습니다.")

print(b)
for key, value in b.items():
    for fuck in value:
        print(fuck[0], fuck[1])
