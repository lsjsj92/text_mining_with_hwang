from django.shortcuts import render, redirect
from django.views import View
import subprocess
import json
from django.views import generic
from gensim.models import word2vec
import datetime
# Create your views here.
class HwangMain(View):
    
    def get(self, request, *args, **kwargs):
        template_name = 'main/home.html'
        return render(request, template_name)

    def post(self, request, *args, **kwargs):
        value = request.POST.get('python_value')
        try:
            output = subprocess.check_output(['python3.6', './hwang_main/subprocess/subprocessed.py', value], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            #raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
            log = "first error! %s  return code : %d Status : FAIL  %s  %s\n" % (str(datetime.datetime.now()), e.returncode, e.stderr, e.output)
            f = open("./hwang_main/log/subprocess_error.log", 'a', encoding='utf-8')
            f.write(log)

        origin_data = value
        with open('./hwang_main/subprocess/test.txt', 'r', encoding='utf8') as f:
            token_data = f.read()
        try:
            output = subprocess.check_output(['python3.6', './hwang_main/subprocess/keras_model.py', token_data], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e: 
            log = "second error! %s  return code : %d Status : FAIL  %s  %s\n" % (str(datetime.datetime.now()), e.returncode, e.stderr, e.output)
            f = open("./hwang_main/log/subprocess_error.log", 'a', encoding='utf-8')
            f.write(log)
        with open('./hwang_main/subprocess/jin3.txt', 'r', encoding='utf8') as f: category = f.read()
        pre = category
        cat = ''
        if pre[1] == "0" : cat = 'policy'
        if pre[1] == "1" : cat = 'economy'
        if pre[1] == "2" : cat = 'it'
        if pre[1] == "3" : cat = 'entertain'

        # tf-idf처리
        tf_idf_data = {}
        w2v = {}
        token_data_array = token_data.split(" ")

        with open('./hwang_main/subprocess/tf_idf_json.json', 'r', encoding='utf8') as f:
            data = json.load(f)

        for token in token_data_array:
            if token in data:
                if token in tf_idf_data: continue
                else : tf_idf_data[token] = '1'
        with open('./hwang_main/subprocess/tf_idf_json_test.json', 'w') as f:
            json.dump(tf_idf_data, f)
        #이제 이 키값과  word2vec 진행.
        w2v_model = word2vec.Word2Vec.load("./hwang_main/subprocess/word2vec.model")
        for key, value in tf_idf_data.items():
            word_dic={}
            try:
                wordlist = w2v_model.most_similar(positive=[key])
                for w in wordlist:
                    word_dic[w[0]] = w[1]
                w2v[key] = word_dic
            except:
                w2v[key] = word_dic
        template_name = 'main/after_input_value.html'
        return render(request, template_name, {'origin_data' : origin_data, 'token_data' : token_data, 'pre':pre, 'category':cat, 'tf_idf':tf_idf_data, 'w2v':w2v})
