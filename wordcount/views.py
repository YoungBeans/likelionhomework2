from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def result(request):
    text = request.GET['text']
    words = text.split()
    words_dictionary = {}
    for word in words :
        if word in words_dictionary:
            words_dictionary[word] += 1
        else:
            words_dictionary[word] = 1
    context = {'text':text, 'words':words, 'total':len(words), 'dictionary':words_dictionary.items()}
    return render(request, 'wordcount/result.html', context)