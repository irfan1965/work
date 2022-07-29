from logging import exception
from django.db.models import Q
from django.http import HttpResponseRedirect
from .filters import *
from telnetlib import AUTHENTICATION
from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
# from httplib2 import Authentication
from .models  import *
import random 
from django.contrib.auth.models import User
from django.contrib.auth  import logout,authenticate,login as auth_login
C_N="Customer_"
k=10001
pay_id=1824
dtl_id=37423
def start(Request,type):
        print(Request.POST,"dkfjg")
  
        #d=Request.POST
       # print(list(d.keys())[0],"efldkh")
      #  d=(next(reversed(d.keys())))
        # print(d)
        #d=list(d.keys())[0]
        d=type
        print(d)
        if (d=='admin'):
            return render(Request,"home.html",{"k":1})
        elif d=="farmer":
            return render(Request,"home.html",{"k":2})
        elif d=="doctor":
            return render(Request,"home.html",{"k":3})
        elif d=="Animal":
            return render(Request,"home.html",{"k":4})
        else :
            return render(Request,"home.html",{"k":5})
   



def disp(Request):
    return render(Request,"display.html")

def db_Admin(Request):
    k=Admin1()
    print(Request.POST)

    print("dsfkjgd,fdhgfdh")
    # k.Id=Request.POST.get("Name")
    # k.Psw=Request.POST.get("Psw")
    # k.save()
    # if Request.POST["Name"]=='irfan' and Request.POST['Psw']==1234:
    return render(Request,"Admin.html")

def admin_details(Request):
    d=Request.POST
    print(d,"juh")
   # m=Request.POST["p"]
    #print(m,"dsfkjg")
    #print(Request.POST["p"]!="")
  #  print(list(d.keys())[0],"efldkh")
    d=(next(reversed(d.keys())))
   
    print(d)
    if d=="f_de":
     try:
        h=1
        print("DFcdx",Request.POST["p"],len(Request.POST["p"])>1)
        k=Request.POST["p"]
        if (len(Request.POST["p"])>1):
            # print(l,"this is l")
            print("hjdfs")
            k= Farmer1.objects.filter(
            Q(Farmer_Name=Request.POST["p"])|Q(Farmer_Email=Request.POST["p"])|Q(Farmer_loc=Request.POST["p"]))
            print(k,"this is l")
            if len(k)==1:
                print(k[0],"rdgyoih")
                return render(Request,"Admin_Disp.html",{"h":1,"k":k[0],"u":121})
            else:
                return render(Request,"Admin_Disp.html",{'h':h,"k":k})
        return render(Request,"Admin_Disp.html",{"h":h,"k":k})
     except:
            print("dfh")
            k=Farmer1.objects.all()
            h=1
            return  render(Request,"Admin_Disp.html",{"h":h,"k":k})
    elif d=="a_d":
            try:
                h=2
                print("DFcdx",Doctor1.objects.filter(Doctor_Exp=Request.POST["p"]))
                if (len(Request.POST["p"])>1):
                    # print(l,"this is l")
                    print("hjdfs")
                    k=Doctor1.objects.filter(
                Q(Doctor_Name=Request.POST["p"])|Q(Doctor_Exp=Request.POST["p"])|Q(Doctor_Loc=Request.POST["p"]))
                    print(k,"this is k")
                    if len(k)==1:
                        print(k[0],"rdgyoih")
                        return render(Request,"Admin_Disp.html",{"h":2,"k":k[0],"u":122})
                    else:
                        return render(Request,"Admin_Disp.html",{'h':2,"k":k})
                return render(Request,"Admin_Disp.html",{"h":2,"k":k})
            except Exception as err:
                print(err,"dfjk")
                k=Doctor1.objects.all()
                h=2
                return  render(Request,"Admin_Disp.html",{"h":h,"k":k})
    else:
        k = Details1.objects.all()
        DF = DetailsFilter(Request.POST, queryset=k)
        k = DF.qs
        print(k,"this is k")
        h=3
        return  render(Request,"Admin_Disp.html",{"h":h,"k":k,"DF":DF})

