from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.views import View
from django.urls import reverse_lazy

from .forms import UserLoginForm

# Create your views here.


class HomeView(LoginRequiredMixin, View):
    template_name = 'index.html'

    login_url = 'login'
    # redirect_field_name = '/'
    
    def get(self, request, *args, **kwargs):
        context={}
        return render(request, self.template_name, context)

class LoginFormView(View):
    template_name="registration/login.html"

    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        context={"form":form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                print(username, password) 

                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('core:home')
                else:
                    form = UserLoginForm()
            else:
                form = UserLoginForm()
        else:
            form = UserLoginForm()

        context={'form': form}
        return render(request, self.template_name, context)
   