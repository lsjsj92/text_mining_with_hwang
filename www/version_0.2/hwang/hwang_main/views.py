from django.shortcuts import render, redirect
from django.views import View
import subprocess
from django.views import generic
import json
from gensim.models import word2vec
import gensim

# Create your views here.
class HwangMain(View):
    def get(self, request, *args, **kwargs):
        template_name = 'main/home.html'
        return render(request, template_name)

    def post(self, request, *args, **kwargs):
        value = request.POST.get('python_value')
        try:
            output = subprocess.check_output(['python', './hwang_main/subprocess/subprocessed.py', value], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            #raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
            log = "error!  return code : %d Status : FAIL  %s  %s\n" % (e.returncode, e.stderr, e.output)
            f = open("./hwang_main/log/subprocess_error.log", 'a', encoding='utf-8')
            f.write(log)

        origin_data = value
        with open('./hwang_main/subprocess/test.txt', 'r', encoding='utf8') as f:
            token_data = f.read()

        '''
            여기서 로직 
            1. 가지고온 토크나이즈 된 데이터와 tf-idf값 비교한다. (웬만하면 상위 10개만)
                1-1. 여기서 로직.
                    - 6~9월에 나온 데이터(배열)값을 dict로 만든다.
                    - 즉, 중복 데이터 제거.
                    - 이걸 json 파일로 저장하고 가지고 온다.
                    - 이 json 파일과 토크나이즈 된 데이터와 비교하는 것.
            2. 비교한 데이터 중 상위 3개만 관련된 연관 단어 키워드 시각화.


        '''
        tf_idf_data = {}
        w2v = {}
        token_data_array = token_data.split(" ")

        with open('./hwang_main/subprocess/tf_idf_json.json', 'r') as f:
            data = json.load(f)

        for token in token_data_array:
            if token in data:
                if token in tf_idf_data: continue
                else : tf_idf_data[token] = '1'

        #이제 이 키값과  word2vec 진행.
        w2v_model = word2vec.Word2Vec.load("./hwang_main/subprocess/word2vec.model")
        for key, value in tf_idf_data.items():
            word_dic = {}
            try:
                wordlist = w2v_model.most_similar(positive=[key])
                for w in wordlist:
                    word_dic[w[0]] = w[1]
                w2v[key] = word_dic
            except:
                w2v[key] = word_dic
        print(w2v)
        template_name = 'main/after_input_value.html'
        return render(request, template_name, {'origin_data' : origin_data, 'token_data' : token_data, 'tf_idf':tf_idf_data, 'w2v':w2v})
