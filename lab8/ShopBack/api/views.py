from django.shortcuts import render  
from django.http.response import JsonResponse
from .models import Product, Category

#Create your views here
def product_list(request):
    products = Product.objects.all()
    json = [product.json() for product in products]
    return JsonResponse(json, safe = False)

def product_one(request, id):
    try:
        product = Product.objects.get(id = id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message':str(e)}, status = 400)
    return JsonResponse(product.json())

def category_list(request):
    categories = Category.objects.all()
    json = [category.json() for category in categories]
    return JsonResponse(json, safe = False)

def category_one(request, id):
    try:
        category = Category.objects.get(id = id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message':str(e)}, status = 400)
    return JsonResponse(category.json())