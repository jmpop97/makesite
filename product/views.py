
from django.contrib.auth import models, login
from django.shortcuts import render, redirect
from .forms import CreateProductForm
# Create your views here.
def create_product(request):

    if request.method == "POST":  # 1
        form = CreateProductForm(request.POST)

        if form.is_valid():  # 2 # 5
            print("work")
            form.producter='test'
            form.save()
            return render(request,'base.html')
        return redirect('product/create_product.html')

    else:  # 3
        form = CreateProductForm()
    return render(request, 'product/create_product.html', {'form': form})  # 4
