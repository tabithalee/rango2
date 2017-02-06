from django.conf.urls import url
from wrango import views

urlpatterns=[
        url(r'^$',views.index,name='index'),
        url(r'^about/$',views.about,name='about'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
            views.show_category, name='show_category'),
        url(r'^page/(?P<page_name>[\w\-]+)/$', views.show_page, name='show_page'),

]
