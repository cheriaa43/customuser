from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from home.forms import SignupForm, LoginForm
from custom_user.settings import AUTH_USER_MODEL
from django.contrib.auth.decorators import login_required
from user_custom.models import CustomUser

# Create your views here.
def index(request):
    return render(request, 'index.html', {'index_title': 'Custom User App', 'AUTH_USER_MODEL': AUTH_USER_MODEL})


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = CustomUser.objects.create_user(
                username=data.get('username'),
                password=data.get('password'),
                display_name=data.get('display_name'),
                age=data.get('age'),
                homepage=data.get('homepage')
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('home'))

    form = SignupForm()
    return render(request, 'generic_form.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(request, username=data.get('username'), password=data.get('password'))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
