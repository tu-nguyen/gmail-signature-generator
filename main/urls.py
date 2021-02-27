from django.urls import path
# from . import views
from .views import HomePageView, CreatePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('home/', HomePageView.as_view(), name='home'),
    path('create/', CreatePageView.as_view(), name='create'),
]