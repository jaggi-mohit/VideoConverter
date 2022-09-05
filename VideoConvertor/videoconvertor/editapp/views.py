from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse, request 
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import UserProfile as UserP
from django.core.mail import mail_admins, send_mail
from django.conf import settings
# Create your views here.
class dash(View):
    def post(self,request,**kwargs):
        print("welcome")
        username=request.POST['username']
        passw=request.POST['password']
        user = auth.authenticate(username=username,password=passw)

        if username =="" or passw == "":
            messages.error(request,f'Blank Fields not allowed !')
            return redirect('login')

        try:
            if user.is_authenticated:
                #print('dhfhvj')
                auth.login(request,user)
                return redirect('home')
        except:
            messages.error(request,f'Invalid Credentials Kindly Try Again !')
            return redirect('login')
        
    
    def get(self,request,**kwargs):
        user=request.user
        print(user)
        if user.is_authenticated:
            userp=UserP.objects.get(user__username=user)

            return render(request,'indexuser.html',{'userp':userp})
        
        else:
            return redirect('login')

class login(TemplateView):
    
    def get(self,request,**kwargs):
        user=request.user
        if user.is_authenticated:
            
            return redirect('home')
        
        else:
            return render(request,self.template_name)
        
        
    def post(self,request,**kwargs):
        if self.template_name =="register.html":
            return HttpResponse('WElvome')

class Edit(TemplateView):
    #template_name="Edit.html"
    '''
    def get(self,request,**kwargs):
        print("running")
        print(self.template_name)
        return render(request,self.template_name)
    '''
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['message'] = 'Hello World!'
        return context


def mails(request):
    #mail_admins('testing well','Hey dude whats up',fail_silently=False)
    #settings.EMAIL_HOST_USER='mohit1702011@gmail.com'
    if request.method == 'POST':
        fname=request.POST.get('Fname')
        Email=request.POST.get('Email')
        Phone=request.POST.get('Pnumber')
        message =request.POST.get('msg')


    send_mail('Query From '+str(Email),str(message)+' \n'+fname+'\n'+Phone,settings.EMAIL_HOST_USER,['mohit1702011@gmail.com'])
    send_mail('Query Submitted','Your Query has been submitted Successsfully',settings.EMAIL_HOST_USER,[str(Email)])
    return redirect('/')