from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.views import login,logout
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Bagian
from .forms import PostForm, CommentForm
from .fungsi import halaman, entrilog, dellog, Totalposting
import blog

def main_view(request):
	bagians = Bagian.objects.all()
	return render(request, 'mainweb/main_view.html', {'bagians':bagians})

def login_adm(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return redirect('/adm/blog/post')
        else:
            stat = 'bukanadmin'
            logout(request)
            return render(request, 'registration/login.html', {'stat':stat})
    else:
        return login(request)

def logout_adm(request):
    logout(request)
    return redirect('login_adm')

@user_passes_test(lambda u:u.is_staff, login_url='/adm/')
def adm_profil(request):
    if request.user.is_authenticated():
        return render(request, 'mainweb/adm_profil.html')
    else:
        return login_adm(request)

@user_passes_test(lambda u:u.is_staff, login_url='/adm/')
def adm_blog_post(request):
    if request.user.is_authenticated():
        posts_list  = blog.models.Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
        users       = User.objects.all()
        posts       = halaman(request,posts_list,10)
        return render(request, 'mainweb/adm_blog.html', 
        {'posts' : posts, 'totposts': Totalposting().totposts, 'totpubs' : Totalposting().totpubs,
        'totunpubs' : Totalposting().totunpubs, 'users' :users })
    else:
        return login_adm(request)

@user_passes_test(lambda u:u.is_staff, login_url='/adm/')
def adm_blog_user(request):
    if request.user.is_authenticated():
        return render(request, 'mainweb/adm_blog_user.html')
    else:
        return login_adm(request)

@user_passes_test(lambda u:u.is_staff, login_url='/adm/')
def adm_blog_post_detail(request, pk):
    post = get_object_or_404(blog.models.Post, pk=pk)
    return render(request, 'mainweb/adm_blog_post_detail.html',{'post':post})

@user_passes_test(lambda u:u.is_staff, login_url='/adm/')
def adm_blog_post_edit(request, pk):
    post = get_object_or_404(blog.models.Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if 'Publikasi' in request.POST:
                post.published_date = timezone.now()
            post.save()
            return redirect('/adm/blog/post')
    else:
        form = PostForm(instance=post)
    return render(request, 'mainweb/adm_blog_post_edit.html', {'form': form, 'totposts': Totalposting().totposts,
        'totpubs' : Totalposting().totpubs,
        'totunpubs' : Totalposting().totunpubs })
