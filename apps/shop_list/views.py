import stripe 

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .list import List
@login_required
def list_detail(request):
    list=List(request)
    remove_from_list = request.GET.get('remove_from_list', '')
    if remove_from_list:
            list.remove(remove_from_list)
            return redirect('list')
    return render(request, 'shop_list/list.html')