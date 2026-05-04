from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# 🟢 REGISTRO
def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'registro.html', {'error': 'Usuario ya existe'})

        User.objects.create_user(username=username, password=password)

        return redirect('login')

    return render(request, 'registro.html')


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# 🟢 REGISTRO
def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'registro.html', {
                'mensaje': '❌ Usuario ya existe'
            })

        User.objects.create_user(username=username, password=password)

        return render(request, 'registro.html', {
            'mensaje': '✅ Usuario creado correctamente'
        })

    return render(request, 'registro.html')


# 🔐 LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            return render(request, 'login.html', {
                'mensaje': '❌ Credenciales incorrectas'
            })

    return render(request, 'login.html')


# 🏠 PÁGINA FINAL
@login_required
def inicio(request):
    return render(request, 'inicio.html')
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')