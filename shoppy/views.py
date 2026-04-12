from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Element, Cart, Category, Owner
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def hello_world(request):
    return render(request, 'index.html')


def shop(request):
    all_products = Product.objects.all() 
    return render(request, 'shop.html',{'products': all_products})


def author(request):
    return render(request, 'author.html')


def product_info(request, pk):
    # Достаем товар по его первичному ключу (pk)
    product = get_object_or_404(Product, pk=pk)
    # Отправляем данные в шаблон
    return render(request, 'product_info.html', {'product': product})


def get_customer_cart(request):
    # Заменяем owner на user, так как это имя поля в твоей модели Cart
    cart, created = Cart.objects.get_or_create(user=request.user)
    return cart



@login_required
def cart_add(request, product_id):
    cart = get_customer_cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    # Ищем, есть ли уже этот товар в корзине (Element)
    element, created = Element.objects.get_or_create(
        cart=cart, 
        product=product,
        defaults={'number': 1} # Если создаем новый, ставим 1 шт.
    )
    
    if not created:
        element.number += 1
        element.save() # Сработает твоя проверка clean() на остаток склада
        
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart = get_customer_cart(request)
    # Получаем все элементы этой корзины
    elements = Element.objects.filter(cart=cart)
    
    # Считаем общую сумму, используя твой метод cost()
    total_price = sum(item.cost() for item in elements)
    
    return render(request, 'cart.html', {
        'cart': cart, 
        'elements': elements, 
        'total_price': total_price
    })

@login_required
def cart_remove(request, item_id):
    # Заменяем cart__owner на cart__user
    element = get_object_or_404(Element, id=item_id, cart__user=request.user)
    element.delete()
    return redirect('cart_detail')

@login_required
def cart_update(request, item_id):
    element = get_object_or_404(Element, id=item_id, cart__user=request.user)
    if request.method == 'POST':
        new_number = int(request.POST.get('number', 1))
        if new_number > 0:
            element.number = new_number
            element.save() # Снова сработает твоя валидация склада
        else:
            element.delete()
    return redirect('cart_detail')


def product_list(request):
    products = Product.objects.all()

    # 1. Поиск по названию (title) или описанию (description)
    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    # 2. Фильтрация по категории
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)

    # 3. Фильтрация по производителю (owner)
    owner_id = request.GET.get('owner')
    if owner_id:
        products = products.filter(owner_id=owner_id)

    # Достаем списки для выпадающих меню в шаблоне
    categories = Category.objects.all()
    owners = Owner.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'owners': owners,
    }
    return render(request, 'shop/product_list.html', context)