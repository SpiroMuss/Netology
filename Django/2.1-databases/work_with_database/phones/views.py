from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    all_phones = Phone.objects.all()

    match request.GET.get('sort', None):
        case 'name':
            phones = all_phones.order_by('name')
        case 'min_price':
            phones = all_phones.order_by('price')
        case 'max_price':
            phones = all_phones.order_by('price').reverse()
        case _:
            phones = all_phones

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
