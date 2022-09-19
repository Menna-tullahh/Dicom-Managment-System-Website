"""
Definition of urls for DicomRecords.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views, create_fhir
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/',
         LoginView.as_view
         (
             template_name='app/index.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
path('login/about/',
         views.about, name='about'),
    path('', LoginView.as_view
         (
             template_name='app/index.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('contact/', views.contact, name='contact'),

    path('about/', views.about, name='about'),

    path('logout/', LogoutView.as_view(next_page='/login'), name='logout'),
    path('admin/', admin.site.urls),
    path('about/sp_contact/<con_id>', views.sp_contact),
    # path('about/sp_contact/image/', views.showImg),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)