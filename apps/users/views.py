
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'Account created for {username} living at {first_name}!')
            return redirect('frontpage')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
        
    }
    return render(request, 'users/profile.html',context)


@login_required
def add(self,request,amount=1):
    self.user.balance+=int(amount)

    self.save()

