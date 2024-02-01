from django.shortcuts import render
from .models import Blog
from django.contrib.auth.decorators import login_required
from .forms import CreateBlogForm
from django.utils.text import slugify
from django.shortcuts import redirect
from django.contrib import messages

def index(request):
  featured_blog = Blog.objects.filter(featured=True).first()
  blogs = Blog.objects.filter(featured = False)
  context = {"blogs": blogs, 'featured_blog': featured_blog}
  return render(request, 'blogapp/index.html', context)

def detail(request, slug):
  blog = Blog.objects.get(slug=slug)
  context = {'blog': blog}
  return render(request, 'blogapp/detail.html', context)

@login_required(login_url='login')
def create_article(request):
    form=CreateBlogForm()
    if request.method == 'POST':
        form = CreateBlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.slug = slugify(request.POST["title"])
            blog.user = request.user
            blog.save()
            messages.success(request, "Article created successfully!")
            return redirect("profile")
    context = {"form": form}
    return render(request, "blogapp/create.html", context)

