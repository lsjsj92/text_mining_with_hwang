from django.shortcuts import render, redirect
from django.views import generic

# Create your views here.
class HwangMain(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'main/home.html'
        return render(request, template_name)
