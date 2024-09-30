from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('article/<str:slug>', views.detail, name='detail'),
    path('articles/<str:slug>', views.detailfeatured, name='detail-featured'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('pricing', views.pricing, name='pricing'),
    path('faq', views.faq, name='faq'),
    path('signup', views.signup, name='signup'),
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]