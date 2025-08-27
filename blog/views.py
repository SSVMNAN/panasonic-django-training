from django.shortcuts import render, redirect
from .models import Post
from .forms import contactForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    all_posts = Post.objects.all()

    context = {
        'posts': all_posts,
    }

    return render(request, 'blog/home.html', context)

@login_required(login_url='sign_in')
def post_detail(request, post_id):

    single_post = Post.objects.get(id=post_id)

    return render(request, 'blog/post_detail.html', {'post': single_post})


def contact(request):
    return render(request, 'blog/contact.html')

def contact(request):

    form = contactForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("home")
        
    else:
        form = contactForm()
        print("Form is not valid")
        print(form)
    return render(request, 'blog/contact.html', {'form': form})

def register(request):
    
    form = RegisterForm
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print("สมัครสมาชิกเรียบร้อย")
            return redirect('home')
    else:
        form = RegisterForm()
        print("แสดงฟอร์มเรียบร้อย")
        
    return render(request, 'blog/register.html', {'form': form})

def sign_in(request):

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            print
            return redirect('home')
        else:
            print("ไม่สามารถเข้าสู่ระบบได้")

    return render(request, 'blog/login.html')

def sign_out(request):
    logout(request)
    return redirect('home')