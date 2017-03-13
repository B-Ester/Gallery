from .forms import PhotoForm
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from gallery.models import Photo

def home(request):
    article = Photo.objects.all()
    context = {
        'articles': article
    }
    return render(request, 'gallery/home.html', context)

def upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            flag_img_saved = True
            form = PhotoForm()
            # do something.
    else:
        form = PhotoForm()
        flag_img_saved = False
    context = {
        "flag_img": flag_img_saved,
        "form_photo": form
    }
    return render(request, "gallery/upload.html", context)

def about(request):
    return render(request, 'gallery/about.html')

def addlike(request, article_id):
    try:
        if article_id in request.COOKIES:
            redirect('/')
        else:
            article = Photo.objects.get(id = article_id)
            article.likes += 1
            article.save()
            response = redirect('/')
            response.set_cookie(article_id, 'test')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

def article(request, article_id):
    article = get_object_or_404(Photo, id=article_id)
    return render(request, 'gallery/article.html' , { 'article' : article , 'username': auth.get_user(request).username })

