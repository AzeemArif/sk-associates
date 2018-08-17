from django.conf.urls.static import static
from django.urls import path

from sk.views import index
from skAssociates import settings

urlpatterns = [
    path('', index.as_view(), name='index'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)