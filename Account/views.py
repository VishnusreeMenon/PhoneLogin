import random
from .forms import ProfileForm
from django.shortcuts import redirect, render
from .models import *
from .mixins import MessageHandler
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        user = User.objects.create(username = username)
        profile = NewUser.objects.create(user=user,phone_number = phone_number)
        
        return redirect('/login')
    return render(request,'Account/register.html')

def home(request):
    return render(request,'Account/home.html')
    
def login_page(request):
    if request.method== 'POST':
        phone_number = request.POST.get('phone_number')
        newuser = NewUser.objects.filter(phone_number = phone_number)
        if not newuser.exists():
            return redirect('/register')
        
        newuser = newuser[0]
        newuser.otp = random.randint(1000,9999)
        newuser.save()
        try:
            res = MessageHandler(phone_number,newuser.otp).send_otp_to_phone()
        except Exception as e:
            print("error-",e)
        return redirect(f'/otp/{newuser.uid}')
    
    return render(request,'Account/login.html')
    
    
def otp(request,uid):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        user = NewUser.objects.get(uid = uid)
        print(otp,user.otp)
        if otp == user.otp:
            print("here")
            login(request,user.user)
            return redirect('/dashboard/')
        return redirect(f'/otp/{uid}')
    return render(request,'Account/otp.html')

@login_required
def dashboard(request):
    print("hello;",request.POST)
    return render(request,'Account/dashboard.html')


class ProfileFill(CreateView):
    model = Profile
    form_class = ProfileForm
    # fields = ['person','role','profile_score','mental_score']
    template_name = 'Account/dashboard.html'
    success_url = '/dashboard'
    
    def form_valid(self,form):
        print("test",self.request.user)
        form.instance.person = NewUser.objects.filter(user = self.request.user)[0]
        form.save()
        return super(ProfileFill,self).form_valid(form)
   