from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .forms import RegisterForm

def signup(request):
  forms = RegisterForm()

  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Account Created!!")
      return redirect('index')
  context = {'forms': forms}
  return render(request, 'core/signup.html', context)

