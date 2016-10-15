from django.shortcuts import render, get_object_or_404, redirect
from django.utils.html import escape
from django.contrib.auth.models import Permission, User
from .models import Post, Label
from .forms import PostForm
from entry.models import Entry
from gallery.models import Image, Video
from profile.models import Profile
from django.contrib.auth import authenticate, login, logout

def index(request):
    entries = Entry.objects.all()
    images = Image.objects.all()
    videos = Video.objects.all()
    videos = Video.objects.all()
    labels = Label.objects.all()

    posts = Post.objects.all().order_by('-date')
    fixed_posts = Post.objects.filter(fixed=True).order_by('-date')
    normal_posts = Post.objects.filter(fixed=False).order_by('-date')

    text_form = PostForm(request.POST or None)
    
    # USAR ISSO AQUI
    text_form.fields['label'].widget.attrs['style'] = 'color:red;'
    text_form.fields['label'].widget.attrs['class'] = 'form-control'

    if text_form.is_valid():
        post = text_form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('home:index')

    args = {'entries': entries,
            'posts': posts,
            'fixed_posts': fixed_posts,
            'normal_posts': normal_posts,
            'images': images,
            'videos': videos,
            'labels': labels,
            'form': text_form}

    return render(request, 'home/index.html', args)

def user_login(request):
    print "Funcionou"
    return redirect('home:index')

def user_login(request):
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home:index')

    return render(request, 'home/login.html')

def user_logout(request):
    if request.user.is_authenticated():
        logout(request)

    return redirect('home:index')

def user_register(request):
    if request.user.is_authenticated():
        logout(request)

    return redirect('home:index')