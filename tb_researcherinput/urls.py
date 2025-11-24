from django.contrib import admin
from django.urls import path, include
from users.views import register
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # App principal
    path('', include('samples.urls')),
    # User auth
    path('registro/', register, name='register'),
    path('acceso/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

]

# Necesario para servir archivos subidos (archivo en Sample)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
