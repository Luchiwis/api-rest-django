from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/<int:a>/', views.index),
    path('api/', views.index),
    path('', lambda req: redirect('api/'))
]
