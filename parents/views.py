from django.shortcuts import render, redirect

from parents.models import Entry
# Create your views here.


def home_page(request):
    if request.method == 'POST':
        new_entry_text = request.POST.get('parents_content', '')
        Entry.objects.create(what=new_entry_text)
        return redirect('/')

    return render(request, 'home.html', {'entries': Entry.objects.all()})
