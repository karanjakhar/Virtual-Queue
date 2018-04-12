from django.shortcuts import render, redirect
from .forms import NameForm,staffform
from django.urls import reverse
from django.core.mail import send_mail
from cuqueue.models import details
import datetime
from django.contrib.auth import authenticate,login
from django.contrib import messages
import random,string


min_ch=0
q_no=0
hrs=8
def index(request):
    form = NameForm()
    return render(request, "cuqueue/home.html", {"form": form})


def get_data(request):
    global min_ch, q_no ,hrs
    min_ch = min_ch + 5
    if min_ch>59:
        hrs=hrs+1
        min_ch=0
    q_no += 1


    to_give_time = datetime.datetime.now()
    to_give_time = to_give_time.replace(hour=hrs, minute=min_ch, second=0, microsecond=0)
    form = NameForm(request.POST)
    save_it = form.save(commit=False)
    save_it.check=False
    save_it.given_time = to_give_time
    save_it.lineno = q_no

    subject = "Token Number"
    random_token=''.join(random.choice(string.ascii_uppercase+string.digits+string.ascii_lowercase)for _ in range(10))
    msg = "Token created successfully"+" and your Token Number is:" + random_token
    messages.success(request,msg)
    save_it.token=random_token
    from_email = 'cucoderarmy@gmail.com'
    to_email = [save_it.email, from_email]
    #send_mail(subject, msg, from_email, to_email)
    save_it.save()
    return redirect(reverse("index"))


def lists(request):
    get_it = details.objects.all()
    return render(request, "cuqueue/list.html", {"get_it": get_it})

def login_page(request):
    form=staffform()
    return render(request,"cuqueue/staff_login.html",{'form':form})

def staff(request):
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return lists(request)

    else:
        return redirect(reverse('login'))

def total(request):
    return render(request,'cuqueue/total.html')


def reset(request):
    global min_ch
    global q_no
    min_ch=0
    q_no=0
    data = details.objects.all()
    data.delete()
    return redirect('index')
