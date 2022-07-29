from django.shortcuts import render
from .models import *
from student_project.forms import *
from student_project.choice import *
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
def disp(Request):
    if Request.method=="POST":
        form=FirstName(Request.POST)
    else:
        form=FirstName()
    return render(Request,'sam.html',{"form":form})
def play(Request):
    if Request.method=="POST":
        form=ByChoice(Request.POST)
        #print(form ,"from kejhgfjxbh")
        if form.is_valid():
            cd=form.cleaned_data
            print(cd,"ekdjgk")

            if(cd["ch"]=="Roll_Number"):
                return render(Request,'sam.html',{"form":FirstName()})
            elif (cd["ch"]=="branch"):
                return render(Request,'form1.html',{"form":Branch()})
            
    else:
        form=ByChoice()
    return render(Request,'xyz.html',{"form":form})

def intra(Request):
    #if Request.POST['Roll_Number']=='18h61a12a0':
    try:
        student1=Student_Profile1.objects.all().filter(roll_no__icontains=Request.POST['Roll_Number'])
        marks=Student_Marks1.objects.all().filter(roll_no__icontains=Request.POST['Roll_Number'])
        subs=Student_Subjects1.objects.all().filter(roll_no__icontains=Request.POST['Roll_Number'])
        print(len(student1),"utwefjhhjdhj")
        
        context={"r":student1[0],"g":marks,"w":len(student1),"sub1":subs}

        return render(Request,'game.html',context)
    except:
        return render(Request,"invalid.html")
def bar(Request):
    if Request.method=="POST":
        form=Branch(Request.POST)
        #print(form)
        if form.is_valid():
            #cd=form.cleaned_data
            #print(cd["ch"],"wdasd")
            pro=Student_Profile1.objects.all().filter(branch_name__icontains=Request.POST['ch'])
            return render(Request,"test.html",{"r":pro})
    
            # if cd["ch"]=="Info":
            #    pro=Student_Profile1.objects.all().filter(branch_name__icontains=Request.POST['ch'])
            #    return render(Request,"test.html",{"r":pro[0]})
            # elif cd["ch"]=="cse":
            #    pro=Student_Profile1.objects.all().filter(branch_name__icontains=Request.POST['ch'])
            #    return render(Request,"test.html",{"r":pro[0]})
            # elif cd["ch"]=="eee":
            #    pro=Student_Profile1.objects.all().filter(branch_name__icontains=Request.POST['ch'])
            #    return render(Request,"test.html",{"r":pro[0]})
            # elif cd["ch"]=="mechanical":
            #    pro=Student_Profile1.ob    jects.all().filter(branch_name__icontains=Request.POST['ch'])
            #    return render(Request,"test.html",{"r":pro[0]})
            # if cd["ch"]=="Pharmacy":
            #    pro=Student_Profile1.objects.all().filter(branch_name__icontains=Request.POST['ch'])
            #    return render(Request,"test.html",{"r":pro[0]})          
    else:
        form=ByChoice()
        # pro="g"
    return render(Request,"form12.html",{"r":pro})
def disp1(Request):
    if Request.method=="POST":
        form=Branch(Request.POST)
    else:
        form=Branch()
    return render(Request,'form2.html',{"form":form})
def search_roll(Request):
    return render(Request,'sam.html',{"form":FirstName()})
def search_branch(Request):
    return render(Request,'form1.html',{"form":Branch()})
def marks(Request):
    return render(Request,"marks.html")
def branch(Request):
     pro=Student_Profile1.objects.all().filter(branch_name__icontains=Request.POST['branch'])
     return render(Request,"test.html",{"r":pro})
def branch1(Request):
    print(Request.POST)
    if Request.POST['branch1']=='none':
        student1=Student_Profile1.objects.all().filter(roll_no__icontains=Request.POST['Roll_Number'])
        return render(Request ,"search_field.html",{"i":student1})
    else :
         br=Student_Profile1.objects.all().filter(branch_name__icontains=Request.POST['branch1'],roll_no__icontains=Request.POST['Roll_Number'])
         l=len(br)
         return  render(Request,"branch.html",{"cs":br,"l":l})
def s_f(Request):

    if Request.method == "POST":
        student1=Student_Profile1.objects.all().filter(roll_no__icontains=Request.POST['Roll_Number'])
        return render(Request ,"search_field.html",{"i":student1})
    stu=Student_Profile1.objects.all()
    
    return render(Request,"s_f.html",{"s":stu})
def b_n(Request):
    return render(Request,'form1.html',{"form":Branch()})
    
def  cse(Request):
     br=Student_Profile1.objects.all().filter(branch_name__icontains='cse')
     print(br)
     return  render(Request,"branch.html",{"cs":br})
  

