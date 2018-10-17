from django.shortcuts import render, redirect
from django.views import View
import subprocess
from django.views import generic

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
        template_name = 'main/after_input_value.html'
        return render(request, template_name, {'origin_data' : origin_data, 'token_data' : token_data})
