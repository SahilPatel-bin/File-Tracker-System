from django.shortcuts import render, redirect
from .models import User_Registration, User, Department, File_Create, Division, Design, Notification,Role
from django.contrib.auth import authenticate
from django.db.models import Q
from django.http import JsonResponse
from datetime import datetime,date,timedelta

def fileData(startDate,endDate,department,file_status):
    date = datetime.strptime(endDate,'%Y-%m-%d').date()
    newDate = date + timedelta(days=1)
    endDate = newDate.strftime('%Y-%m-%d')
    if file_status=='all' :
        fileData = File_Create.objects.filter(scode=department,file_created_date__range=(startDate,endDate))
    else :
        fileData = File_Create.objects.filter(scode=department,file_created_date__range=(startDate,endDate),file_status=file_status)

    data = []
    for i in fileData:
        file_name = i.file_name
        section = department
        subject = i.file_title
        created_date = i.file_created_date
        putup = i.file_put_uname

        current_user_notification = Notification.objects.exclude(action='Forward').get(file_name=file_name)
        if i.file_status == 'CREATE':
            current_user = ''
        else :
            current_user = current_user_notification.receive_uname
        if current_user == 'null':
            current_user = current_user_notification.sender_uname

        status = i.file_status

        data.append({'file_name':file_name,'section':section,"subject":subject,"created_date": created_date,
                         'putup':putup, 'current_user':current_user , 'status':status})

    return data

# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        data = User_Registration.objects.filter(email=email, password=password).values()

        if data:
            request.session['username'] = data[0]['username']
            return redirect('/home/')
        else:
            return render(request, 'login.html', {'status': -1})

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        query = User_Registration(
            username=username, email=email, moblie_No=phone, password=password)
        query.save()
        return redirect('/login/')

    return render(request, 'signup.html')


def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        data = User_Registration.objects.get(email=email)
        data.password = password
        data.save()
        return redirect('/login/')

    return render(request, 'forgotPassword.html')


def logout(request):
    del request.session['username']
    return redirect('/login/')

def home(request):
    return redirect('/home/')

def index(request):
    if request.session.get('username'):
        return render(request, 'index.html')
    else:
        return redirect('/login/')


def manageProfile(request):
    if request.session.get('username'):
        if request.method == 'POST':
            email = request.POST['email']
            phone = request.POST['phone']
            userDate = User.objects.get(adminname=request.session['username'])
            userDate.email = email
            userDate.phone = phone
            userDate.save()
            return redirect('/home/')
        else :
            userDate = User.objects.get(adminname=request.session['username'])
            data = {'email':userDate.email, 'phone': userDate.phone}
            return render(request, 'manageProfile.html',data)
    else:
        return redirect('/login/')


def dashboard(request):
    if request.session.get('username'):
        totalFiles = File_Create.objects.filter(file_put_uname=request.session['username']).count()
        fileCreate = File_Create.objects.filter(file_put_uname=request.session['username'],file_status='Create').count()
        fileInprocess = File_Create.objects.filter(file_put_uname=request.session['username'],file_status='InProcess').count()
        fileApprove = File_Create.objects.filter(file_put_uname=request.session['username'],file_status='APPROVED').count()
        fileReject = File_Create.objects.filter(file_put_uname=request.session['username'],file_status='REJECTED').count()
        fileCancel = File_Create.objects.filter(file_put_uname=request.session['username'],file_status='Cancel').count()

        pendingFile = {}
        fileList = File_Create.objects.filter(file_put_uname=request.session['username'],file_status='InProcess').values('file_name').distinct()
        for i in fileList :
            username = Notification.objects.exclude(action='Forward').get(file_name=i['file_name']).receive_uname
            sendDate = Notification.objects.filter(file_name=i['file_name']).values('sender_date').first()
            department = User.objects.get(adminname=username).department_id
            department = Department.objects.get(id=department).scode

            if department not in fileList :
                pendingFile[department] = [0,0,0,0,0]
            pendingFile[department][0] = pendingFile[department][0] + 1

            delta = date.today() - sendDate['sender_date'].date()
            delta = delta.days

            if delta<7 :
                pendingFile[department][1] = pendingFile[department][1] + 1
            elif delta>=7 and delta<16 :
                pendingFile[department][2] = pendingFile[department][2] + 1
            elif delta>=16 and delta<31:
                pendingFile[department][3] = pendingFile[department][3] + 1
            else :
                pendingFile[department][4] = pendingFile[department][4] + 1

        total = {'totalFiles' : totalFiles,'fileCreate' : fileCreate, 'fileInprocess' : fileInprocess, 'fileApprove' : fileApprove, 
                 'fileReject' : fileReject, 'fileCancel' : fileCancel, 'department':pendingFile}
        
        return render(request, 'dashboard.html',total)
    else:
        return redirect('/login/')


