from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

# Create your views here.
def cv_page(request):
    return render(request,'cv\cv_page.html')
