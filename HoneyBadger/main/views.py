from django.shortcuts import render, HttpResponse
from django.views.generic import View


class Main_Page(View):
    
    
    def get(self, request):
        
        return render(request, 'pages/main.html', {})


class Reg_Page(View):

    def get(self, request):


        return render(request, 'pages/reg.html', {})