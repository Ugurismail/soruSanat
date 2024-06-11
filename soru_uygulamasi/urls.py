from django.contrib import admin
from django.urls import path
from sorular import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ana_sayfa, name='ana_sayfa'),
    path('soru/<int:soru_id>/', views.soru_detay, name='soru_detay'),
]