def fileManagement(request):
    if request.session.get('username'):
        if request.session.get('title'):
            del request.session['title']
        user = User.objects.get(adminname=request.session['username'])
        userData = File_Create.objects.filter(file_put_user_id=user.id)
        print(userData)
        return render(request, 'fileManagement.html', {'data': userData})
    else:
        return redirect('/login/')


def addFile(request):
    if request.session.get('username'):
        if request.method == 'POST':
            userData = User.objects.get(adminname=request.session['username'])

            departmentData = Department.objects.get(id=userData.department_id)
            dept_id = userData.department_id
            sid = File_Create.objects.filter(dept_id=dept_id).count()+1
            scode = departmentData.scode
            design_id = userData.design_id
            file_name = f"{scode}{sid}"
            file_title = request.POST['fileSubject']
            file_desc = request.POST['fileDescription']
            if request.FILES.get('document') != None :
                document = request.FILES['document']
            else :
                document = "NULL"

            now = datetime.now()
            file_created_date = now
            file_put_user_id = userData.id
            file_put_uname = userData.adminname
            file_status = 'CREATE'

            file_status_date = now
            last_update_user_id = userData.id
            last_update_date = now
            queue = File_Create(scode=scode, sid=sid, dept_id=dept_id, design_id=design_id, file_name=file_name, file_title=file_title, file_desc=file_desc, file_created_date=file_created_date,document=document,
                                file_put_user_id=file_put_user_id, file_put_uname=file_put_uname, file_status=file_status, file_status_date=file_status_date, last_update_user_id=last_update_user_id, last_update_date=last_update_date)
            queue.save()
            return redirect('/fileManagement/')
        return render(request, 'addNewFile.html')
    else:
        return redirect('/login/')


def updateFileData(request):
    if request.session.get('username'):
        if request.POST['update'] == '1':
            file_title = request.POST['fileSubject']
            file_desc = request.POST['fileDescription']
            fileData = File_Create.objects.get(file_name=request.session.get('title'))
            fileData.file_title = file_title
            fileData.file_desc = file_desc

            if request.FILES.get('document') != None :
                fileData.document = request.FILES['document']
            else :
                fileData.document = "NULL"
    
            del request.session['title']
            fileData.save()
            return redirect('/fileManagement/')
        else:
            filetitle = request.POST['file_title']
            userData = File_Create.objects.get(
                file_name=filetitle)
            fileDescription = userData.file_desc
            request.session['title'] = filetitle
            filetitle = userData.file_title
            document = userData.document
        return render(request, 'addNewFile.html', {'title': filetitle, 'desc': fileDescription,'document':document})

    else:
        return redirect('/login/')


def notificationDetails(request):
    if request.session.get('username'):
        if request.POST['insert'] == "1":
            file_name = request.POST['name']
            fileData = File_Create.objects.get(file_name=file_name)
            file_id = fileData.id
            sender_user_id = fileData.file_put_user_id
            sender_uname = fileData.file_put_uname

            now = datetime.now()
            sender_date = now
            

            userData = User.objects.get(id=request.POST['user'])
            receive_user_id = request.POST['user']
            action_remarks = request.POST['userComment']
            receive_uname = userData.adminname

            action = 'UnRead'
            action_read_date = now
            action_date = now

            last_update_user_id = sender_user_id
            last_update_date = sender_date

            queue = Notification(file_id=file_id, file_name=file_name, sender_user_id=sender_user_id, sender_uname=sender_uname, sender_date=sender_date, receive_user_id=receive_user_id,
                                 receive_uname=receive_uname, action=action, action_read_date=action_read_date, action_date=action_date, last_update_user_id=last_update_user_id, 
                                 last_update_date=last_update_date,action_remarks = action_remarks)
            queue.save()
            fileData.file_status = 'InProcess'
            fileData.save()
            return redirect('/fileManagement/')
        else:
            officeData = Division.objects.all().order_by('division_name')
            departmentData = Department.objects.all().order_by('department_name')
            title = request.POST['title']
            fileData = File_Create.objects.get(file_name=title)
            return render(request, 'notificationDetails.html', {'file': fileData, 'office': officeData, 'department': departmentData})
    else:
        return redirect('/login/')


