

from django.shortcuts import render, HttpResponseRedirect, reverse

from django.contrib import messages
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

def home_view(request):
    articles = Article.objects.filter(is_active=True).order_by("-id")[:3]
    context = {"articles": articles}
    return render(request, "index.html", context)

def about_view(request):
    articles = Article.objects.filter(is_active=True).order_by("-id")
    context = {"articles": articles}
    return render(request, "about.html", context)

def product_view(request):
    articles = Article.objects.filter(is_active=True).order_by("-id")
    context = {"articles": articles}
    return render(request, "product.html", context)

def contact_view(request):
    articles = Article.objects.filter(is_active=True).order_by("-id")
    context = {"articles": articles}
    return render(request, "contact.html", context)

# def dukon_view(request):
    # articles = Article.objects.filter(is_active=True).order_by("-id")
    # context = {"articles": articles}
    # return render(request, "contact.html", context)
#  def article_detail(request, id):
#     article = Article.objects.get(id=id)

#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data["first_name"]
#             text = form.cleaned_data["text"]
        
#             comment = Comment(
#                 first_name=first_name,
#                 text=text,
#                 article=article
#             )
#             comment.save()
#             messages.success(request, 'Comment posted successfully')

#     comments = Comment.objects.filter(article=id)
#     form = CommentForm()
#     context = {"about": article, "comments": comments, "form": form}
#     return render(request, "about.html", context)

def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']

            article = Article(
                title=title,
                description=description,
                image=image,
            )
            article.save()
            messages.success(request, 'Your article has been submitted successfully. It will be published after review.')
            return HttpResponseRedirect(reverse('articles-list'))
        else:
            messages.error(request, 'Please fill in the form correctly.')
    else:
        form = ArticleForm()
    context = {"form": form}
    
    return render(request, "create_article.html", context)


from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

def home_view(request):
    articles = Article.objects.filter(is_active=True).order_by("-id")[:3]
    context = {"articles": articles}
    return render(request, "index.html", context)

def about_view(request):
    articles = Article.objects.filter(is_active=True).order_by("-id")
    context = {"articles": articles}
    return render(request, "about.html", context)

def product_view(request):
    articles = Article.objects.filter(is_active=True).order_by("-id")
    context = {"articles": articles}
    return render(request, "product.html", context)

def contact_view(request):
    articles = Article.objects.filter(is_active=True).order_by("-id")
    context = {"articles": articles}
    return render(request, "contact.html", context)

def testimonial_view(request):
    return render(request, "testimonial.html")

def article_detail(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            text = form.cleaned_data["text"]
            comment = Comment(
                first_name=first_name,
                text=text,
                article=article
            )
            comment.save()
            messages.success(request, 'Comment posted successfully')
            return HttpResponseRedirect(reverse('article-detail', args=[id]))  # Redirect to the same page after posting comment
    else:
        form = CommentForm()
    comments = Comment.objects.filter(article=id)
    context = {"about": article, "comments": comments, "form": form}
    return render(request, "about.html", context)

def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            article = Article(
                title=title,
                description=description,
                image=image,
            )
            article.save()
            messages.success(request, 'Your article has been submitted successfully. It will be published after review.')
            return HttpResponseRedirect(reverse('articles-list'))
        else:
            messages.error(request, 'Please fill in the form correctly.')
    else:
        form = ArticleForm()
    context = {"form": form}
    return render(request, "create_article.html", context)
