from django.contrib import admin
from django.urls import path,include
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.home_page),
    path('',include('products.urls')),
    path('about/',views.about_page),
    path('contact/',views.contact_page),
    path('login/',views.login_page),
    path('register/',views.register_page),
    
]

if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
