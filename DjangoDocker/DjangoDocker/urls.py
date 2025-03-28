from django.contrib import admin
from django.urls import path
from TestApp.views import TestApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TestApiView.as_view(), name='api'),
]