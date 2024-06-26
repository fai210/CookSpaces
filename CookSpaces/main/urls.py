from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
    path("", views.home, name="home"),
    path("delete/<kitchen_id>", views.delete_kitchen, name="delete_kitchen"),
    path("articles/", views.all_article, name="articles"),
    path("articles/detail/<kitchen_id>", views.article_detail, name="article_detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('contact/messages', views.messages, name='message'),
    path("reviews/add/<kitchen_id>", views.add_review, name="add_review"),
]