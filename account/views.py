from django.shortcuts import render, redirect
from .models import Post, UserProfile, FeaturedPost, ReviewPost, Message, DailyReview
from django.contrib.auth.models import User, auth
from django.contrib import messages
# from django.contrib import messages

# Create your views here.
def index(request):
    post = Post.objects.all()
    reviewpost = ReviewPost.objects.all()
    dailypost = DailyReview.objects.all()
    posts = FeaturedPost.objects.all()
    return render(request, 'account/index.html', {'post': post, 'posts': posts, 'reviewpost': reviewpost, 'dailypost': dailypost})


def detail(request, slug):
    posts = Post.objects.get(slug=slug)
    context = {'post': posts}
    return render(request, 'account/detail.html', context)

def detailfeatured(request, slug):
    post = FeaturedPost.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'account/detailfeatured.html', context)

def about(request):
    return render(request, 'account/about.html')


def contact(request):
    if request.method == 'POST':
        contact = Message()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.subject = subject
        contact.message = message
        contact.save()
        messages.success(request, 'Thanks for Sending us a message, we will get back to you very soon!')
        return redirect('contact')
    return render(request, 'account/contact.html')

def pricing(request):
    return render(request, 'account/pricing.html')

def faq(request):
    return render(request, 'account/faq.html')

def portfolio(request):
    return render(request, 'account/portfolio.html')

def portfolioitem(request):
    return render(request, 'account/portfolioitem.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password==password2:
            if User.objects.filter(email=email).exists():
                return redirect('signup')
                messages.success(request, "Email already exists")
            elif User.objects.filter(username=username).exists():
                return redirect('signup')
                messages.success(request, "Username already exists")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "You Have Successfully Signed Up")

                # Login user
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                messages.success(request, "You Have Successfully Logged In")

                # then create new profile
                user_model = User.objects.get(username=username)
                new_profile = UserProfile.objects.create(user=user_model, id=user_model.id)
                new_profile.save()
                return redirect('index')
        else:
            return redirect('signup')
    else:
        return render(request, 'account/signup.html')


def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = UserProfile.objects.get(user=user_object)

    context = {'user_profile':user_profile}
    return render(request, 'account/profile.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.success(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'account/login.html')

