from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def index(request):
    # Rendre la page d'accueil sans nécessiter de connexion
    return render(request, 'accueil.html')

@login_required
def home(request):
    # Vue protégée par authentification qui pourrait être utilisée pour un tableau de bord utilisateur par exemple
    context = {'val': "Menu Accueil"}
    return render(request, 'accueil.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('studenthelp:post_list')  # Assurez-vous que cette URL est correctement définie dans l'application 'studenthelp'
        else:
            return render(request, 'registration/login.html', {'error': "Nom d'utilisateur ou mot de passe incorrect"})
    return render(request, 'registration/login.html')
