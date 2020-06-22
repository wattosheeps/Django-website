from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import SummaryForm
from .models import Summary
# Create your views here.
def cv_page(request):
    summary = Summary.objects.all()
    if summary.count() == 0:
        return render(request,'cv\cv_page.html',{'summary': ""})
    else:
        return render(request,'cv\cv_page.html',{'summary':summary[0]})
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
