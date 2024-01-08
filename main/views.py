from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item, Category
from .forms import RegisterForm, ItemForm, EditItemForm,LoginForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.contrib import messages
from .models import CustomUser

# Create your views here.
def index(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, 'main/index.html', {
        'items':items,
    })
def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request,email = email, password = password)

            if user is not None:
                login(request,user)
                return redirect('main:index')
            else:
                messages.error(request, 'Invalid email or password.')



    return render(request, 'registration/login.html', {
        'form':form
    })


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.create_user(form.cleaned_data['email'], form.cleaned_data['password'])
            login(request,user)
            
            return redirect("main:index")
    else:
        form = RegisterForm()
    
    return render(request, 'registration/signup.html', {
        'form':form
    })
@login_required
def logout_view(request):
    logout(request)
    return redirect("main:index")

@login_required
def profile(request):
    items = Item.objects.filter(seller = request.user)
    return render(request, 'main/profile.html', {
        'user': request.user,
        'items':items,
    })


@login_required
def additem(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit = False)
            item.seller = request.user
            item.save()

            return redirect('main:profile')
    else:
        form = ItemForm()

    return render(request, 'main/additem.html', {
        'form' : form,
    })

def viewitem(request, pk):
    item = get_object_or_404(Item,pk= pk)
    return render(request, 'main/viewitem.html', {
        'item':item
        })

@login_required
def edititem(request,pk):
    item = get_object_or_404(Item, pk = pk)
    if request.method == "POST":
        form = EditItemForm(request.POST,request.FILES,instance = item)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = EditItemForm(instance = item)

@login_required
def deleteitem(request, pk):
    item = get_object_or_404(Item, pk = pk)
    item.delete()

    return redirect('main:index')

def viewcart(request):
    cart_item_ids = request.session.get('cartids', [])
    if cart_item_ids:
        cart_items = Item.objects.filter(pk__in =cart_item_ids)
    else:
        cart_items = []
    totalprice = 0
    for item in cart_items:
        totalprice += item.price
    print(cart_items)
    return render(request, 'main/cart.html', {
        'items':cart_items,
        'price':totalprice
    })

def addtocart(request, pk):
    # item = get_object_or_404(Item, pk = pk)

    # cart_items = request.session.get('cartitems', [])
    
    # if cart_items:
    #     cart_items.append(item)
    # else:
    #     cart_items = [item]
    # request.session['cartitems'] = cart_items
    # request.session.modified = True


    cart_ids = request.session.get('cartids', [])
    cart_ids.append(pk)
    request.session['cartids'] = cart_ids
    request.session.modified = True
    print(request.session['cartids'])
    return redirect('main:viewcart')

class ItemListView(ListView):
    model = Item
    template_name = 'main/index.html'
    context_object_name = 'items'   
    paginate_by = 3
    def get_queryset(self):
        return Item.objects.all()