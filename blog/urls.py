from django.urls import path
from blog.views import HomePageView, BlogDetailView, ContactsPageView, AboutPageView


urlpatterns = [
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path('', HomePageView.as_view(), name='home'),
    path('contacts', ContactsPageView.as_view(), name='contacts'),
    path('about', AboutPageView.as_view(), name='about'),
]