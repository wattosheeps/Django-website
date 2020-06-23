from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import SummaryForm
from .models import Summary
from .forms import QualificationForm
from .models import Qualification
# Create your views here.
def cv_page(request):
    summary = Summary.objects.all()
    qualifications = Qualification.objects.filter(date_added__lte=timezone.now()).order_by('date_added')
    if summary.count() == 0:
        return render(request,'cv\cv_page.html',{'summary': "",'qualifications':qualifications})
    else:
        return render(request,'cv\cv_page.html',{'summary':summary[0],'qualifications':qualifications})
def edit_summary(request):
    post = get_object_or_404(Summary, pk=1)
    if request.method == "POST":
        form = SummaryForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.last_edited = timezone.now()
            post.save()
            return redirect('cv_page')
    else:
        form = SummaryForm(instance=post)
    return render(request,'cv\edit_summary.html', {'form': form})
    
def education_overview(request):
    qualifications = Qualification.objects.filter(date_added__lte=timezone.now()).order_by('date_added')
    return render(request,'cv\education_overview.html',{'qualifications':qualifications})
def new_education(request):
    form = QualificationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.date_added = timezone.now()
            post.save()
            return redirect('education_overview')
    else:
        form = QualificationForm()
    return render(request, 'cv\\new_education.html', {'form':form})
def edit_education(request,pk):
    qualification = get_object_or_404(Qualification, pk=pk)
    if request.method == "POST":
        form = QualificationForm(request.POST, instance=qualification)
        if form.is_valid():
            post = form.save(commit=False)
            post.date_added = timezone.now()
            post.save()
            return redirect('education_overview')
    else:
        form = QualificationForm(instance=qualification)
    return render(request, 'cv\\new_education.html', {'form': form})