from keras.models import load_model
from keras.preprocessing import sequence
import pickle, sys
value = [sys.argv[1]]


with open('./textmining_main/subprocess/tokenizer.pickle', 'rb') as handle:
    tok = pickle.load(handle)

model = load_model('./textmining_main/subprocess/model/hwang_lstm.model')

token_data = value
sequence_data = tok.texts_to_sequences(token_data)
pad_sequence_data = sequence.pad_sequences(s, maxlen=500)
pre = model.predict_classes(pad_sequence_data)
with open('./hwang_main/subprocess/predict_result.txt', 'w', encoding='utf8') as f: f.write(str(pre))
pre = model.predict_proba(pad_sequence_data)
with open('./hwang_main/subprocess/predict_result_proba.txt', 'w', encoding='utf8') as f: f.write(str(pre))
