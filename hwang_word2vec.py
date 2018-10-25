from gensim.models import word2vec
import gensim
import glob, os
import pandas as pd
import numpy as np


data_6m = pd.read_csv('./6m/6m_after_prepro.csv')
X_6m = data_6m.iloc[:, 1].values
model = gensim.models.Word2Vec(size=130, window=10, min_count=10, iter=5, sg=1)
model.build_vocab(X_6m)
model.train(X_6m, epochs=model.iter, total_examples=model.corpus_count)
print("6month end")

data_7m = pd.read_csv('./7m/7m_after_prepro.csv')
X_7m = data_7m.iloc[:, 1].values
model.build_vocab(X_7m, update=True)
model.train(X_7m, epochs=model.iter, total_examples=model.corpus_count)
print("7month end")

data_8m = pd.read_csv('./8m/8m_after_prepro.csv')
X_8m = data_8m.iloc[:, 1].values
model.build_vocab(X_8m, update=True)
model.train(X_8m, epochs=model.iter, total_examples=model.corpus_count)
print("8month end")

data_9m = pd.read_csv('./9m/9m_after_prepro.csv')
X_9m = data_9m.iloc[:, 1].values
model.build_vocab(X_9m, update=True)
model.train(X_9m, epochs=model.iter, total_examples=model.corpus_count)
print("9month end")

model.save('./word2vec.model')