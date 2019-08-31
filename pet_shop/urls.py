from django.urls import path
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from pet import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('pets/list/', views.list, name = "pet-list"),
    path('pets/<int:pet_id>/', views.detail, name = 'pet-detail'),

    path('pets/create', views.create, name = 'pet-create'),
	path('pets/<int:pet_id>/update/', views.update, name = 'pet-update'),
    path('pets/<int:pet_id>/delete/', views.delete, name = 'pet-delete'),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)
