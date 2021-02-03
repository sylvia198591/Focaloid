from django.db.models import *
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import *
from django.views.generic import *
from django.urls import *
from Kiosk.models import *
from Kiosk.forms import *

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
from Kiosk.models import *


class createAccount(TemplateView):
    form_class = Accountcreateform
    model_name = Account
    template_name = "Kiosk/createAccount.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context["form"] = self.form_class
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            Name = form.cleaned_data["Name"]
            Accno = form.cleaned_data["Accno"]

            # Amt_c = form.cleaned_data["Amt_c"]
            # Amt_d = form.cleaned_data["Amt_d"]
            Amount = form.cleaned_data["Amount"]
            Dfield = form.cleaned_data["Dfield"]
            Type = form.cleaned_data["Type"]
            # qs = Account.objects.filter(Accno=Accno).order_by('Dfield')[0].values_list('Amt')
            #
            # context = {}
            # context["accdtl"] = qs
            # x_data = [i.get("Amt") for i in qs]
            # if(x_data==)
            # isActive=True
            if (request.session['Accno'] == Accno):
                print("tYPE",str(Type))
                if(str(Type)=="Debit"):
                    Amount=Amount*(-1)
                    print("Amt",Amount)
                print("Amto", Amount)
                qs = Account.objects.create(Name=Name, Accno=Accno,Dfield=Dfield,\
                                             Amount=Amount, Type=Type)
                print("d1")
                # form.save(commit=False)
                print("d2")
                qs.save()
                print("d3")
                return redirect("Account_view")
            else:
                return render(request, self.template_name, {"form": form})
        else:
            return render(request, self.template_name, {"form": form})


class viewAccount(TemplateView):
    model_name = Account
    form_class = ViewAccountform
    # template_name = "Kiosk/viewAccounto.html"
    # def get_queryset(self):
    #     return self.model_name.objects.all()
    template_name = "Kiosk/viewAccount.html"
    template_name1 = "Kiosk/viewAccounto.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context["form"] = self.form_class
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print("0000")
        if form.is_valid():
            print("11111")
            # Name = request.session["Name"]
            Accno = form.cleaned_data["Accno"]
            # Startdate = form.cleaned_data["Startdate"]
            # Enddate = form.cleaned_data["Enddate"]
            # print("sess:", request.session["Username"])
            # print("pay:",Paymode)
            # Username1 = request.session.Username
            # Username=form.cleaned_data["Username"]
            if(request.session['Accno']==Accno):
                qs = Account.objects.filter(Accno=Accno)
                qs1 = Account.objects.filter(Accno=Accno).aggregate(Total=Sum('Amount'))

                    # .order_by('Accno') \

                    # .order_by('Accno').aggregate(Sum('Amount'))

                # .aggregate(Total=Sum('Amount'))
                # print(qs.Total)
                # qs =Entry.objects.filter(Q(Username=Username)& \
                #                          Q(Dfield__gte=Startdate)&\
                #                          Q(Dfield__lte=Enddate)&\
                #                          Q(Category__Category=Category)).\
                #     aggregate(Sum('Amount')).get('Amount__sum')
                print("d1")
                context = {}
                context["viewaccount"] = qs
                context["viewaccount1"] = qs1
                return render(request, self.template_name1, context)

                # form.save()
                print("d2")
                # qs.save()
                print("d3")
                # return redirect("Categorywise_view")
            else:
                return render(request, self.template_name, {"form": form})
        else:
            return render(request, self.template_name, {"form": form})


class updateAccount(UpdateView):
    model = Account
    fields = ['Name', 'Type', 'Amount', 'Dfield' ]
    success_url = '/Viewaccount'
    # success_url = reverse_lazy('getRes')
    # context_object_name = "form"
    template_name = 'Kiosk/createAccount.html'


class deleteAccount(DeleteView):
    model = Account

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    fields = ['Name', 'Trans_type',  'Amount', 'Dfield']
    # template_name_suffix = "_del"
    success_url = '/Viewaccount'

class createDatewise(TemplateView):
    form_class=Adddatewiseform
    model_name=Account
    template_name = "Kiosk/createDatewise.html"
    template_name1 = "Kiosk/viewDatewise.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        print("0000")
        if form.is_valid():
            print("11111")
            # Username = request.session["Username"]
            Accno = form.cleaned_data["Accno"]
            Startdate = form.cleaned_data["Startdate"]
            Enddate = form.cleaned_data["Enddate"]
            # print("sess:",request.session["Username"])
            # print("pay:",Paymode)
            # Username1 = request.session.Username
            # Username=form.cleaned_data["Username"]
            qs = Account.objects.filter(Accno=Accno, \
                                        Dfield__range=[Startdate, Enddate])
            qs1 =Account.objects.filter(Accno=Accno, \
                    Dfield__range=[Startdate,Enddate]).aggregate(Total=Sum('Amount'))\
                                        # Dfield__lte=Enddate, \
                    # Category__Category=Category)\

            # print(qs.Total)
            # qs =Entry.objects.filter(Q(Username=Username)& \
            #                          Q(Dfield__gte=Startdate)&\
            #                          Q(Dfield__lte=Enddate)&\
            #                          Q(Category__Category=Category)).\
            #     aggregate(Sum('Amount')).get('Amount__sum')
            print("d1")
            context = {}
            context["vdw"] = qs
            context["vdw1"] = qs1
            # context[""]=Username
            # context["sd"]=Startdate
            # context["ed"]=Enddate
            # context["Accno"]=Accno
            return render(request, self.template_name1, context)

            # form.save()
            print("d2")
            # qs.save()
            print("d3")
            # return redirect("Categorywise_view")
        else:
            return render(request, self.template_name,{"form":form})

class createTrans(TemplateView):
    form_class = Addtranstypeform
    model_name = Trans_type
    template_name = "Kiosk/createTrans.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context["form"] = self.form_class
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            Trans_symbol = form.cleaned_data["Trans_symbol"]
            Type = form.cleaned_data["Type"]


            qs = Trans_type.objects.create(Trans_symbol=Trans_symbol, Type=Type)
            print("d1")
            # form.save(commit=False)
            print("d2")
            qs.save()
            print("d3")
            return redirect("Account_view")

        else:
            return render(request, self.template_name, {"form": form})

class createTransfer(TemplateView):
    form_class = Addtransferform
    model_name = Account
    template_name = "Kiosk/createAccount.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context["form"] = self.form_class
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Name=form.cleaned_data["Accno"]
            Accno = form.cleaned_data["Accno"]
            Accnoto = form.cleaned_data["Accnoto"]
            # Dfieldt = form.cleaned_data["Dfieldt"]
            Amount= form.cleaned_data["Amount"]
            print("a",Accno)
            print("at",Accnoto)
            qs=Account.objects.filter(Accno=Accnoto).annotate(Count('Accno', distinct=True))
            if((qs[0].Accno__count)==1):
                n1=Account.objects.filter(Accno=Accno)

                qs1 = Account.objects.create(Name=n1[0].Name, Accno=Accno,\
                                             Amount=(Amount*-1), Type=(Trans_type.objects.get(id=2)))
                qs1.save()
                qs2 = Account.objects.create(Name=qs[0].Name, Accno=Accnoto,\
                                             Amount=(Amount), Type=(Trans_type.objects.get(id=1)))
                print("d1")
                # form.save(commit=False)
                print("d2")

                qs2.save()
                print("d3")
                return redirect("Account_view")
            else:
                return render(request, self.template_name, {"form": form})


        else:
            return render(request, self.template_name, {"form": form})

