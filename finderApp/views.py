
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .models import Lawyer
from .forms import LawyerForm


# Main routes
def index(request):
    todos = Todo.objects.all().order_by('text')
    users = User.objects.all()

    if request.method == 'GET':
        # Display all teh todos
        if request.user.is_authenticated:
            print("Logged in")
            return render(request, 
                'finderapp/index.html',
                { 
                    'todos': todos,
                    'users': users
                })
        else:
            print("Not logged in")
            return render(request, 'finderapp/signup.html')
    elif request.method == 'POST':
        # Add a new todo
        try:
            user_id = request.POST['userid']
        except:
            return render(request, 
                '/finderapp/index.html',
                {
                    'error': 'You must select a user',
                    'todos': todos,
                    'users': users,
                })
        else:
            new_todo = Todo()
            new_todo.text = request.POST['text']
            new_todo.user = User.objects.get(pk=user_id)
            new_todo.save()
        return redirect('index')

def index2(request):
    return render(request, 'finderapp/index2.html')

def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('index')

def done(request, todo_id):
    # Mark a todo as complete
    item = Todo.objects.get(id=todo_id)
    item.is_complete = True
    item.save()
    return redirect('index')

# Auth-related routes
def signup(request):
    if request.method == 'GET':
        return render(request, 'finderapp/signup.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        try:
            user = User.objects.create_user(username=username, 
                password=password)
            if user is not None:
                # auth.login(request, user)
                return login(request)
        except:
            return render(request, 'finderapp/signup.html', { 'error': 'Arggghhh!'})

def login(request):
    if request.method == 'GET':
        return render(request, 'finderapp/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'finderapp/login.html', { 'error': 'Invalid credentials!'})

def logout(request):
    auth.logout(request)
    return redirect('index')




def lawyer_list(request):
    lawyers = Lawyer.objects.all()
    return render(request, 'lawyer_list.html', {'lawyers': lawyers})

def lawyer_detail(request, pk):
    lawyer = Lawyer.objects.get(id=pk)
    return render(request, 'lawyer_detail.html', {'lawyer': lawyer})

def lawyer_create(request):
    if request.method == 'POST':
        form = LawyerForm(request.POST)
        if form.is_valid():
            lawyer = form.save()
            return redirect('lawyer_detail', pk=lawyer.pk)
    else:
        form = LawyerForm()
        return render(request, 'lawyer_form.html', {'form': form})

def lawyer_edit(request, pk):
    lawyer = Lawyer.objects.get(id=pk)
    if request.method == 'POST':
        form = LawyerForm(request.POST, instance=lawyer)
        if form.is_valid():
            lawyer = form.save()
            return redirect('lawyer_detail', pk=lawyer.pk)
    else:
        form = LawyerForm(instance=lawyer)
        return render(request, 'lawyer_form.html', {'form': form})

def lawyer_delete(request, pk):
    Lawyer.objects.get(id=pk).delete()
    return redirect('lawyer_list')










