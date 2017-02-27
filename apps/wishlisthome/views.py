from django.shortcuts import render,redirect
from django.contrib import messages

from ..wishlist.models  import User
from .models import Item

# Create your views here.
def index(request):
    user = User.objects.get(id=request.session['id'])
    print Item.objects.filter(likeditems=user)
    print Item.objects.all().exclude(user=user)

    context ={
        "user": User.objects.get(id=request.session["id"]),
        "items": Item.objects.all().exclude(user=user),
        "liked": Item.objects.filter(user=user)|Item.objects.filter(likeditems=user)
    }
    return render(request, "wishlisthome/index.html", context)

def create(request):
    return render(request, "wishlisthome/create.html")

def update(request):
    user = User.objects.get(id=request.session['id'])
    response = Item.objects.itemreview(request.POST,user)
    if not response['Status']:
        for error in response['errors']:
            messages    .error(request,error)
        return redirect("wishlist:my_w_create")
    else:
        return redirect('wishlist:my_w_home')

def add(request,id):
    Item.objects.get(id=id).likeditems.add(User.objects.get(id=request.session['id']))
    return redirect('wishlist:my_w_home')

def remove(request, id):
    Item.objects.get(id=id).likeditems.remove(User.objects.get(id=request.session['id']))
    return redirect('wishlist:my_w_home')

def delete(request, id):
    Item.objects.filter(id=id).delete()
    return redirect('wishlist:my_w_home')


def view(request, id):
    context ={
        "items": Item.objects.get(id=id)
    }
    return render(request,'wishlisthome/view.html', context)

def logout(request):
    del request.session['id']
    return redirect('home:my_home')
