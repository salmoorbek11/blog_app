from django.views.generic import ListView, DetailView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class ContactsPageView(ListView):
    model = Post
    template_name = 'contacts.html'

class AboutPageView(ListView):
    model = Post
    template_name = 'about.html'