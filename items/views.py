import logging
from django.shortcuts import render, HttpResponse, redirect
from .models import GroceryItems
from .models import Store


# Create your views here.

def store(request):
    dm = Store.objects.all()
    return render(request, "items/inventory.html", {'dm' : dm})

def inventory(request):
    data = GroceryItems.objects.all()
    return render(request, "items/inventory.html", {'data' : data})

def form(request):
    if request.method == "POST":
        dy = request.POST
        name = dy.get('name')
        wholesale_price = dy.get('wholesale_price')
        retail_price = dy.get('retail_price')
        country = dy.get('country')
        company = dy.get('company')
        entry_date = dy.get('entry_date')
        GroceryItems.objects.create(name=name, wholesale_price=wholesale_price, retail_price=retail_price, country=country,
                                    company=company, entry_date=entry_date)
        return redirect('/')

    return render(request, "items/form.html")

def edit_form(request, pk):
    if request.method == "POST":
        dy = request.POST
        name = dy.get('name')
        wholesale_price = dy.get('wholesale_price')
        retail_price = dy.get('retail_price')
        country = dy.get('country')
        company = dy.get('company')
        entry_date = dy.get('entry_date')
        dtu = GroceryItems.objects.get(id=pk)
        dtu.name = name
        dtu.wholesale_price = wholesale_price
        dtu.retail_price = retail_price
        dtu.country = country
        dtu.company = company
        dtu.entry_date = entry_date
        dtu.save()
        return redirect("/")
    mx = GroceryItems.objects.get(id=pk)
    return render(request, "items/edit_form.html", {'mx':mx})

def delete_form(request, pk):
    GroceryItems.objects.get(id=pk).delete()
    return redirect('/')
