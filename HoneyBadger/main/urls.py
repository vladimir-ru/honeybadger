from .views import *
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path('', Main_Page.as_view(), name="main"),
    path('registration/', Reg_Page.as_view(), name="reg")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
