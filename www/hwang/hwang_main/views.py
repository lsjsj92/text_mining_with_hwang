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
        print(value)
        try:
            print("!"*100)
            output = subprocess.check_output(['python', './hwang_main/subprocess/subprocessed.py', value], stderr=subprocess.STDOUT)
            print("@" * 100)
        except subprocess.CalledProcessError as e:
            print("#" * 100)
            #raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
            log = "error!  return code : %d Status : FAIL  %s  %s\n" % (e.returncode, e.stderr, e.output)
            print('error!!!!!!!!!!!!   ',log)
            f = open("./hwang_main/log/subprocess_error.log", 'a', encoding='utf-8')
            f.write(log)
        print("$" * 100)
        template_name = 'main/after_input_value.html'
        return render(request, template_name)
