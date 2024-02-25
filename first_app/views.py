from django.shortcuts import render
from . forms import studentForm
# Create your views here.
def home(req):
    if req.method == 'POST':
        form = studentForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = studentForm()
    return render(req,'first_app/home.html', {'form' : form})
