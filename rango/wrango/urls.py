from django.conf.urls import url
from wrango import views

urlpatterns=[
        url(r'^$',views.index,name='index'),
]
