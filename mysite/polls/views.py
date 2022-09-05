from django.shortcuts import redirect
from django.shortcuts import render

from .forms import UserLoginForm


def UserLogin(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'pages/login.html', {'form': form})


def login(request):
    return render(request, 'pages/login.html')
    print('test 1')
    print('test 2')
    # if request.method == 'POST':
    #     form = UserLoginForm(data=request.POST)
    #     if form.is_valid():
    #         user = form.get_user()
    #         login(request,user)
    #         return redirect('index')
    # else:
    #     form = UserLoginForm()
    # return render(request,'pages/autorizaciya.html',{'form': form})
