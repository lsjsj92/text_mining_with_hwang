from keras.models import load_model
from keras.preprocessing import sequence
import pickle, sys
value = [sys.argv[1]]

#with open('./hwang_main/subprocess/test.txt', 'r', encoding='utf8') as f:
#    data = f.read()



with open('./hwang_main/subprocess/tokenizer.pickle', 'rb') as handle:
    tok = pickle.load(handle)

model = load_model('./hwang_main/subprocess/model/hwang_lstm.model')

#tok.fit_on_texts(token_data)
token_data2 = value
s = tok.texts_to_sequences(token_data2)
ss = sequence.pad_sequences(s, maxlen=500)
pre = model.predict_classes(ss)
with open('./hwang_main/subprocess/jin3.txt', 'w', encoding='utf8') as f: f.write(str(pre))
pre = model.predict_proba(ss)
with open('./hwang_main/subprocess/jin4.txt', 'w', encoding='utf8') as f: f.write(str(pre)) 
