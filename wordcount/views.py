from django.shortcuts import render
from django.http import HttpResponse
import operator


def home(request):
    return render(request, 'home.html')
    
    
def count(request):
    fulltext = request.GET['fulltext']
    
    wordlist = fulltext.split()
    
    countdict = {}
    for word in wordlist:
        if word in countdict:
            countdict[word] += 1
        else:
            countdict[word] = 1
   
    sortedwords = sorted(countdict.items(), key=operator.itemgetter(1), reverse=True) 
    
    return render (request, 'count.html', {'fulltext': fulltext, 'count':len(wordlist), 'sortedwords': sortedwords})


def about(request):
    return render(request, 'about.html')

    
#def eggs(request):
#    return HttpResponse('<h1>Eggs are just great</h1>')