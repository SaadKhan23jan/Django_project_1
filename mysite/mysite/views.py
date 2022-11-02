# Created by Saad Khan

from django.http import HttpResponse
from django.shortcuts import render
from plotly.offline import plot
import plotly.express as px


# def index(request):
#     return HttpResponse('''<a href="https://www.facebook.com", target="_blank">Facebook</a>''')
#
#
# def about(request):
#     return HttpResponse("About Saad Khan")

def index(request):
    # return HttpResponse("Home")

    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepun = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('removepunc', 'off')
    punctuations = '''!()-[];:'"\<>./!@#$%^&*_'''
    analyzed = ""

    if fullcaps == "on":
        djtext = djtext.upper()

    if removepun == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', context=params)
    else:
        return HttpResponse("Error")


