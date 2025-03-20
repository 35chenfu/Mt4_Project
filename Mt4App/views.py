# Create your views here.
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json

from .models import Book

# 新增图书
@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(title=request.GET.get('title'))
        book.save()
        response['msg'] = 'success'
        response['error_code'] = '0'
    except Exception as e:
        response['msg'] = str(e)
        response['error_code'] = '1'

    return JsonResponse(response)



# 显示图书列表
@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)