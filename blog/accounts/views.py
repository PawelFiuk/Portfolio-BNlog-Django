from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)      # tworzymy uchwyt do stworzenia uzytkownika
        if form.is_valid():
            form.save() # zapisuje uzytkownika do bazy danych, po sprawdzeniu czy istnieje
            return redirect('articles:list')     # jezeli wszystko bedzie ok dojdzie do przekierowania uzytkownika
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # logowanie uzytkownika
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')  # po zalogowaniu przekieruj na podany URL
    else:
        form = AuthenticationForm()      # jezeli uzytkownik nie jest zarejestrowany uzyskaj autoryzacje
    return render(request, "login.html", {"form": form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')
