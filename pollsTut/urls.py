
from django.contrib import admin
from django.urls import include, path
from .views import home
from accounts.views import login_view, register_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('accounts/login/', login_view, name='login'),
    path('accounts/register/', register_view, name='register'),
    path('accounts/logout/', login_view, name='logout'),
    path('polls/', include('polls.urls'))
]
