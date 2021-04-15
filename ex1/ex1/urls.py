"""ex1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.default, name="default"),
    path('admin/', admin.site.urls),
    path('books/', views.books, name="alinea_a"),
    path('book_details/<str:book_name>', views.book_details, name="alinea_b"),
    path('authors/', views.authors, name="alinea_c"),
    path('author_details/<str:author_name>', views.author_details, name="alinea_d"),
    path('publishers/', views.publishers, name="alinea_e"),
    path('publisher_details/<str:publisher_name>', views.publisher_details, name="alinea_f"),
    path('author_books/<str:author_name>', views.author_books, name="alinea_g"),
    path('publisher_authors/<str:publisher_name>', views.publisher_authors, name="alinea_h"),

    # Aula 4
    path('booksearch/', views.booksearch, name="booksearch"),
    path('booksearch2/', views.booksearch2, name="booksearch2"),
    path('author_search/', views.author_search, name="author_search"),
    path('author_publisher_search/', views.author_publisher_search, name="author_publisher_search"),
    path('insert_author/', views.insert_author, name="insert_author"),
    path('insert_publisher/', views.insert_publisher, name="insert_publisher"),
    path('insert_book/', views.insert_book, name="insert_book"),
    path('edit_author/', views.edit_author, name="edit_author"),

    # Aula 5
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name="logout"),

]
