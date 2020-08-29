from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from .views import homepageview,product_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "shop"

urlpatterns = [
    path('',homepageview.as_view(), name='home'),
    path('product/<int:pk>',product_view.as_view(), name='product_view'),
    path('about',TemplateView.as_view(template_name='about.html')),
    path('contact',TemplateView.as_view(template_name='contact.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
