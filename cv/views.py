from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import SummaryForm
from .models import Summary
from .forms import QualificationForm
from .models import Qualification
from .models import Experience
from .forms import ExperienceForm
from .models import Skill
from .forms import SkillForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def cv_page(request):
    summary = Summary.objects.all()
    qualifications = Qualification.objects.filter(date_added__lte=timezone.now()).order_by('-date_end')
    work_experience = Experience.objects.filter(date_added__lte=timezone.now()).order_by('-date_end')
    skills = Skill.objects.all()
    if summary.count() == 0:
        return render(request,'cv/cv_page.html',{'summary': "",'qualifications':qualifications,'work_experience':work_experience,'skills':skills})
    else:
        return render(request,'cv/cv_page.html',{'summary':summary[0],'qualifications':qualifications,'work_experience':work_experience,'skills':skills})
@login_required
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
    return render(request,'cv/edit_summary.html', {'form': form})
@login_required   
def new_education(request):
    form = QualificationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.date_added = timezone.now()
            post.save()
            return redirect('cv_page')
    else:
        form = QualificationForm()
    return render(request, 'cv/new_education.html', {'form':form})
@login_required
def edit_education(request,pk):
    qualification = get_object_or_404(Qualification, pk=pk)
    if request.method == "POST":
        form = QualificationForm(request.POST, instance=qualification)
        if form.is_valid():
            post = form.save(commit=False)
            post.date_added = timezone.now()
            post.save()
            return redirect('cv_page')
    else:
        form = QualificationForm(instance=qualification)
    return render(request, 'cv/new_education.html', {'form': form})
@login_required
def new_experience(request):
    form = ExperienceForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.date_added = timezone.now()
            post.save()
            return redirect('cv_page')
    else:
        form = ExperienceForm()
    return render(request, 'cv/edit_experience.html', {'form':form})
@login_required
def edit_experience(request,pk):
    experience = get_object_or_404(Experience, pk=pk)
    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            post = form.save(commit=False)
            post.date_added = timezone.now()
            post.save()
            return redirect('cv_page')
    else:
        form = ExperienceForm(instance=experience)
    return render(request, 'cv/edit_experience.html', {'form': form})
@login_required
def new_skill(request):
    form = SkillForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.date_added = timezone.now()
            post.save()
            return redirect('cv_page')
    else:
        form = SkillForm()
    return render(request, 'cv/edit_skill.html', {'form':form})
@login_required
def edit_skill(request,pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            post = form.save(commit=False)
            post.date_added = timezone.now()
            post.save()
            return redirect('cv_page')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'cv/edit_skill.html', {'form': form})
@login_required
def experience_remove(request, pk):
    post = get_object_or_404(Experience, pk=pk)
    post.delete()
    return redirect('cv_page')
@login_required
def qualification_remove(request, pk):
    post = get_object_or_404(Qualification, pk=pk)
    post.delete()
    return redirect('cv_page')
@login_required
def skill_remove(request, pk):
    post = get_object_or_404(Skill, pk=pk)
    post.delete()
    return redirect('cv_page')