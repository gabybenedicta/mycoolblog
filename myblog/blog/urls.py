from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^category/$',views.category, name='category'),
    url(r'^category/(?P<category_id>[0-9]+)/$',views.category_type, name= 'category_type'),
    url(r'^newcategory/$',views.newcategory, name='newcategory'),
    url(r'^admin/', views.admin, name='admin'),
    url(r'^allpost/$',views.allpost, name='allpost'),
    url(r'^allpost/(?P<post_id>[0-9]+)/$',views.onepost, name='onepost'),
    url(r'^newpost/$', views.newpost, name='newpost'),
    url(r'^newcomment/(?P<post_id>[0-9]+)/$', views.newcomment, name='newcomment'),
    url(r'signup/$', views.signup.as_view(), name='signup'),
    url(r'error/$',views.error, name= 'error'),
    
    
]