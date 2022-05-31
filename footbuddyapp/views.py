from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Room,  Message, Topic
# from .forms import RoomForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    rooms = Room.objects.all()
    user = User.objects.all()
    message = Message.objects.all()
    topic = Topic.objects.all()
    
    


    

    context = {'rooms':rooms, 'user':user, 'topic':topic, 'message':message}
    return render(request, 'index.html', context)

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1)
                return redirect('login')

    return render(request, 'signup.html')
    

        

    return render(request, 'signup.html')

def logoutUser(request):
    logout(request)
    return redirect('home')

def room(request, pk):
    room = Room.objects.get(id=pk)
    rooms = Room.objects.all()
    topic = room.topic_set.all()
    topics = Topic.objects.all()
    # topicx = Topic.objects.get(id=pk)
    # message_count = Topic.objects.get(id=pk).message_set.all()
    

    context = {'topics':topics,'rooms':rooms,
     'room':room, 'topic':topic,  }
    return render(request, 'room.html', context )

def topic(request, pk):
    topics = Topic.objects.get(id=pk)
    topic_messages = topics.message_set.all()
    messages = Message.objects.all()
    topic = Topic.objects.all()
    if request.method == 'POST':
        message = Message.objects.create(
            sender = request.user,
            topic = topics,
            body = request.POST.get('message')
        )
        message.save()
        return redirect('topic', pk=topics.id)

    context = {'topic':topic,'topics':topics, 'messages':messages, 'topic_messages':topic_messages}
    return render(request, 'topic.html', context)

def createtopic(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        topic = Topic.objects.create(
            creator = request.user,
            room = room,
            title = request.POST.get('title-topic'),
            body = request.POST.get('body-topic')
        )
        topic.save()
        return redirect('room', pk=room.id)
        

    return render(request, 'create-topic.html')

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    topic = Topic.objects.get(id=pk)
    user_topic = user.topic_set.all()
    topicx = Topic.objects.all()
    roomx = Room.objects.all()

    context = {'user_topic':user_topic, 'topicx':topicx, 'roomx':roomx, 'topic':topic}
    return render(request, 'profile.html', context)