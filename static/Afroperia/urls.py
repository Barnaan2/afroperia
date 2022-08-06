"""Afroperia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from system_admin.views import login_page,register,logout_page

urlpatterns = [
    path('', include('customer.urls')),
    path('login/', login_page, name='login'),
    path('register/', register, name='register'),
    # path('edit/', views.update_profile, name='edit'),
    path('logout/', logout_page, name='logout'),
    # path('admin/', admin.site.urls),
    path('system_admin/', include('system_admin.urls')),
    path('hotel/', include('hotel.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
