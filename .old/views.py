from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm, LoginForm
from .models import User  # Importe seu modelo User

def signup(request):

    # Verificamos se o método da solicitação é POST
    if request.method == 'POST':

        # Verificamos se o formulário foi enviado com os dados corretos
        form = UserForm(request.POST)

        if form.is_valid():

            # Salvar os dados do formulário no banco de dados
            form.save()

            # Redirecionar para a página de login após o cadastro
            return redirect('login')
    else:

        # Caso o formulário não tenha sido enviado com os dados corretos
        form = UserForm()

    return render(request, 'signup.html', {'form': form})

def login(request):

    # Verificamos se o método da solicitação é POST
    if request.method == 'POST':

        # Verificamos se o formulário foi enviado com os dados corretos
        form = LoginForm(request.POST)

        if form.is_valid():

            # Recuperar os dados do formulário
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:

                user = User.objects.get(email=email)
                user_id = user.id
                
            except User.DoesNotExist:
                user = None
                user_id = None

            print('user')
            print(user)
            print('user_id')
            print(user.id)
            print('user_email')
            print(user.email)
            print('user_password')
            print(user.password)

            # Autenticar o usuário com as credenciais enviadas pelo formulário
            #user = authenticate(request, email=email, password=password)

            # Verificar se o usuário existe no banco de dados
            #if user is not None:
            
            #if user is not None and user.check_password(password):

            # Não utilizar a checkgem padrão do Django
            if user_id is not None and password == user.password:

                # Autentica o usuário
                # Caso a autenticação seja bem-sucedida, armazenar os dados do usuário na sessão do usuário
                #login(request, user)  # Aqui está a correção
                #login(request)  # Aqui está a correção
                # Redireciona para a página inicial ou outra página após o login bem-sucedido
                #return redirect('home')

                print("Usuário ID encontrado:", user_id)  # Mensagem de depuração

                # Autentica o usuário manualmente usando a função authenticate()
                authenticated_user = authenticate(request, email=email, password=password)

                print("Usuário autenticado:", authenticated_user)  # Mensagem de depuração

                if authenticated_user is not None:

                    # Se o usuário for autenticado com sucesso, inicia a sessão manualmente
                    request.session.set_expiry(86400)  # Define a duração da sessão em segundos (86400 segundos = 1 dia)
                    request.session['user_id'] = user.id  # Armazena o ID do usuário na sessão

                    print('user_id')
                    print(user.id)

                    login(request, authenticated_user)  # Autenticar o usuário

                    return redirect('home')
                
                else:
                    form.add_error(None, 'Credenciais inválidas. Por favor, tente novamente.')
                
            else:
                # Caso as credenciais estejam incorretas
                form.add_error(None, 'Credenciais inválidas. Por favor, tente novamente.')
    else:
        # Caso o formulário não tenha sido enviado com os dados corretos
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



