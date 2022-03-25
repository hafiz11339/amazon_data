from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import amazon_data
from django.core.paginator import Paginator
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def main(request):
    obj = amazon_data.objects.all()
    if obj:
        pagination = Paginator(obj, 10)
        page = request.GET.get("page")
        objects = pagination.get_page(page)
        print(objects)
        context = {"obj":objects}
        # if request.user.is_authenticated:
        #     return HttpResponse('<h1>hello</h1>')
        # else:
        return render(request, "amazon/main.html", context=context)
def loginPage(request):
    if request.method == "POST":
        username = request.POST['user']
        passwd = request.POST['pass']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"User does not exist")
        user = authenticate(request,username=username,password=passwd)
        if user is not None:
            login(request,user)
            return redirect("main")
        else:
            messages.error(request,"User does not exist")
    return render(request,'amazon/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')