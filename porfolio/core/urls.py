from .views import IndexPage,ContactView
from django.urls import path

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact')
]
