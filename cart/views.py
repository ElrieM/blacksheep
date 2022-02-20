# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

# Internal:
from products.models import Product

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def view_cart(request):
    """ View to renders products in the shopping cart """

    return render(request, 'cart/shopcart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request,
                    f'Added additional {product.name} size {size.upper()} to cart'
                )
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request,
                    f'Added {product.name} size {size.upper()} to cart')
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request,
                             f'Added additional {product.name} to cart')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Added {product.name} to cart')
        else:
            cart[item_id] = quantity
            messages.success(request, f'{product.name} added to cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def edit_cart(request, item_id):
    """ Adjusts quantity of items within the shopping cart """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(
                request,
                f'Updated quantity of {product.name} size {size.upper()} in cart'
            )
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(
                request,
                f'{product.name} size {size.upper()} removed from cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(
                request,
                f'Updated quantity of {product.name} size {size.upper()} in cart'
            )
        else:
            cart.pop(item_id)
            messages.success(
                request,
                f'{product.name} size {size.upper()} removed from cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove item from shopping cart """
    
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
                messages.success(
                    request,
                    f'Removed {product.name} size {size.upper()} from cart')
        else:
            cart.pop(item_id)
            messages.success(
                    request,
                    f'Removed {product.name} from cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
