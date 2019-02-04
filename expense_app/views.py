from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print("---------user authenticated next redirect")
            return redirect('user_profile')
    else:
        form = UserCreationForm()
    return render(request, 'expense_app_templates/signup.html', {'form': form})

def user_profile(request):
    try:
        print(request.user,"-------user")
        user1 = request.user.username
        print (user1,"--------------user.name")

        if user1 == request.user.username :
            print("-----inside if")
            messages.add_message(request, messages.INFO, 'Welcome, '+request.user.username)
            return render(request, 'expense_app_templates/user_profile.html')
            
    except Exception as e:
        print(e,"--------Exception error")
        messages.add_message(request, messages.INFO, 'User record not found')
        return redirect('signup')
            
    return render(request, 'expense_app_templates/user_profile.html')