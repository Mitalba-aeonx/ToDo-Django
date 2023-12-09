from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login as login_user,logout
from django.contrib.auth.decorators import login_required 
from todo_app.forms import TodoForm
from todo_app.models import TODO
# Create your views here.
@login_required(login_url='login')
def home(request):
     if request.user.is_authenticated:
        user = request.user
        form = TodoForm()
        todos = TODO.objects.filter(user=user)
        return render(request,"index.html",context={'form':form , 'todos':todos})

def signup(request):
   if request.method == "GET":
        form = UserCreationForm()
        context = {
            "form":form
        }
        return render(request,"signup.html",context=context)
   
   else:
       form = UserCreationForm(request.POST)
       context = {
            "form":form
        }
       if form.is_valid():
           print(form.error_messages)
           user = form.save()
           print(user)
           if user is not None:
               return redirect('login')
               
       else:
        return render(request,"signup.html",context=context)
       

def login(request):
    if request.method =='GET':
        form = AuthenticationForm()
        context = {
            "form":form 
        }
        
        return render(request,"login.html",context=context)

    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=user_name,password=password)
            if user is not None:
                login_user(request,user)
                return redirect('home')
        else:
            context = {
            "form":form 
            }
            
            return render(request,"login.html",context=context)

@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TodoForm(request.POST)
        context = {
                "form":form 
                }
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('home')
        else:
            return render(request,"index.html",context=context)
       

def signout(request):
    logout(request)
    return redirect('login')

def delete_todo(request,id):
    TODO.objects.get(pk=id).delete()
    return redirect('home')



def update_status(request,id,is_completed):
    db_todo = TODO.objects.get(pk=id)
    db_todo.is_completed = is_completed
    db_todo.save()
    return redirect('home')


@login_required(login_url='login')
def update_todo(request, id):
    todo = get_object_or_404(TODO, pk=id)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm(instance=todo)

    context = {
        'form': form,
        'todo': todo,
    }
    return render(request, 'update_todo.html', context)