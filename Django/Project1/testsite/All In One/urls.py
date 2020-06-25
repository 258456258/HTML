from django.urls import path
from django.contrib import admin
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
   
    path('analyze',views.analyze,name="analyze")
