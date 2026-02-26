from .views import IndexPage
from django.urls import path

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
]
