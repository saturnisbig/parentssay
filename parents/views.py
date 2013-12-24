from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home_page(request):
    #return HttpResponse('<html><title>ParentsSay</title></html>')
    parents_content = request.POST.get('parents_content', '')
    print(parents_content)
    if parents_content:
        date = datetime.now().strftime('%Y-%m-%d')
        content = (date + ' ' + request.POST.get('role') + ':' +
                   request.POST.get('parents_content', '') + '@' +
                   request.POST.get('baby_name', ''))
    else:
        content = ''
    return render(request, 'home.html', {
        'new_content_text': content,
    })
