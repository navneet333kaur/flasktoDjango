from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path('', views.home_view, name='home'),  # Add the home URL
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Keep existing URL
    # Add your productivity guide URLs
    path('productivity-guide/', views.ProductivityHomeView.as_view(), name='productivity_guide'),
    path('productivity-guide/topic/<slug:slug>/', views.TopicDetailView.as_view(), name='topic_detail'),
    path('productivity-guide/article/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
]
