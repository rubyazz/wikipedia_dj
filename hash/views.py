from django.shortcuts import render, get_object_or_404, redirect
import requests

from .forms import WordForm
from .models import *


def index(request):
    response = 'https://en.wikipedia.org/w/api.php?action=parse&page={}&format=json'

    if request.method == 'POST':
        form = WordForm(request.POST)
        form.save()

    form = WordForm()
    words = Word.objects.all()
    all_words = []
    for word in words:
        new_url = response.format(word.name).replace(' ', '_')
        res = requests.get(new_url).json()
        word_info = {
            'word': word.name,
            'title': res["parse"]["title"],
            'text': res["parse"]["text"]["*"],
            'pk': word.pk,
        }

        all_words.append(word_info)
    context = {'all_info': all_words, 'form': form}
    return render(request, "index.html", context)


def delete_word(request, pk):
    word = get_object_or_404(Word, pk=pk)
    word.delete()
    return redirect('home')