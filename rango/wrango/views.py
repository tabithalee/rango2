from django.shortcuts import render
from django.http import HttpResponse
from wrango.models import Category
from wrango.models import Page

def index(request):
#Query database for list of all categories currently stored
#Order categories by no. likes, descending order
#Retrieve top 5 only / all if<5 entries
#Place list in context_dict to be passed to template engine

    category_list = Category.objects.order_by('-likes')[:5]
    
#    return HttpResponse("Rango says hey there partner! <br/><a href='/rango/about/'>About</a>")
#    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context = context_dict)

def about(request):
#    return HttpResponse("Rango says here is the about page. <br/><a href='/rango/'>Index</a>")
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    context_dict={}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context_dict)

def show_page(request, page_name):
    context_dict={}

    try:
        pages = Page.objects.get(slug=page_name)
        context_dict['pages'] = pages
    except Page.DoesNotExist:
        context_dict['pages'] = None
    return render(request, context_dict)
