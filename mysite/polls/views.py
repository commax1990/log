from django.shortcuts import render


def login(request):
    return render(request, 'login.html')
    # if request.method == 'POST':
    #     form = UserLoginForm(data=request.POST)
    #     if form.is_valid():
    #         user = form.get_user()
    #         login(request,user)
    #         return redirect('index')
    # else:
    #     form = UserLoginForm()
    # return render(request,'pages/autorizaciya.html',{'form': form})