def db_Farmer(Request):
    if Request.method == 'POST':
       print(Request.POST,"desfjkgh")
       v=Farmer1()
       D=Doctor1()
       #Request.POST.get("Farmer_Name") in Farmer1.objects.all().filter("Farmer_Name")
       print(Farmer1.objects.all().filter(Farmer_Name=Request.POST.get("Farmer_Name")))
       if True:
      
        v.Farmer_Name=Request.POST.get("Farmer_Name")

        v.Farmer_Email=Request.POST.get("Farmer_Email")
        v.Farmer_Psw=Request.POST.get("Farmer_Psw")
        v.Farmer_loc=Request.POST.get("Farmer_Loc")
      #  print(Admin1.objects.get(Id="irfan"),"sdf;oh")
        v.Id=Admin1.objects.get(Admin=1)
        v.save()
        A=Animal1()
        # print(Farmer1.objects.get(Id=Request.POST.get("Farmer_Name")),"sdjhgkkjhg")
        #print(Farmer1.objects.get(Farmer_Name=Request.POST.get("Farmer_Name")),"edsjhb")
        A.Farmer_ID = Farmer1.objects.get(Farmer_Name=Request.POST.get("Farmer_Name"))
        
        # print(Doctor1.objects.get(Id="irfan"), "doctor")
        A.Doctor_ID=Doctor1.objects.get(Doctor_Name="irfan")
        print(Farmer1.objects.all().filter(Farmer_Name__icontains=Request.POST.get("Farmer_Name")),"efkljb")
        A.Animal_Amount=100
        A.save()
        
        return render(Request,'Farmer_Login.html',{'farmer':Request.POST.get("Farmer_Name")})

       # return render(Request,'info.html',{'farmer':Request.POST.get("Farmer_Name")})
    return render(Request,'home.html')

def Ani_reg(Request):
    print(Request.POST,"drfloih")
    return render(Request,"info.html")
def d_l(Request):
    print(Request.POST,"dsfkjhlkj")
    if "Name1" not in Request.POST and Request.POST["Name"] !="" :
        Request.session['doc']=Request.POST["Name"]
    elif  Request.POST["Name1"]!="":
         Request.session['doc']=Request.POST["Name1"]
    else:
        pass
    if "Name1" not in Request.POST or  "status" in Request.POST  :
            s=Doctor1.objects.filter(Doctor_Name= Request.session['doc'])
            print(s[0].Doctor_ID,"dfskjg")
            d=Animal1.objects.filter(Doctor_ID_id=s[0].Doctor_ID)
            p=Details1.objects.filter(Details_Prescription="",Details_Doctor=s[0].Doctor_ID).values_list("Details_Farmer_id","Details_Animal_id")
            h=Details1.objects.filter(Details_Prescription="",Details_Doctor=s[0].Doctor_ID)
            print(h,"this is h")
            b=[]
            m=Details1.objects.filter(Details_Prescription="",Details_Doctor=s[0].Doctor_ID).values_list("Details_Animal_id" )
            n=Details1.objects.filter(Details_Prescription="",Details_Doctor=s[0].Doctor_ID).values_list("Details_Farmer_id")
            for i in p:
            # print(i[0],i[1])
                b.append(Animal1.objects.filter(Animal_Id=i[1],Farmer_ID_id=i[0]))
            k=Animal1.objects.filter(Animal_Id__in=m,Farmer_ID_id__in=n)
            print(k,"drygbf")       # print(b,"this is b")

            l=[]
            for i in d:
                l.append(i)
        # print(l,"this is l")
        # print(p[0][1],"fgfg")
            d=k
            print(d,"dsf")
            # d=d.exclude()
            
            #print(p[0].Details_Farmer_id,"qwqweweewweqqwe")
            #print((p.Details_Farmer_id,p.Details_Animal_id,"efjkg"))
            # for i in p:
            #     print(i.Details_Farmer_id,i.Details_Animal_id,"efjkg")
            
            # for i in d:
            #     print(i)
            #     print("sjh")

            print(*d)
            #print(Request.POST,"kiejfgjh")

            return render(Request,"displayd.html",{"d":d,"F": Request.session['doc'],"s":1})
    else:
           
            print(Request.session['doc'],"gtlkdh")
            s=Doctor1.objects.filter(Doctor_Name= Request.session['doc'])
            print(s,"rkgdfuyg")
            print(s[0].Doctor_ID,"dfskjg")
            d=Animal1.objects.filter(Doctor_ID_id=s[0].Doctor_ID)
        #  print(d)
            p=Details1.objects.exclude(Details_Prescription="",Details_Doctor=s[0].Doctor_ID).values_list("Details_Farmer_id","Details_Animal_id")
            h=Details1.objects.exclude(Details_Prescription="",Details_Doctor=s[0].Doctor_ID)
            print(h,"this is h")
            b=[]
            m=Details1.objects.exclude(Details_Prescription="",Details_Doctor=s[0].Doctor_ID).values_list("Details_Animal_id" )
            n=Details1.objects.exclude(Details_Prescription="",Details_Doctor=s[0].Doctor_ID).values_list("Details_Farmer_id")
            for i in p:
                b.append(Animal1.objects.filter(Animal_Id=i[1],Farmer_ID_id=i[0]))
            k=Animal1.objects.filter(Animal_Id__in=m,Farmer_ID_id__in=n)
            print(k,"drygbf")     
            # print(b,"this is b")

            l=[]
            for i in d:
                l.append(i)
        # print(l,"this is l")
        # print(p[0][1],"fgfg")
            d=k
            print(d,"dfgsf")
            # d=d.exclude()
            
            #print(p[0].Details_Farmer_id,"qwqweweewweqqwe")
            #print((p.Details_Farmer_id,p.Details_Animal_id,"efjkg"))
            # for i in p:
            #     print(i.Details_Farmer_id,i.Details_Animal_id,"efjkg")
            
            # for i in d:
            #     print(i)
            #     print("sjh")

            print(*d)
            #print(Request.POST,"kiejfgjh")

            return render(Request,"displayd.html",{"d":d})