def load_users(request):
    if request.session.get('username'):
        division_code = request.POST.get('officeLocation')
        department_id = request.POST.get('department')
        users = User.objects.filter(
            division_code=division_code, department_id=department_id).exclude(adminname=request.session['username']).order_by('adminname')

        users_list = []
        for i in users:
            design = Design.objects.get(id=i.design_id)
            users_list.append(
                {'id': i.id, 'name': f"{i.adminname} ({design.designation})"})

        return JsonResponse({'users': users_list})


def notification(request):
    if request.session.get('username'):
        notificationData = Notification.objects.filter(receive_uname=request.session['username']).exclude(action='Forward')
        data = []
        userData = User.objects.get(adminname=request.session['username'])
        role = Role.objects.get(id=userData.role_id).role_name
        department = Department.objects.get(id=userData.department_id).scode

        for i in notificationData:
            if File_Create.objects.get(file_name=i.file_name).file_status == 'InProcess':
                data.append({'id': i.id ,'file_code': i.file_name, 'file_subject':File_Create.objects.get(file_name=i.file_name).file_title,
                         'sender_user' : i.sender_uname , 'send_date' : i.sender_date , 'status': i.action ,'section': department })
    
        return render(request, 'notification.html',{'data':data,'role':role})
    else:
        return redirect('/login/')

def readFile(request):
    if request.session.get('username'):
        notificationData =  Notification.objects.get(id=int(request.POST['file_id']))
        notificationData.action = 'Read'
        now = datetime.now()
        notificationData.action_read_date = now
        notificationData.action_date = now
        notificationData.save()
        return redirect('/notification/')
    else :
        return redirect('/login/')
    
def notificationForward(request):
    if request.session.get('username'):
        if request.POST['insert'] == "0":
            officeData = Division.objects.all().order_by('division_name')
            departmentData = Department.objects.all().order_by('department_name')
            title = request.POST['file_code']
            fileData = File_Create.objects.get(file_name=title)
            data  = []
            notification = Notification.objects.filter(file_name=title)
            for i in notification :
                userData = User.objects.get(adminname=i.sender_uname)
                section = Department.objects.get(id=userData.department_id).scode
                senderUser = f"{userData.adminname} ({Design.objects.get(id=userData.design_id).designation},{Division.objects.get(division_code=userData.division_code).division_name})"
                data.append({'section':section,'senderUser':senderUser,'sender_date':i.sender_date, 'action_read_date':i.action_read_date,
                             'action':i.action, 'action_remarks':i.action_remarks})
                
            return render(request, 'notificationForward.html', {'file': fileData, 'office': officeData, 'department': departmentData, 'data':data})
        
        else :

            fileData = File_Create.objects.get(file_name=request.POST['name'])
            file_id = fileData.id
            file_name = fileData.file_name

            userData = User.objects.get(adminname=request.session['username'])
            sender_user_id = userData.id
            sender_uname = userData.adminname
            now = datetime.now()
            sender_date = now

            receive_user_id = request.POST['user']
            receive_uname = User.objects.get(id=receive_user_id).adminname
            action = 'UnRead'
            action_read_date = now
            if request.POST.get('userComment') != None :
                action_remarks = request.POST['userComment']
            else :
                action_remarks = ""
            action_date = now

            last_update_user_id = sender_user_id
            last_update_date = sender_date

            notification = Notification.objects.exclude(action='Forward').get(receive_user_id=sender_user_id,file_name=file_name,file_id=file_id)
            notification.action = 'Forward'
            notification.action_date = now
            notification.save()
            
            queue = Notification(file_id=file_id, file_name=file_name, sender_user_id=sender_user_id, sender_uname=sender_uname, sender_date=sender_date, receive_user_id=receive_user_id,
                                 receive_uname=receive_uname, action=action, action_read_date=action_read_date, action_remarks=action_remarks,action_date=action_date, 
                                 last_update_user_id=last_update_user_id, last_update_date=last_update_date)
            queue.save()

            return redirect('/notification/')
    else :
        return redirect('/login/')

