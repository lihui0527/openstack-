from django.conf.urls import url
from . import views
urlpatterns =[
    url(r'^$',views.index,name='index'),
    url(r'^post/(\w+)/$',views.show_post,name='show_post'),
]
