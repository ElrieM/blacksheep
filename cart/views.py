from django.shortcuts import render

def view_cart(request):
    """ View to renders products in the shopping cart """

    return render(request, 'cart/shopcart.html')
