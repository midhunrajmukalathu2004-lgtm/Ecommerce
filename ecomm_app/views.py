from django.shortcuts import render
from .models import Tb_user
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,'home.html')


# ---------------------Login-----------------------------------------
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        login_password = request.POST['login_password']
        # user_role = request.POST['user_role']
        Tb_user.objects.all()
        user = Tb_user.objects.filter(
            full_name = username,password = login_password,
        )
        if user:
            # print("Login Success")
            for x in user:
                request.session['my_id']=x.id
                if x.id == 4:
                    return render(request,'Admin/admin_home.html') 
 
                else:
                    return render(request,'User/user_home.html')

        else:
            return render(request, 'login.html', {
                'error': 'Invalid Username or password!!'
                })
    return render(request,'login.html')    
            
    


# ------------------------------Register----------------------------
def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        user_role = request.POST['user_role']
        Tb_user(full_name = name,email = email,phone_no = phone,password = password,user_role=user_role).save()
        # if user_role=='user':
        #     return render(request,'User/user_home.html')
        # elif user_role == 'admin':
        #     return render(request,'Admin/admin_home.html')
        return render('login.html')
    return render(request,'register.html')


#tb_name(colomn_name = variable_name)
def user_home(request):
    return render(request,'User/user_home.html')

# ------------------------user--------------------------------
def userprofile(request):
    userid = request.session.get('my_id')
    print(userid)

    data = Tb_user.objects.get(id=userid)

    return render(request, 'User/userprofile.html', {'user': data})

def user_edit(request):
    userid = request.session['my_id']
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        Tb_user.objects.filter(id = userid).update(full_name=name,email=email,phone_no=phone)
        # return render(request,'User/user_edit.html')
        return HttpResponseRedirect('/userprofile/')
    else:
        data = Tb_user.objects.filter(id=userid)
        return render(request,'User/user_edit.html',{'data':data})
    
  




# ---------------------admin-------------------------------------
def admin_home(request):
    return render(request,'admin_home.html')

def manage_user(request):
    if request.session.get('my_id')!=4:
        return HttpResponseRedirect('/login/')
    data = Tb_user.objects.exclude(id=4)
    return render(request,'Admin/manage_user.html',{'data':data})

def delete_user(request,id):
    data = Tb_user.objects.get(id=id)

    if request.method == 'POST':
        data.delete()
        return HttpResponseRedirect('/manage_user/')

    return render(request,'Admin/delete_user.html',{'data':data})




def products(request):
    return render(request,'User/user_home.html')

