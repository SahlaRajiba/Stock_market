from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages, auth
# Create your views here.
from stock.models import *
from .gru_python_aave import *

def main(request):
    return render(request,'index.html')

@login_required(login_url='/')
def add_and_manage_expert(request):
    ob=expert.objects.all()
    return render(request,'add and manage expert.html',{'val':ob})

@login_required(login_url='/')
def add_complaint(request):
    return render(request,'add complaint.html')

@login_required(login_url='/')
def add_expert(request):
    return render(request,'add expert.html')

@login_required(login_url='/')
def add_notification(request):
    return render(request,'add notification.html')

@login_required(login_url='/')
def admin_home(request):
    return render(request,'admin home.html')

@login_required(login_url='/')
def ask_doubt(request):
    ob = doubt.objects.filter(uid__lid__id=request.session['lid'])
    return render(request,'ask doubt.html',{'val':ob})

@login_required(login_url='/')
def block_unblock(request):
    ob = expert.objects.all()
    return render(request,'block nd unblock.html',{'val':ob})

@login_required(login_url='/')
def expert_add(request):
    return render(request,'expert add.html')

@login_required(login_url='/')
def expert_home(request):
    return render(request,'expert home.html')

@login_required(login_url='/')
def notifications(request):
    ob = notification.objects.filter(eid__lid__id=request.session['lid'])
    return render(request,'notication.html',{'val':ob})


def register(request):
    return render(request,'register.html')

@login_required(login_url='/')
def reply(request):
    return render(request,'reply.html')

@login_required(login_url='/')
def send_complaint(request):
    ob = complaint.objects.filter(uid__lid__id=request.session['lid'])
    return render(request,'send complaint.html',{'val':ob})

@login_required(login_url='/')
def send_doubt_reply(request):
    return render(request,'send doubt reply.html')

@login_required(login_url='/')
def send_doubts(request):
    ob=expert.objects.all()
    return render(request,'send doubts.html',{'val':ob})

@login_required(login_url='/')
def send_ratings(request):
    ob= expert.objects.all()
    return render(request,'send rating.html',{'val':ob})

@login_required(login_url='/')
def send_tips(request):
    ob = tips.objects.filter(eid__lid__id=request.session['lid'])
    return render(request,'send tips.html',{'val':ob})

@login_required(login_url='/')
def tips_send_user(request):
    return render(request,'tips send user.html')

@login_required(login_url='/')
def user_home(request):
    return render(request,'user home.html')

@login_required(login_url='/')
def user_rating(request):
    return render(request,'user rating.html')

@login_required(login_url='/')
def view_complaint(request):
    ob=complaint.objects.all()
    return render(request,'view complaint.html',{'val':ob})

@login_required(login_url='/')
def view_doubts_and_reply(request):
    ob=doubt.objects.filter(eid__lid__id=request.session['lid'])
    return render(request,'view doubts and reply.html',{'val':ob})

@login_required(login_url='/')
def view_expert(request):
    ob = rating.objects.all()
    return render(request,'view expert.html',{'val':ob})

@login_required(login_url='/')
def view_notification(request):
    ob=notification.objects.all()
    return render(request,'view notification.html',{'val':ob})

@login_required(login_url='/')
def view_rating(request):
    ob=expert.objects.all()
    return render(request,'view rating.html',{'val':ob})

@login_required(login_url='/')
def view_rating_expert(request):
    ob=rating.objects.filter(eid__lid__id=request.session['lid'])
    return render(request,'view rating expert.html',{'val':ob})

@login_required(login_url='/')
def view_tips(request):
    ob=tips.objects.all()
    return render(request,'view tips.html',{'val':ob})

def regcode(request):
    fname=request.POST['textfield']
    lname=request.POST['textfield2']
    plce=request.POST['textfield3']
    pst=request.POST['textfield4']
    pn=request.POST['textfield5']
    phne=request.POST['textfield6']
    mail=request.POST['textfield7']
    uname=request.POST['textfield8']
    passwd=request.POST['textfield9']
    ob=login()
    ob.username=uname
    ob.password=passwd
    ob.type='user'
    ob.save()
    iob=user()
    iob.firstname=fname
    iob.lastname=lname
    iob.place=plce
    iob.pin=pn
    iob.post=pst
    iob.phone=phne
    iob.email=mail
    iob.lid=ob
    iob.save()
    messages.success(request, 'Registered')
    return HttpResponse('''<script>window.location='/'</script>''')

