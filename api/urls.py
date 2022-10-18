from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/<str:a>/', views.index),
    path('', lambda req: redirect('api/'))
]
