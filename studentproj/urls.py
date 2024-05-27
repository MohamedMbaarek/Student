from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Vue index redirigeant vers accueil.html sans exigence de connexion
      path('accueil/', views.home, name='accueil'),  # Vue d'accueil, nécessitant une connexion
    path('accounts/login/', views.login_view, name='login'),
  
    
    path('studenthelp/', include('studenthelp.urls')),  # Inclusion des URLs de l'application 'studenthelp'
]
