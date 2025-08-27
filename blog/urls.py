from django.urls import path
from .views import home, post_detail, contact, register, sign_in, sign_out
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('blog/<int:post_id>', post_detail, name='post_detail'),
    path('contact/', contact, name='contact'),
    path('register', register, name='register'),
    path('login', sign_in, name='sign_in'),
    path('logout', sign_out, name='sign_out')
    ]