def info(Request):
     br=Student_Profile1.objects.all().filter(branch_name__icontains='info')
     print(br)
     return  render(Request,"branch.html",{"cs":br})

def eee(Request):
     br=Student_Profile1.objects.all().filter(branch_name__icontains='eee')
     print(br)
     return  render(Request,"branch.html",{"cs":br})
def Pharmacy(Request):
     br=Student_Profile1.objects.all().filter(branch_name__icontains='Pharmacy')
     print(br)
     return  render(Request,"branch.html",{"cs":br})

def mechanical(Request):
     br=Student_Profile1.objects.all().filter(branch_name__icontains='cse')
     print(br)
     return  render(Request,"branch.html",{"cs":br})

def home(Request):
    return render(Request,"home.html")
def fun(Request):
    return render(Request,"reg.html")
def sid(Request):
    return render(Request ,"game.html")
def first(Request):
    return render(Request,"sample.html")
def rgt(Request):
    #  name=Request.POST["name"]
    #  branch_name1=Request.POST["branch_name"]
    #  duration=Request.POST["duration"]
    #  degree_type=Request.POST["degree_type "]
    #  roll_no=Request.POST["roll_no"]
    #  father_name=Request.POST["father_name"]
    #  sex=Request.POST["sex"]
    # #  print(Request.FILES["pic"],"djkgh")
    #  pic=Request.FILES["pic"]
    #  strg="Student/"
    #  f=FileSystemStorage(location=strg,base_url=strg)
    #  fs=f.save(pic)
    #  file_url=f.url(fs)
    #  res=Student_Profile1()
    #  res.name=name
    #  res.branch_name=branch_name1
    #  res.duration=duration
    #  res.branch_name=branch_name1
    #  res.degree_type=degree_type
    #  res.roll_no=roll_no
    #  res.father_name=father_name
    #  res.sex=sex
    #  res.pic=file_url
    #  res.save()
     

      if Request.method == "POST":
           #print("hi")
        #if Request.Student_Profile1.get("name") and Request.Student_Profile1.get("branch_name") and Request.Student_Profile1.get("duration") and Request.Student_Profile1.get("degree_type") and Request.Student_Profile1.get("roll_no") and Request.Student_Profile1.get("father_name") and Request.Student_Profile1.get("sex") :
           res=Student_Profile1()
           res.name=Request.POST.get("name")
           res.branch_name=Request.POST.get("branch_name")
           res.duration=Request.POST.get("duration")
           res.degree_type=Request.POST.get("degree_type")
           res.roll_no=Request.POST.get("roll_no")
           res.father_name=Request.POST.get("father_name")
           res.sex=Request.POST.get("sex")
           #print(res.sex,"ueagy")
           #print(Request.FILES)
        #    return render(Request,"test.html",{"gen":res.sex})

           pic=Request.FILES.get("pic")
        #    pic=Request.getlist('pic')
           
           fss=FileSystemStorage()
           #print(pic,"jkfh")
           file=fss.save(pic.name, pic)
           file_url=fss.url(file)
           res.img=file_url
           res.save()
           return render(Request,"marks.html")
           
           
      else:
        res=Student_Profile1()
      

def sucess(Request):
    return render(Request,"sucess.html")
