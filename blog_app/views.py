from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def show(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'show.html', {'article': article})


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = ArticleForm()
        return render(request, 'create.html', {'form': form})
    

def delete(request, id):
    entry = get_object_or_404(Article, id=id)
    if request.method == "POST":
        entry.delete()
        return redirect(index)
    else:
        return render(request, 'delete.html', {'entry': entry})
    

def update(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = ArticleForm(instance=article)
        return render(request, 'create.html', {'form': form})
