from django.shortcuts import render

from django.http import HttpResponse
from random import randint

def home_view(request):
    # print("request:::", request.META)
    # print("request:::", request.HEADERS)
    # return HttpResponse('Ana sayfaya hosgeldiniz..')
    # context = {"platform": f"Django platformu kullanildi ve randint ile dönen veri: {randint(1,100)}"}
    context = dict()
    return render(request, "page/home_page.html", context)

def about_us_view (request):
    context = dict()
    return render(request,"page/about_us.html", context )
    
def contact_us_view (request):
    context = dict()
    return render(request,"page/contact_us.html", context )

