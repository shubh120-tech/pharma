from django.shortcuts import render
from .models import Users
from .models import Medicines

# Create your views here.
Medicine = Medicines.objects.all()
def index(request):







    return render(request,'MathuraMed/index.html',{'medicine': Medicine})


def shop_single(request,medicine):
    Medicine = Medicines.objects.filter(MedicineName=medicine)
    return render(request,'MathuraMed/shop-single.html',{'medicine': Medicine,'name':medicine})

def about(request):
    return render(request,'MathuraMed/about.html')

def cart(request,medname):
    Medicine = Medicines.objects.filter(MedicineName=medname)
    return render(request,'MathuraMed/cart.html',{'medicine': Medicine})

def checkout(request):
    return render(request,'MathuraMed/checkout.html')

def shop(request):
        return render(request, 'MathuraMed/shop.html',{'medicine': Medicine})


def thankyou(request):
    return render(request,'MathuraMed/thankyou.html')