def details(Request):
        # if Request.method == "POST":
         #  print(Request,"Request")
           res1=Student_Marks1()
           res2=Student_Subjects1()
        #   print(Request.POST.get("Sem_Id3"),"sem")

           res2.sem_id=Request.POST.get("Sem_Id1")
           res2.save()
           res1.ind=Request.POST.get("Sem_Id1")[0:3]+Request.POST.get("s1")
           res1.save()
           res1.sem_id=Request.POST.get("Sem_Id1")
           res2.sub_name1=Request.POST.get("s1")
           res2.save()
           res1.save()
           res1.grade=Request.POST.get("g1")
           res2.roll_no=Request.POST.get("roll_no")
           res2.save()
           res1.save()
           res1.roll_no=Request.POST.get("roll_no")
           res1.save()
           res1.pass_fail=Request.POST.get("pf1")
           res1.save()
           res1.credits=Request.POST.get("c1")
           res1.save()
           res1.total_marks=Request.POST.get("m1")
           res1.save()
           res2.sub_name2=Request.POST.get("s2")
           res2.save()
           res1.grade=Request.POST.get("g2")
           res1.save()
           res1.ind=Request.POST.get("Sem_Id1")[0:3]+Request.POST.get("s2")
           res1.save()
        #   print(Request.POST.get("roll_no"),"Reques")
           res1.save()
           
           res2.roll_no=Request.POST.get("roll_no")
           res2.save()
           res1.pass_fail=Request.POST.get("pf2")
           res1.save()
           res1.credits=Request.POST.get("c2")
           res1.save()
           res1.total_marks=Request.POST.get("m2")
           res1.save()
           res2.sub_name3=Request.POST.get("s3")
           res1.grade=Request.POST.get("g3")
           res1.ind=Request.POST.get("Sem_Id1")[0:3]+Request.POST.get("s3")
           res1.save()
           res2.roll_no=Request.POST.get("roll_no")
           res2.save()
           res1.pass_fail=Request.POST.get("pf3")
           res1.save()
           res1.credits=Request.POST.get("c3")
           res1.save()
           res1.total_marks=Request.POST.get("m3")
           res2.save()
           res1.save()
           res2.sem_id=Request.POST.get("Sem_Id2")
           res1.sem_id=Request.POST.get("Sem_Id2")
           res1.save()
           res1.ind=Request.POST.get("Sem_Id2")[0:3]+Request.POST.get("s4")
           res1.save()
           res2.sub_name1=Request.POST.get("s4")
           res2.roll_no=Request.POST.get("roll_no")     
           res1.roll_no=Request.POST.get("roll_no") 
           res1.save()    
           res1.grade=Request.POST.get("g4")
           res1.save()
           res1.pass_fail=Request.POST.get("pf4")
           res1.save()
           res1.credits=Request.POST.get("c4")
           res1.save()
           res1.total_marks=Request.POST.get("m4")
           res1.save()

           res2.sub_name2=Request.POST.get("s5")
           res1.grade=Request.POST.get("g5")
           res1.save()
           res1.ind=Request.POST.get("Sem_Id2")[0:3]+Request.POST.get("s5")
           res1.save()
           res2.roll_no=Request.POST.get("roll_no")
           res1.pass_fail=Request.POST.get("pf5")
           res1.save()
           res1.credits=Request.POST.get("c5")
           res1.save()
           res1.total_marks=Request.POST.get("m5")
           res1.save()

           res2.sub_name3=Request.POST.get("s6")
           res2.save()
           res1.grade=Request.POST.get("g6")
           res1.save()
           res2.roll_no=Request.POST.get("roll_no")
           res2.save()
           res1.ind=Request.POST.get("Sem_Id2")[0:3]+Request.POST.get("s6")
           res1.save()
           res1.pass_fail=Request.POST.get("pf6")
           res1.save()
           res1.credits=Request.POST.get("c6")
           res1.save()
           res1.total_marks=Request.POST.get("m6")
           res1.save()
         
           res2.sem_id=Request.POST.get("Sem_Id3")
           res2.save()
          # print(Request.POST.get("Sem_Id3"),"oiuhwefkjb")
           res1.sem_id=Request.POST.get("Sem_Id3")
           res1.ind=Request.POST.get("Sem_Id3")[0:3]+Request.POST.get("s7")
           res1.save()
           res2.sub_name1=Request.POST.get("s7")
           res2.save()
           res1.grade=Request.POST.get("g7")
           res1.save()
           res1.pass_fail=Request.POST.get("pf7")
           res1.save()
           res2.roll_no=Request.POST.get("roll_no")
           res2.save()
           res2.roll_no=Request.POST.get("roll_no")  
           res2.save() 
           res1.credits=Request.POST.get("c7")
           res1.save()
           res1.total_marks=Request.POST.get("m7")
           res1.save()
           res2.sub_name2=Request.POST.get("s8")
           res2.save()
           res1.grade=Request.POST.get("g8")
           res1.save()
           res1.ind=Request.POST.get("Sem_Id3")[0:3]+Request.POST.get("s8")
           res1.save()
           res1.pass_fail=Request.POST.get("pf8")
           res1.save()
           res2.roll_no=Request.POST.get("roll_no")
           res2.save()
           res1.credits=Request.POST.get("c8")
           res1.save()
           res1.total_marks=Request.POST.get("m8")
           res1.save()

           res2.sub_name3=Request.POST.get("s9")
           res2.save()
           res1.grade=Request.POST.get("g9")
           res1.save()
           res1.ind=Request.POST.get("Sem_Id3")[0:3]+Request.POST.get("s9")
           res1.save()
           res1.pass_fail=Request.POST.get("pf9")
           res1.save()
           res2.roll_no=Request.POST.get("roll_no")
           res2.save()
          
           res1.credits=Request.POST.get("c9")
           res1.save()
           res1.total_marks=Request.POST.get("m9")
           res1.save()

           res2.save()
           res1.save()
           return HttpResponse("<h1> Registration Sucessfull</h1>")

           