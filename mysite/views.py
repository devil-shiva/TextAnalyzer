# I have created this file - Shivam
from django.http import HttpResponse
from django.shortcuts import render
import string


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # getTExt
    djtext = request.POST.get('text', 'default')
    rempunc = request.POST.get('rempunc', 'off')
    remSpc = request.POST.get('spaceRem', 'off')
    capFirst = request.POST.get('capfirst', 'off')
    charcount = request.POST.get('charcount', 'off')
    caps = request.POST.get('capsAll', 'off')
    punctuations = string.punctuation

    # analyzeText
    result = ""
    if rempunc == "on":
        for x in djtext:
            if x in punctuations:
                continue

            else:
                result += x
    else:
        result = djtext
    if remSpc == "on":
        result = result.replace(" ", "")
    if caps == "on":
        for x in result:
            result = result.upper()
    if capFirst == "on":
        result = result.title()
    if charcount == "on":
        c = 0

        for x in djtext:
            if x != " ":
                c += 1
        result += " Character Count " + str(c)
    if rempunc != "on" and remSpc != "on" and caps != "on" and capFirst != "on" and charcount != "on":
        return HttpResponse("Error Select What To do")
    print(result)
    params = {'textEntered': djtext, 'analyzedText': result}
    return render(request, 'analyze.html', params)