def notificationClose(request):
    if request.session['username']:
        if request.POST['insert'] == "0":
            title = request.POST['file_code']
            fileData = File_Create.objects.get(file_name=title)
            data  = []

            notification = Notification.objects.filter(file_name=title)
            for i in notification :
                userData = User.objects.get(adminname=i.sender_uname)
                section = Department.objects.get(id=userData.department_id).scode
                senderUser = f"{userData.adminname} ({Design.objects.get(id=userData.design_id).designation},{Division.objects.get(division_code=userData.division_code).division_name})"
                data.append({'section':section,'senderUser':senderUser,'sender_date':i.sender_date, 'action_read_date':i.action_read_date,
                             'action':i.action, 'action_remarks':i.action_remarks})
            return render(request, 'notificationClose.html', {'file': fileData, 'data':data})

        else :
            fileData = File_Create.objects.get(file_name=request.POST['name'])
            file_id = fileData.id
            file_name = fileData.file_name

            userData = User.objects.get(adminname=request.session['username'])
            sender_user_id = userData.id
            sender_uname = userData.adminname
            now = datetime.now()
            sender_date = now

            action = 'Read'
            action_read_date = now
            if request.POST.get('userComment') != None :
                action_remarks = request.POST['userComment']
            else :
                action_remarks = ""
            action_date = now

            last_update_user_id = sender_user_id
            last_update_date = sender_date

            notification = Notification.objects.exclude(action='Forward').get(receive_user_id=sender_user_id,file_name=file_name,file_id=file_id)
            notification.action = 'Forward'
            notification.action_date = now
            notification.save()

            queue = Notification(file_id=file_id, file_name=file_name, sender_user_id=sender_user_id, sender_uname=sender_uname, sender_date=sender_date,
                                 action=action, action_read_date=action_read_date, action_remarks=action_remarks,action_date=action_date, 
                                 last_update_user_id=last_update_user_id, last_update_date=last_update_date)
            queue.save()

            fileData.file_status = request.POST['status']
            fileData.save()
            return redirect('/notification/')
    else :
        return redirect('/login/')

def fileReports(request):
    if request.session['username']:
        if request.method == 'POST':
            startDate = request.POST['fromDate']
            endDate = request.POST['toDate']
            department = request.POST['department']
            file_status = request.POST['status']

            data = fileData(startDate,endDate,department,file_status)
            return render(request,'fileReports.html',{'department':department, 'data':data, 'startDate':startDate,
                                                      'endDate':endDate, 'file_status':file_status})  
        else :
            department = User.objects.get(adminname=request.session['username']).department_id
            department = Department.objects.get(id=department).scode
            endDate = date.today()
            startDate = endDate - timedelta(days=30)
            endDate = endDate.strftime("%Y-%m-%d")
            data = fileData(startDate,endDate,department,'all')
            
            return render(request,'fileReports.html',{'department':department,'data':data})
    else :
        return redirect('/login/')

def searchFiles(request):
    if request.session['username']:
        search = request.POST['search']
        user = User.objects.get(adminname=request.session['username'])
        data = File_Create.objects.filter((Q(file_name__icontains=search) | Q(file_title__icontains=search) | Q(file_put_uname__icontains=search) | Q(file_created_date__icontains=search) | Q(file_status__icontains=search)) & Q(file_put_user_id=user.id))

        return render(request,'fileManagement.html',{'data':data})
    else :
        return redirect('/login/')
    
def printData(request):
    if request.session['username']:
        title = request.POST['file_code']
        fileData = File_Create.objects.get(file_name=title)
        data  = []

        notification = Notification.objects.filter(file_name=title)
        for i in notification :
            userData = User.objects.get(adminname=i.sender_uname)
            section = Department.objects.get(id=userData.department_id).scode
            senderUser = f"{userData.adminname} ({Design.objects.get(id=userData.design_id).designation},{Division.objects.get(division_code=userData.division_code).division_name})"
            data.append({'section':section,'senderUser':senderUser,'sender_date':i.sender_date, 'action_read_date':i.action_read_date,
                             'action':i.action, 'action_remarks':i.action_remarks})
        return render(request,'printData.html',{'file':fileData , 'data': data})
    else :
        return redirect('/login/')