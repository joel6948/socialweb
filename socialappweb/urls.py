"""socialappweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from socialgram import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.LoginView.as_view(),name='signin'),
    path('accounts/signup/',views.SignUpView.as_view(),name="signup"),
    path('home',views.HomeView.as_view(),name="home"),
    path('home/account/',views.UserDashboardView.as_view(),name='userdashboard'),
    path('home/<int:id>/add_like',views.add_like,name="add-like"),
    path('home/account/addpost/',views.PostAddView.as_view(),name='add-post'),
    path('home/account/logout/',views.signout,name='signout'),
    path('home/account/<int:id>/',views.PostDetailView.as_view(),name='post-detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
