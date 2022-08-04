# I have created this file - Hashman
from django.http import HttpResponse
from django.shortcuts import render
from sympy import numbered_symbols


def index(request):
    # return HttpResponse('''<h1>hello bhai</h1><a href=https://www.reddit.com/r/popular?geo_filter=GLOBAL/>reddit web link</a>''')
    return render(request, 'index.html')


def about(request):
    # return HttpResponse('''yeh about page hai <br> <a href=http://127.0.0.1:8000/> BACK</a>''')
    return render(request, "about_template.html")


def new_page(request):
    return HttpResponse('''<h>naya page bana lia !!</h><br><a href=http://127.0.0.1:8000/> yeh index page ka link hai </a>  ''')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    print(djtext)
    # checkbox values
    removepunc = request.POST.get('removepunc', 'on')
    char_count = request.POST.get('char_count', 'on')
    character_capitilization = request.POST.get(
        'Character_capitilization', 'on')
    # check which checkbox is on
    if (removepunc == "on"):
        punctuations = r'''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    # yeh Character counter hai
    elif (char_count == 'on'):
        analyzed = len(djtext)
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    # Character ko uppercase main convert kerta hai yeh
    elif (character_capitilization == 'on'):
        analyzed = ''
        analyzed += djtext.upper()
        params = {'purpose': 'Character Capitilization',
                  'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif removepunc == 'on' or char_count == 'on' or character_capitilization == 'on':
        params = {'purpose': 'result of multiple checkboxes',
                  'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')
