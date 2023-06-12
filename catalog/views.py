from django.shortcuts import render, redirect
#from django.http import HttpResponse
from . import models
from . import handlers
# Create your views here.
def main_page(request):
    all_categories = models.Category.objects.all()
    all_products = models.Product.objects.all()

    #получить переменную из фронта если оно есть
    search_value_from_front = request.GET.get('pr')
    if search_value_from_front:
        all_products = models.Product.objects.filter(name__contains=search_value_from_front)
    # показ контента из html файла
    # передача переменных из бека на фронт
    context = {'all_categories': all_categories,'all_products': all_products}
    return render(request, 'index.html', context)

def contact_page(request):
   return HttpResponse('My name alex')

def about_page(request):
    return render(request, 'about.html')

#получить продукты из конкретной категории
def get_category_products(request, pk):
    # Получить все товары из конкретной категории
    exact_category_products = models.Product.objects.filter(category_name__id=pk)

    context = {'category_products': exact_category_products}

    return render(request, 'category.html', context)

def get_exact_products(request, name, pk):
    exact_product = models.Product.objects.get(id=pk, name=name)

    context = {'product': exact_product}

    return render(request, 'product.html', context)

def add_pr_to_cart(request, pk):
    quantity = request.POST.get('pr_count')
    product_to_add = models.Product.objects.get(id=pk)
    models.UserCart.objects.create(user_id=request.user.id,
                                   user_product=product_to_add,
                                   user_product_quantity=quantity)
    return redirect('/')

def get_user_cart(request):
    products_from_cart = models.UserCart.objects.filter(user_id=request.user.id)
    context = {'cart_products': products_from_cart}
    return  render(request, 'user_cart.html', context)

def complere_order(request):
    # Получаем корзину пользователя
    user_cart= models.UserCart.objects.filter(user_id=request.user.id)
    if request.method == "POST":
        result_message = 'Новый зака(из Сайта) \n\n'
    # Счетчик для подсчета итога корзины
        total_for_all_cart = 0
        for cart in user_cart:
            result_message += f'Название товара:{cart.user_product}\n' \
                        f'Колличество: {cart.user_product_quantity}'
        handlers.bot.send_message(-738866598, result_message)
        user_cart.delete()
        return  redirect('/')
    return render(request, 'user_cart.html', {'user_cart': user_cart})

def delete_from_user_cart(request):
    user_cart = models.UserCart.objects.filter(user_id=request.user.id, user_product=pk)
    user_cart.delete()
    return redirect('/user_cart')