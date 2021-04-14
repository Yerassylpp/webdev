from django.shortcuts import render
from .models import *
from django.http import JsonResponse
# Create your views here.

def company_list(request):
    companies = Company.objects.all()
    json = [company.json() for company in companies]
    return JsonResponse(json, safe=False)

def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message':str(e)}, status=400)
    return JsonResponse(company.json())

def company_vacancies(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message':str(e)},status=400)
    vacancies = [vacancy.json() for vacancy in company.vacancies.all()]
    return JsonResponse(vacancies, safe=False)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    json = [vacancy.json() for vacancy in vacancies]
    return JsonResponse(json, safe=False)

def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse(vacancy)

def top_ten(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    json = [vacancy.json() for vacancy in vacancies]
    return JsonResponse(json, safe=False)

