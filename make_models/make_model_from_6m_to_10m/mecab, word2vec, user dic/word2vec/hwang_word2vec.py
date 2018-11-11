from gensim.models import word2vec
import gensim
import glob, os
import pandas as pd
import numpy as np


data_6m = pd.read_csv('./6m/6m_after_prepro.csv')
X_6m = data_6m.iloc[:, 1].values

str =[]

for s in X_6m:
    before_pre = s.split(" ")
    str.append(before_pre)

model = gensim.models.Word2Vec(size=130, window=10, min_count=10, iter=5, sg=1)
model.build_vocab(str)
model.train(str, epochs=model.iter, total_examples=model.corpus_count)
print("6month end")

data_7m = pd.read_csv('./7m/7m_after_prepro.csv')
X_7m = data_7m.iloc[:, 1].values

str =[]

for s in X_7m:
    before_pre = s.split(" ")
    str.append(before_pre)

model.build_vocab(str, update=True)
model.train(str, epochs=model.iter, total_examples=model.corpus_count)
print("7month end")

data_8m = pd.read_csv('./8m/8m_after_prepro.csv')
X_8m = data_8m.iloc[:, 1].values

str =[]

for s in X_8m:
    before_pre = s.split(" ")
    str.append(before_pre)

model.build_vocab(str, update=True)
model.train(str, epochs=model.iter, total_examples=model.corpus_count)
print("8month end")

data_9m = pd.read_csv('./9m/9m_after_prepro.csv')
X_9m = data_9m.iloc[:, 1].values

str =[]

for s in X_9m:
    before_pre = s.split(" ")
    str.append(before_pre)

model.build_vocab(str, update=True)
model.train(str, epochs=model.iter, total_examples=model.corpus_count)
print("9month end")

model.save('./word2vec.model')