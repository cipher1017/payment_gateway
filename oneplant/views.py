from django.shortcuts import render, redirect
from .models import Comments
from .forms import CommentForm

from django.http import HttpResponse


def index(request):
    return render(request, "oneplant/index.html")
def home(request):
    return render(request, "oneplant/home.html")

def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_comment')
    else:
        form = CommentForm()
    comments = Comments.objects.all().order_by('-pub_date')
    return render(request, 'oneplant/add_comment.html', {'form': form, 'comments': comments})

def about(request):
    context = {
        'title': 'about us page'
    }
    return render(request, "oneplant/about.html", context)
