from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from loginapp.models import Profile
from loginapp.forms import ProfileForm, SignupForm

from django.contrib import messages


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!")
            return HttpResponseRedirect(reverse('loginapp:login'))

    return render(request, 'loginapp/signup.html', context={'form': form})


def loginuser(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('shopapp:home'))

    return render(request, 'loginapp/login.html', context={'form': form})


@login_required
def logoutuser(request):
    logout(request)
    messages.warning(request, "Logged Out")
    return HttpResponseRedirect(reverse('loginapp:login'))


@login_required
def userprofile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Profile has been updated!")
            form = ProfileForm(instance=profile)
            return HttpResponseRedirect(reverse('shopapp:home'))
    return render(request, 'loginapp/changeprofile.html', context={'form': form})
