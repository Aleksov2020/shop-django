from django.shortcuts import render

from shop.models import Category, Item, ItemImage


def index(request):
    return render(request, 'index.html')


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def item_list(request, category_id: int):
    category = Category.objects.get(id=category_id)
    items = Item.objects.filter(category=category)
    return render(request, 'item_list.html', {'category': category, 'items': items})


def item_details(request, item_id: int):
    item = Item.objects.get(id=item_id)
    images = ItemImage.objects.filter(item=item)
    return render(request, 'item.html', {'item': item, 'images': images})
