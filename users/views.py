from users.forms import EmailLoginForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from users.models import CustomUser
from django.shortcuts import render, redirect



def user_login(request):
    error_message = None
    if request.method == "POST":
        form = EmailLoginForm(request.POST)
        email = request.POST.get('email')

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is None:
                try:
                    CustomUser.objects.get(email=email)
                    error_message = "Senha inválida"
                except CustomUser.DoesNotExist:
                    error_message = "E-mail invalido"

                return render(request, "login.html", {"form": form, "error_message": error_message })
            
            login(request, user)
            return redirect("home")

    else:
        form = EmailLoginForm()

    return render(request, "login.html", {"form": form, 'error_message': error_message})



def user_register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data["email"]
            user.set_password(form.cleaned_data["password1"])
            user.save()
            user = authenticate(request, username=user.email, email=user.email, password=form.cleaned_data["password1"])
            if user is not None:
                login(request, user)
                return redirect("login")
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {"form": form})




@login_required
def home(request):
    return render(request, "main.html")




def user_logout(request):
    logout(request)
    return redirect("login")