def Farmer_Login(Request,type):
    print(type,"dfjd")
    return render(Request,"Farmer_Login.html",{"F":"farmer"})
def pre_c(Request):
   
        print(Request.POST,"fdklbjb")
        de=Details1()
        # o=list("spXjgs51458623Xxxdd")
        # random.shuffle(o)
        # print(''.join(o),"payment_id")
        # de.Payment_Id=''.join(o)
        k=Animal1.objects.filter(Farmer_ID=Request.POST["Farmer_ID_id"],Animal_Name=Request.POST["Animal_Name"])
        print(k[0].Animal_Id,"this is vg k1",Request.POST["Farmer_ID_id"],k[0].Animal_Id)
        r=Details1.objects.filter(Details_Farmer=Request.POST["Farmer_ID_id"],Details_Animal_id=k[0].Animal_Id)
        print(r[0].Payment_Id,"dsfilh")
    
       # print(r.Payment_Id," : ",Details1.objects.all().filter(Details_Farmer=Request.POST["Farmer_ID_id"],Details_Animal_id=k[0].Animal_Id),"this is r")
        #print(k,"this is k")
        de=Details1.objects.filter(Payment_Id=r[0].Payment_Id)
        print(de,"this is de")
        # de.Details_fid=1
        # d=Animal1.objects.filter(Doctor_ID_id=Request.POST["Name"])
        de.update(Details_Prescription=Request.POST["presc"])
        de.update(Details_Status=Request.POST["Status"])
        de.update(Details_Farmer=Farmer1.objects.get(Farmer_id=Request.POST["Farmer_ID_id"]))
        de.update(Details_Doctor=Doctor1.objects.get(Doctor_ID=Request.POST["Doctor_ID_id"]))
        de.update(Details_Animal=Animal1.objects.get(Animal_Name=Request.POST["Animal_Name"]))
        de.update(Details_Amount=Request.POST.get("Animal_Amount"))
        print(Request.POST.get("Farmer_ID_id"),"fvgklfjb1")
        # de.Details_Prescription=Request.POST.get("presc")
        # de.Details_Amount=Request.POST.get("Details_Amount")
        #return HttpResponseRedirect(Request.META.get('HTTP_REFERER'))
        return HttpResponse("sending reqeust..")
def displayf(Request):
    print(Request.POST,"DSFKGH")
    return render(Request,"displayf.html",{"F":Request.POST["Farmer_Name"]})
def displayd(Request):
    print(Request.POST["Name"],"DSFKGwerH")
    return render(Request,"displayd.html",{"F":Request.POST["Name"]})
def doctorhome(Request):
    return render(Request,"doctorhome.html",{"F":Request.session["doc"]})
