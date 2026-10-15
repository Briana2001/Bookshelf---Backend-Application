from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, ProfileEditForm


def login_view(request):
    # If already logged in, no reason to show the login form
    if request.user.is_authenticated:
        return redirect('shelf:home')

    if request.method == 'POST':
        # AuthenticationForm validates username + password against the DB.
        # First arg is request (for session/auth hooks), second is the data.
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()          # pulls the User out of the form
            login(request, user)            # create the session
            messages.success(request, f'Welcome back, {user.username}!')

            # If they were bounced here by @login_required, ?next= is the page
            # they were trying to reach. Send them there instead of home.
            next_url = request.GET.get('next') or request.POST.get('next')
            return redirect(next_url or 'shelf:home')
    else:
        form = AuthenticationForm(request)

    return render(request, 'account/login.html', {'form': form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('shelf:home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)            # log them in right after registering
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('shelf:home')
    else:
        form = RegisterForm()

    return render(request, 'account/register.html', {'form': form})


def logout_view(request):
    # Only allow logout via POST for CSRF safety — a GET logout means any
    # image tag on any site could log your users out.
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out.')
        return redirect('shelf:home')
    return redirect('shelf:home')


@login_required
def profile_view(request):
    # request.user is guaranteed to be a real User here because
    # @login_required bounced anonymous visitors to the login page.
    return render(request, 'account/profile.html', {'profile_user': request.user})


@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated.')
            return redirect('account:profile')
    else:
        form = ProfileEditForm(instance=request.user)

    return render(request, 'account/profile_edit.html', {'form': form})