from main.forms import ItemForm
from main.models import Item
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseNotFound,JsonResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import datetime 
import json


@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    context = {
        'nama_mahasiswa': request.user.username.capitalize(),
        'kelas': 'D',
        'items':items,
        'last_login':request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "create_item.html", context)

def show_html(request):
    items = Item.objects.filter(user=request.user)
    context = {'items':items}
    return render(request,"show_html.html",context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml",data),content_type = "application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json",data),content_type= "application/json")

def show_xml_by_id(request,id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml",data),content_type="application/xml")

def show_json_by_id(request,id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json",data),content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login',str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def increase_item_amount(request,id):
    item = Item.objects.get(id=id)
    item.amount +=1
    item.save()
    return HttpResponseRedirect(reverse('main:show_html'))

def decrease_item_amount(request,id):
    item = Item.objects.get(id=id)
    if item.amount>0:
        item.amount -=1
        item.save()
    return HttpResponseRedirect(reverse('main:show_html'))

def delete_item(request,id):
    item  = Item.objects.get(id=id)
    if item.user == request.user:
        item.delete()
        return HttpResponseRedirect(reverse('main:show_html'))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        code  = request.POST.get("code")
        price = request.POST.get("price")
        

        new_item = Item(user=user,name=name,amount=amount,code=code, description=description, price=price)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_item_ajax(request,id):
    if request.method == 'POST':
        item = Item.objects.get(id=id)
        if item.user == request.user:
            item.delete()
            return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def create_item_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_item = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = data["amount"],    
            description = data["description"],
            code = int(data["code"]),
            price = int(data["price"]),
        )

        new_item.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
def show_data_user(request):
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json",data),content_type= "application/json")