def doctor_redirect(Request):
    Request=k
    try:
        print(Request.POST,"fdklbjbtyu")
        de=Details1()
        # o=list("spXjgs51458623Xxxdd")
        # random.shuffle(o)
        # print(''.join(o),"payment_id")
        # de.Payment_Id=''.join(o)
        k=Animal1.objects.filter(Farmer_ID=Request.POST["Farmer_ID_id"],Animal_Name=Request.POST["Animal_Name"])
        print(k[0].Animal_Id,"this is k6")
        r=Details1.objects.get(Details_Farmer=Request.POST["Farmer_ID_id"],Details_Animal=k[0].Animal_Id)
        print(r)
        print(k,"this is k4")
        de=Details1.objects.filter(Payment_Id=r)
        print(de,"this is de65")
        # de.Details_fid=1
        # d=Animal1.objects.filter(Doctor_ID_id=Request.POST["Name"])
        de.update(Details_Prescription=Request.POST["presc"])
        de.update(Details_Status=Request.POST["Status"])
        de.update(Details_Farmer=Farmer1.objects.get(Farmer_id=Request.POST["Farmer_ID_id"]))
        de.update(Details_Doctor=Doctor1.objects.get(Doctor_ID=Request.POST["Doctor_ID_id"]))
        de.update(Details_Animal=Animal1.objects.get(Animal_Name=Request.POST["Animal_Name"]))
        de.update(Details_Amount=Request.POST.get("Animal_Amount"))
        print(Request.POST.get("Farmer_ID_id"),"fvgkljb")
        # de.Details_Prescription=Request.POST.get("presc")
        # de.Details_Amount=Request.POST.get("Details_Amount")
        return HttpResponse("sendingRequest...")
    except:
        return HttpResponse("error occured")
    
def f_l(Request):
    print(Request.POST)
    qwe=Request
    print(qwe,"ksdjfg")
    f_l.val=Request
    F=Farmer1.objects.all().filter(Farmer_Name=Request.POST["Farmer_Name"])
    Request.session['req']=Request.POST["Farmer_Name"]
    
    print(F)
    print( Request.POST,"kigh12")
    if "search" not  in Request.POST:
        try:
                print(Request.POST,"kuygf")
                de=list(Details1.objects.values_list("Details_Farmer",flat=True))
                #print(de,"this is de")
               # print(F[0].Farmer_id,"fgjkdh")
                Fd=list(Farmer1.objects.values_list("Farmer_Name",flat=True))
               # print(str(Request.POST["Farmer_Name"])  in de,"dfkdsgfjgh")
                if str(Request.POST["Farmer_Name"])  not  in Fd:
                    return render(Request,"except.html",{"k": 2})
                else: 
                    if str(Request.POST["Farmer_Name"])   in  Fd   and F[0].Farmer_id in de:
                        j=(Farmer1.objects.filter(Farmer_Name=Request.POST["Farmer_Name"]))
                        a=Details1.objects.all().filter(Details_Farmer=j[0])
                       # print(a,"this is a")
                        a=Details1.objects.all().filter(Details_Farmer=j[0])
                        if len(a)==1:
                            return render(Request,"F_D.html",{"a":a[0],"F":Request.POST["Farmer_Name"],"k":1,"r":qwe,"id1":F[0].Farmer_id})
                        else:
                            return render(Request,"F_D.html",{"a":a,"F":Request.POST["Farmer_Name"],"k":2,"r":qwe,"id1":F[0].Farmer_id})


                    else:
                        return render(Request,"F_D.html",{"F":Request.POST["Farmer_Name"],})

               
        except:
                return render(Request,"except.html",{"k": 2})

    else:
        try:
            print(qwe,"this is F")
            print(Request.POST,"this is Request ")
            #print(Details1.objects.all().filter(Q(Details_Status=Request.POST["search"])| Q(Details_Prescription=Request.POST["search"]),Details_Farmer=Request.POST['Farmer_Name']))
          #  a=Details1.objects.all().filter(Details_Farmer=Request.POST['Farmer_Name'])
          #  print(a,"this is a")
            # a=Details1.objects.all().filter(Details_Farmer=j[0])
            g=Details1.objects.all().filter(
                Q(Details_Status=Request.POST["search"])| Q(Details_Prescription=Request.POST["search"])|Q(Payment_Id=Request.POST["search"]),
                Details_Farmer=Request.POST['Farmer_Name'])
              
            print(g)
            if len(g)==1:
                    return render(Request,"F_D.html",{"a":g[0],"F":Request.POST["Farmer_Name1"],"k":1,"r":qwe,"id1":Request.POST["Farmer_Name"]})
            else:
                return  render(Request,"F_D.html",{"a":g,"F":Request.POST["Farmer_Name1"],"k":2,"r":g,"id1":Request.POST["Farmer_Name"]})
              
        except Exception as Err:
                print(Err,"this is Err")
                a=Details1.objects.all().filter(Details_Farmer=Request.POST["Farmer_Name"])
                #print(a,"this is a")
                # a=Details1.objects.all().filter(Details_Farmer=j[0])
                if len(a)==1:
                    return render(Request,"F_D.html",{"a":a[0],"F":Request.POST["Farmer_Name1"],"k":1,"r":qwe,"id1":Request.POST["Farmer_Name"]})
                else:
                    return render(Request,"F_D.html",{"a":a,"F":Request.POST["Farmer_Name1"],"k":2,"r":qwe,"id1":Request.POST["Farmer_Name"]})

