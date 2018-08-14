from django.urls import path

from sk.views import index

urlpatterns = [
    path('', index.as_view(), name='index'),
]