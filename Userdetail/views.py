from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import *
from django.views.generic import *
from django.urls import *
from Userdetail.models import *
from Userdetail.forms import *
# Create your views here.

class createUser(TemplateView):
    form_class=Usercreateform
    model_name=Users
    template_name = "Userdetail/Usercreate.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            Name = form.cleaned_data["Name"]
            Accno = form.cleaned_data["Accno"]
            Telephone = form.cleaned_data["Telephone"]
            Email = form.cleaned_data["Email"]
            Username = form.cleaned_data["Username"]
            Password = form.cleaned_data["Password"]
            # isActive=True
            qs = Users.objects.create(Name=Name, Telephone=Telephone,Accno= Accno,\
                    Email=Email,Username=Username,Password=Password,isActive=True,isLog=False)
            print("d1")
            # form.save(commit=False)
            print("d2")
            qs.save()
            print("d3")
            return JsonResponse({"message": "loginSuccess", 'status': 200})

        else:
            return render(request, self.template_name,{"form":form})

class loginUser(TemplateView):
    form_class=Userlogin
    model_name=Users
    template_name = "Userdetail/Userlogin.html"
    template_name1 = "Kiosk/home.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        print("Hi0000")
        if form.is_valid():
            print("Hi1111")
            Accno=form.cleaned_data["Accno"]
            Username = form.cleaned_data["Username"]
            Password = form.cleaned_data["Password"]
            qs=Users.objects.get(Username=Username)
            print("Hi")
            print("Active:",qs.isActive)
            if((qs.Username==Username)&(qs.Password==Password)):
                request.session['Username']=Username
                request.session['Accno'] = Accno
                context = {}
                context["qs"] = qs
                # context["user"] = user
                print("hiiiiiiiiiiiiii")
                return render(request, self.template_name1, context)
                # return HttpResponseNotFound('<h1>Page not found</h1>')
            else:
                print("Hi2222")
                return redirect("User_login")
                # return HttpResponse('<h1>Page was not found</h1>')

        else:
            print("Hi33333")
            return render(request, self.template_name,{"form":form})


def logoutUser(request):
        del request.session['Username']
        del request.session['Accno']
        return redirect("User_login")