def f_l1(Request,k):
    qwe=Request
    f_l.val=Request
    print(k ,Request,"kigh")
    try:
            print(Request.POST,"kuygf1")
            de=list(Details1.objects.values_list("Details_Farmer",flat=True))
            print(de,"this is de")
            F=Farmer1.objects.all().filter(Farmer_Name=k)
            print(F[0].Farmer_id,"fgjkdh")
            Fd=list(Farmer1.objects.values_list("Farmer_Name",flat=True))
            print(F[0].Farmer_id  in de,"dfkdsgfjgh")
            print(str(k)   in Fd   and F[0].Farmer_id in de,k  not  in Fd)
            if str(k)  not  in Fd:
                return render(Request,"except.html",{"k": 2})
            else: 
                if str(k)   in Fd   and F[0].Farmer_id in de:
                    j=(Farmer1.objects.filter(Farmer_Name=k))
                    a=Details1.objects.all().filter(Details_Farmer=j[0])
                    print(a,"this is a")
                    a=Details1.objects.all().filter(Details_Farmer=j[0])
                    if len(a)==1:
                        return render(Request,"F_D.html",{"a":a[0],"F":k,"k":1,"r":qwe})
                    else:
                        return render(Request,"F_D.html",{"a":a,"F":k,"k":2,"r":qwe})


                else:
                    return render(Request,"F_D.html",{"F":k})

            # try:
            #     j=(Farmer1.objects.filter(Farmer_Name=Request.POST["Farmer_Name"]))
            #     b=list(Farmer1.objects.filter())
            #     print(j.Farmer_id,"ert")
            #     for i in list(Farmer1.objects.filter()):
            #         print(i.Farmer_Name,j[0])
            #         if  str(i.Farmer_Name) == str(j[0]) :
            #             return render(Request,"except.html",{"k":1})
            # except:
            #     try:
                 
            #     except:
            #         return render(Request,"except.html",{"k":2})
    except:
            return render(Request,"except.html",{"k": 2})


def db_Doctor(Request):
    D=Doctor1()
    A=Animal1()
    #D.Doctor_ID=Request.POST.get("Doctor_Name")
    D.Doctor_Name=Request.POST.get("Doctor_Name")
    D.Doctor_Desgination=Request.POST.get("Doctor_Desgination")
    D.Doctor_Exp=Request.POST.get("Doctor_Exp")
   # D.Doctor_Image=Request.POST.get("Doctor_Image")
    D.Doctor_Name=Request.POST.get("Doctor_Name")
    D.Doctor_Slot=Request.POST.get("Doctor_Slot")
    D.Doctor_Image=Request.POST.get("Doctor_Image")
    D.Doctor_Psw=Request.POST.get("Doctor_Psw")
   # print(Admin1.objects.get(Admin="irfan"),"erqwoidgu")
    D.Admin_Id=Admin1.objects.get(Admin=1)
   
   # print(D.Id,"ewodfu yg sdckjasdghfakkjgdesf oewqgfyk jdsag o")
    D.save()
    return HttpResponse("<h2>register sucessful  db_Doctor </h2>")
def Doct_r(Request,type):
    print(type,"type")
    return render(Request,"Doctor.html",{"doc":"doctor"})

