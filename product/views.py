
from django.shortcuts import render, redirect
from .forms import CreateProductForm
# Create your views here.
def create_product(request):

    if request.method == "POST":  # 1
        form = CreateProductForm(request.POST)

        if form.is_valid():  # 2
            #new_user = models.User.objects.create_user(**form.cleaned_data)  # 5
            #login(request, new_user)
            pass
        return redirect('product/create_product.html')

    else:  # 3
        form = CreateProductForm()
    print(form)
    return render(request, 'product/create_product.html', {'form': form})  # 4
