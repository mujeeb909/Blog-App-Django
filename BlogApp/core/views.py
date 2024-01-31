from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import RegisterForm, UpdateProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signup(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created!!")
            return redirect('login')
        else:
            # Display form errors
            messages.error(request, "Form submission failed. Please check the form.")
    
    context = {'form': form}
    return render(request, 'core/signup.html', context)

def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email = email, password = password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, "Invalid Email or Password!")
            return redirect('login')
    context = {}
    return render(request, 'core/login.html', context)

def signout(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'core/profile.html', context)

@login_required(login_url='login')
def update_profile(request):
    if request.user.is_authenticated:
        user= request.user
        forms = UpdateProfileForm(instance=user)
        if request.method == 'POST':
            forms = UpdateProfileForm(request.POST, request.FILES, instance=user)
            if forms.is_valid():
                forms.save()
                messages.success(request, 'Profile updated successfully')
                return redirect('profile')
        
    
    context = {'forms': forms}
    return render(request, 'core/update_profile.html', context)