from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('book_now/', views.book, name='book'),
    path('pricing/', views.pricing, name='pricing'),
    path('service/', views.service, name='service'),
    path('blog-details/', views.blog_details, name='blog_details'),
]