def db_Animal(Request):
    print(Request.POST,"DSFJH")
    f=Request.POST["farmer"]
    dc=Farmer1.objects.filter(Farmer_Name=Request.POST["farmer"])
    print(dc[0].Farmer_id,"fgv")
    a=Request.POST['Animal_Name']
    iv=Animal1.objects.filter(Farmer_ID=dc[0].Farmer_id)
   # print(f,(iv),"dsfjkgv")
    l=[]
    Far=list(Animal1.objects.values_list("Animal_Name","Farmer_ID"))
    ani=list(Animal1.objects.values_list("Animal_Name",flat=True))
    print(ani,"sdjkfl")
    # if Request.POST["Animal_Name"] in d:

   # print(Far,"Far")
    print(iv[0].Animal_Name,iv[0].Farmer_ID,Farmer1.objects.filter(Farmer_Name=iv[0].Farmer_ID)[0].Farmer_id)
    k=(Request.POST["Animal_Name"],Farmer1.objects.filter(Farmer_Name=iv[0].Farmer_ID)[0].Farmer_id)
    print( k in  Far)
    if k in Far:
         return HttpResponse("you already register")
    Am=Request.POST["Animal_Amount"]
    farm = Request.POST.get('farmer')
    print(farm,"fdhg")
    farm=Farmer1.objects.get(Farmer_Name=farm)
    A=Animal1()
    A.Animal_Amount=Request.POST["Animal_Amount"]
    A.Farmer_ID=Farmer1.objects.get(Farmer_Name=farm)
    A.Doctor_ID=Doctor1.objects.get(Doctor_Name="irfan")
    A.Animal_Age=Request.POST["Animal_Age"]
    A.Animal_Loc="hyderabad"
    A.Animal_Name=Request.POST["Animal_Name"]
    A.Animal_Symptom=Request.POST["Animal_Symptom"]
    A.Animal_Image=Request.POST["Animal_Image"]
    A.save()
    print(farm,"dsfjk")
    print
    # A=Animal1.objects.filter(Farmer_ID= A.Farmer_ID)
    # print(A,"this ia a")
    # A.update(Animal_Age = Request.POST.get("Animal_Age"))
    # A.update(Animal_Amount = Request.POST.get("Animal_Amount"))
    # A.update(Animal_Name = Request.POST.get("Animal_Name"))
    # A.update(Animal_Symptom = Request.POST.get("Animal_Symptom"))
    #A.Animal_Image = Request.POST.get("Animal_Image")
    #A.Animal_Loc =  Request.POST.get("Animal_Loc")
    #print(f_id ,"werjkfjv") 
    Doc=Doctor1.objects.all()
    #print(Doc)
    return render(Request,"doctor.html",{"Doc":Doc,"a":a,"f":f,"Am":Am})


def db_details(Request):
    de=Details1()
    pay_id+=1
    de.Payment_Id=random.shuffle(list("spXjgs"))+random.shuffle(list("1q2w5e1"))
    de.Details_Farmer=random.shuffle("djbkbf")+str(dtl_id)
    de.Details_Prescription=Request.POST.get("Details_Prescription")
    de.Details_Status=Request.POST.get("Details_Status")
    de.Details_Amount=Request.POST.get("Details_Amount")
    de.save()
    return HttpResponse("<h2>register sucessful  db_details </h2>")


def  req(Request):
    print(Request.POST)
    de=Details1()
    
    o=list("spXjgs51458623Xxxdd")
    random.shuffle(o)
    print(Request.POST["Animal_Amount"],"animal_name")
    print(''.join(o),"payment_id",Request.POST["Farmer_Name"])
    de.Payment_Id=''.join(o)
    #print(Animal1.objects.get(Animal_Amount=Request.POST["Animal_Amount"]),"dsfjkb")
    de.Details_Farmer=Farmer1.objects.get(Farmer_Name=Request.POST["Farmer_Name"])
    de.Details_Doctor=Doctor1.objects.get(Doctor_ID=Request.POST["Doctor_ID"])
    #Ani_Name=Animal1.objects.values_list("Animal_Id" ,flat=True)
    De_Animal=list(Details1.objects.values_list("Details_Animal" ,flat=True))
    Fa=Farmer1.objects.filter(Farmer_Name=Request.POST["Farmer_Name"])
    d=Animal1.objects.filter(Animal_Name=Request.POST["Doctor_Name"],Farmer_ID=Fa[0].Farmer_id)
    print(d[0].Animal_Id,d[0],"this is d[0")
    #Ani_Name=Animal1.objects.filter(Animal_Id=)
    print(De_Animal,"animal_Name")
    print(Fa[0].Farmer_id,"farmer_id")

    de.Details_Animal=Animal1.objects.get(Animal_Name=Request.POST["Doctor_Name"],Farmer_ID=Fa[0].Farmer_id)

   # de.Details_Amount=Animal1.objects.get(Animal_Amount=Request.POST["Animal_Amount"])
    de.save()
   # return render(Request,"farmer_redirect.html",{"k":Request.POST["Farmer_Name"]})
    return redirect("farmer_redirect",k=str(Request.POST["Farmer_Name"]))
def Add_Animal(Request):
    print(Request.POST,"as")
    return render(Request,"info.html",{"farmer":Request.POST["farmer"]})
def display(Request):
    return render(Request,"display.html")