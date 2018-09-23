from django.shortcuts import render,redirect, get_object_or_404
from .models import User, Category, Post, Comment
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

# Create your views here.

#user creation
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def home(request):
    all_post = Post.objects.all()
    all_category = Category.objects.all()
    user_id = 1
    current_user= User.objects.get(pk=1)
    like_id=-1
    for i in request.POST:
        if(request.POST[i]=='Like'):
                like_id = i
                current_post= Post.objects.get(pk=like_id)
                current_post.likes += 1
                current_post.save()

    context={'all_post' : all_post,
            'all_category': all_category,
            'current_user': current_user,
        }
    return render(request,'blog/home.html',context)
    # if request.method=='POST':
    #     Users.username = request.POST['username']
    #     Users.password = request.POST['password']
    #     print(request.POST)
    #     user = authenticate(username = Users.username, password = Users.password)
    #     context={
    #         'all_post' : all_post,
    #         'all_category': all_category,
    #         'username':username,
    #         'password':password,
    #         'user':user,
    #         }
    #     if Users is not None:
    #         login(request, user)
    #         return render(request, 'blog/userhome.html',context)
    #     else:
    #         return render(request, 'blog/error.html', context)
    # else:
    #     context={
    #         'all_post' : all_post,
    #         'all_category': all_category,
    #         }
    #     return render(request, 'home.html', context)

def category(request):
    categories = Category.objects.all() #variable categories adalah semua category
    context = {
        'posts_count' : posts_count,
        'categories' : categories,
    }
    return render(request, 'blog/category.html', context)
def newcategory(request):
    try:
        new = Category(name = request.POST['category_name'],created_at = timezone.now())
        new.save()
        print(Category.objects.all())
        
        return HttpResponseRedirect(reverse('blog:category'))
    except:
        context={}
        return render(request, 'blog/newcategory.html',context)
    
def category_type(request, category_id):
    category_type= Category.objects.get(pk=category_id) #category_type= category1
    #mau display post di satu category
    post_in_category = category_type.post_set.all() #post in category 1= category1.post
    context={
        'category_type': category_type,
        'post_in_category': post_in_category,
        }
    return render(request,'blog/category_type.html',context)


def admin(request):
    return render(request, 'blog/admin.html',{})

def allpost(request):
    all_post = Post.objects.all()

    print(all_post)
    context={
        'all_post': all_post,
    }
    return render(request, 'blog/allpost.html',context)
def onepost(request,post_id):
    one_post= Post.objects.get(pk=post_id)
    comments_in_post = one_post.comment_set.all()
    number_of_likes= one_post.likes
    context={
        'one_post' : one_post,
        'comments_in_post' : comments_in_post,
    }
    return render(request, 'blog/onepost.html',context)

def newpost(request):
    all_category = Category.objects.all()
    post_title = request.POST.get('post_title',False)
    post_content= request.POST.get('post_content', False)
    context={
    }
    if(post_title == "" or post_content ==""):
        err_name =""
        err_desc =""
        if(post_title==""):
            err_name = "Please enter the post title"
        if(post_content ==""):
            err_desc = "Please enter the post description"
        context={
            'err_name': err_name,
            'err_desc': err_desc,
            'all_category': all_category,
        }
        return render(request, 'blog/newpost.html', context)
    elif(post_title ==False and post_content == False):
        context ={
            'all_category': all_category,
        }
        return render(request, 'blog/newpost.html', context)
    else:
        category_id = request.POST.get('category_id', False)
        user_id =1 #gabybenedicta
        print(category_id)
        new = Post(title = post_title, content= post_content,category_id=category_id, user_id= 1)
        new.save()
        print(request.POST['post_title'])
        all_post = Post.objects.all()
        all_category = Category.objects.all()
        context={
            'all_post' : all_post,
            'all_category': all_category,
        }
        return HttpResponseRedirect(reverse('blog:home'))

def newcomment(request,post_id):
    post_comment = request.POST.get('post_comment',False)
    print(post_id)
    post= get_object_or_404(Post, pk=post_id)

    if(post_comment==""):
        err_desc=""
        if(post_comment ==""):
            err_desc= "Please enter the post description"
            context = {
            'err_desc' : err_desc,
            }
        return render(request, 'blog/newcomment.html',context)
    #ga ada isinya
    elif(post_comment ==False):
        context={

        }
        return render(request,'blog/newcomment.html',context)
    else:
        user_id=1 #gabybenedicta
        new = Comment(user_id = 1, content= post_comment, post_id=post_id)
        new.save()
        print(request.POST['post_comment'])
        context={

        }
        return HttpResponseRedirect(reverse('blog:allpost'))

# def signup(request):
#     if request.method=='POST':
#         form = UserCreationForm(request.POST)
#         context={
#             'form' : form,
#         }
#         if form.is_valid():
#             form.save()
#             Users.username = form.cleaned_data.get('Username')
#             Users.password = form.cleaned_data.get('password1')
#             Users= authenticate(username=Users.username, password=Users.password)
#             login(request, Users)
#             return redirect('home')
#     else:
#         form= UserCreationForm()
#         context={
#             'form' : form,
#         }
#     return render(request, 'blog/signup.html',context)
class signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def error(request):
    return render(request,'blog/error.html',{})
