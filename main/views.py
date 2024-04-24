from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import * 
from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_user
from django.contrib.auth import login
from .models import UserUpdate
from django.contrib import messages

 

def home_page(request):    
    
    data = {}

    return render(request , 'home.html' , data)


def login_page(request):
    data = {}
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request , user)
            return HttpResponseRedirect("")
        else:
            messages.error(request, "Вы ввели данные неверно!")
            return HttpResponseRedirect("")


    return render(request , 'accounts/login.html' , data)
    

def registration_page(request):
    if request.user.is_authenticated : 
        return redirect("profile")
    try : 
        if request.method == "POST":
            if len(request.POST["phone"]) == 16  :
                replace_dict= {"(": "", ")": "" ,"-":"",}
                phone = request.POST['phone']
                for old, new in replace_dict.items():
                    phone = phone.replace(old, new)
                if User.objects.filter(username=request.POST['username']).exists() : 
                    messages.error(request, "Пользователь уже существует!")
                    return HttpResponseRedirect(request.path_info)

                new_user  = User.objects.create_user(username=request.POST['username'])
                new_user_Update , created_u = UserUpdate.objects.get_or_create(user = new_user ,type_of_account=request.POST['type_of_account'] , phone = phone)                
                if new_user : 
                    new_user.set_password(request.POST['password'])
                    new_user.first_name=request.POST['first_name']
                    new_user.last_name=request.POST['last_name']
                    new_user.save()
                new_user_Update.save()
                login(request , new_user)
                return HttpResponseRedirect("")
    except Exception as e : 
        print(e)

    data = {
        "type_of_account":UserUpdate.TYPE_OF_ACCOUNT,
        "form" : UserForm() ,
    }

    return render(request , 'accounts/registration.html' , data)


@login_required
def logout(request):
    logout_user(request)
    return redirect("home")



@login_required(redirect_field_name= "login")
def profile_page(request):
    
    try : 
        if request.method == "POST" :
            user = request.user
            user.username =request.POST["username"] 
            user.first_name =request.POST["first_name"] 
            user.last_name =request.POST["last_name"] 
            user.save()
            messages.success(request, "Данные успешно обновлены!")
            return HttpResponseRedirect(request.path_info)

    except Exception as e:
        print(e)
        messages.info(request, "Ошибка сервера!")
        return HttpResponseRedirect(request.path_info)


    data = {
        "userUpdate" :UserUpdate.objects.get(user = request.user)
    }

    return render(request , 'accounts/profile.html' , data)