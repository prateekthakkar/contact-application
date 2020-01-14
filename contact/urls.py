"""contact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from contactapp import views
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header='Contact Admin'
admin.site.site_title='Contact Admin Portal'
admin.site.index_title='Welcome To Contact Admin Panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='Home'),
    path('Register/',views.Register,name='Register'),
    path('Login/',views.Login,name='Login'),
    path('Contact',views.Contact,name='Contact'),
    path('Logout/',views.Logout,name='Logout'),
    path('Contact_Insert/',views.Contact_Insert,name='Contact_Insert'),
    path('Edit/<int:c_id>',views.Edit,name='Edit'),
    path('Update/<int:c_id>',views.Update,name='Update'),
    path('Delete/<int:c_id>',views.Delete,name='Delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
