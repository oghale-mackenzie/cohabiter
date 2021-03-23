"""shareflatweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from shareflatapp import views as shareflatapp_views # < here

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', shareflatapp_views.index, name='index'), # < here
	path('login/', shareflatapp_views.user_login, name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('home', shareflatapp_views.dashboard, name='dashboard'),
	path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
	path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
	# reset password urls
	path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
	path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
	path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
	path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
	path('register/', shareflatapp_views.register, name='register'),
	path('edit/', shareflatapp_views.edit, name='edit'),
]

admin.site.site_header = "ShareFlat Admin"
admin.site.site_title = "ShareFlat Admin Portal"
admin.site.index_title = "Welcome to ShareFlat Admin Portal"