def logincode(request):
    uname=request.POST['textfield']
    pword=request.POST['textfield2']
    try:
        ob=login.objects.get(username=uname,password=pword)
        if ob.type == 'admin':
            ob1=auth.authenticate(username='admin',password='admin')
            auth.login(request,ob1)
            messages.success(request, 'welcome to admin home page')
            return HttpResponse('''<script>window.location='/admin_home'</script>''')
        elif ob.type == 'expert':
            request.session['lid']=ob.id
            ob1 = auth.authenticate(username='admin', password='admin')
            auth.login(request, ob1)
            messages.success(request, 'welcome to expert home page')
            return HttpResponse('''<script>window.location='/expert_home'</script>''')
        elif ob.type == 'user':
            request.session['lid'] = ob.id
            ob1 = auth.authenticate(username='admin', password='admin')
            auth.login(request, ob1)
            messages.success(request, 'welcome to user home page')
            return HttpResponse('''<script>window.location='/user_home'</script>''')
        else:
            messages.success(request, 'invalid')
            return  HttpResponse('''<script>window.location='/'</script>''')
    except Exception as e:
        # print("1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",e)
        messages.success(request, 'invalid')
        return HttpResponse('''<script>window.location='/'</script>''')



@login_required(login_url='/')
def expertcode(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    plce=request.POST['place']
    pst=request.POST['post']
    pn=request.POST['pin']
    phne=request.POST['phone']
    mail=request.POST['email']
    uname=request.POST['uname']
    passwd=request.POST['pw']
    ob=login()
    ob.username=uname
    ob.password=passwd
    ob.type='expert'
    ob.save()
    iob=expert()
    iob.firstname=fname
    iob.lastname=lname
    iob.place=plce
    iob.pin=pn
    iob.post=pst
    iob.phone=phne
    iob.email=mail
    iob.lid=ob
    iob.save()
    messages.success(request, 'expert added')
    return HttpResponse('''<script>window.location='/add_and_manage_expert#about'</script>''')

@login_required(login_url='/')
def expert_edit(request,id):
    ob=expert.objects.get(id=id)
    request.session['eid']=id
    return render(request,'expert edit.html',{'val':ob})

@login_required(login_url='/')
def exeditcode(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    plce = request.POST['place']
    pst = request.POST['post']
    pn = request.POST['pin']
    phne = request.POST['phone']
    mail = request.POST['email']
    ob=expert.objects.get(id=request.session['eid'])
    ob.firstname = fname
    ob.lastname = lname
    ob.place = plce
    ob.pin = pn
    ob.post = pst
    ob.phone = phne
    ob.email = mail
    ob.save()
    messages.success(request, 'expert edited')
    return HttpResponse('''<script>window.location='/add_and_manage_expert#about'</script>''')

@login_required(login_url='/')
def exdeletecode(request,id):
    ob=expert.objects.get(lid__id=id)
    ob.delete()
    iob=login.objects.get(id=id)
    iob.delete()
    messages.success(request, 'deleted')
    return HttpResponse('''<script>window.location='/add_and_manage_expert#about'</script>''')

@login_required(login_url='/')
def addnoticode(request):
    notif=request.POST['textfield']
    ob=notification()
    ob.notificaion=notif
    ob.date=datetime.today()
    ob.time=datetime.today()
    ob.eid=expert.objects.get(lid__id=request.session['lid'])
    print(ob)
    ob.save()
    messages.success(request, 'notification added')
    return HttpResponse('''<script>window.location='/notifications#about'</script>''')

@login_required(login_url='/')
def addtipcode(request):
    tp=request.POST['textarea']
    ob=tips()
    ob.tips=tp
    ob.date=datetime.today()
    ob.eid = expert.objects.get(lid__id=request.session['lid'])
    print(ob)
    ob.save()
    messages.success(request, 'tips added')
    return HttpResponse('''<script>window.location='/send_tips#about'</script>''')

@login_required(login_url='/')
def addsendrating(request):
    rt=request.POST['select2']
    rv=request.POST['textfield2']
    experts=request.POST['select']
    ob=rating()
    ob.rating=rt
    ob.review=rv
    ob.date=datetime.today()
    ob.uid=user.objects.get(lid__id=request.session['lid'])
    ob.eid=expert.objects.get(id=experts)
    ob.save()
    messages.success(request, 'rating send')
    return HttpResponse('''<script>window.location='/send_ratings#about'</script>''')

@login_required(login_url='/')
def notification_edit(request,id):
    ob = notification.objects.get(id=id)
    request.session['eid'] = id
    return render(request,'notification edit.html',{'val': ob})

@login_required(login_url='/')
def notieditcode(request):
    noti=request.POST['textfield']
    ob=notification()
    ob = notification.objects.get(id=request.session['eid'])
    ob.notificaion=noti
    ob.save()
    messages.success(request, 'edited')
    return HttpResponse('''<script>window.location='/notifications#about'</script>''')

@login_required(login_url='/')
def notidelcode(request,id):
    ob=notification.objects.get(id=id)
    ob.delete()
    messages.success(request, 'deleted')
    return HttpResponse('''<script>window.location='/notifications#about'</script>''')

@login_required(login_url='/')
def blockuser(request,id):
    ob=login.objects.get(id=id)
    ob.type='block'
    ob.save()
    messages.success(request, 'blocked')
    return HttpResponse('''<script>window.location='/block_unblock#about'</script>''')

@login_required(login_url='/')
def unblockuser(request,id):
    ob = login.objects.get(id=id)
    ob.type = 'expert'
    ob.save()
    messages.success(request, 'unblocked')
    return HttpResponse('''<script>window.location='/block_unblock#about'</script>''')

@login_required(login_url='/')
def addsenddoubt(request):
    dt=request.POST['textarea']
    experts = request.POST['select']
    ob = doubt()
    ob.doubt=dt
    ob.date = datetime.today()
    ob.uid = user.objects.get(lid__id=request.session['lid'])
    ob.eid = expert.objects.get(id=experts)
    ob.reply='pending'
    ob.save()
    messages.success(request, 'doubt send')
    return HttpResponse('''<script>window.location='/ask_doubt#about'</script>''')

@login_required(login_url='/')
def addcomplaintcode(request):
    cp = request.POST['textarea']
    ob = complaint()
    ob.notificaion=cp
    ob.date = datetime.today()
    ob.uid= user.objects.get(lid__id=request.session['lid'])
    ob.reply='pending'
    print(ob)
    ob.save()
    messages.success(request, 'complaint added')
    return HttpResponse('''<script>window.location='/send_complaint#about'</script>''')

@login_required(login_url='/')
def viewratingcode(request):
    experts = request.POST['select']
    obb= rating.objects.filter(eid__id=experts)
    ob = expert.objects.all()
    print(obb,"++",experts)
    return render(request, 'view rating.html', {'val':ob,'val1': obb})

@login_required(login_url='/')
def rep(request,id):
    ob=complaint.objects.get(id=id)
    request.session['cid']=id
    return render(request,'reply.html')

@login_required(login_url='/')
def complaintreply(request):
    creply=request.POST['textarea']
    ob=complaint.objects.get(id=request.session['cid'])
    ob.reply=creply
    ob.save()
    messages.success(request, 'Your Reply has been sent')
    return HttpResponse('''<script>window.location='/view_complaint#about'</script>''')

@login_required(login_url='/')
def repl(request,id):
    ob=doubt.objects.get(id=id)
    request.session['did']=id
    return render(request,'send doubt reply.html')

@login_required(login_url='/')
def doubtreply(request):
    dreply=request.POST['textarea']
    ob=doubt.objects.get(id=request.session['did'])
    ob.reply=dreply
    ob.save()
    messages.success(request, 'Replied')
    return HttpResponse('''<script>window.location='/view_doubts_and_reply#about'</script>''')


def logout(request):
    auth.logout(request)
    return  render(request,'index.html')

def forecasting(request):
    rr=gru_aave()
    x=[]
    y=[]
    for i in range(0,len(rr)):
        x.append(i+1)
        y.append(rr[i][0])
    return render(request,'foercasting.html',{"x":x,"y":y})

























