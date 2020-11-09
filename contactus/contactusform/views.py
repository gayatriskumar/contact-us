from django.shortcuts import render
from .models import Contactusform
from django.views.generic import View
from django.http import HttpResponse
from .forms import Contactform
from django.http import JsonResponse

# Create your views here.

def contactusform_view(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponse('Thanks for contacting us!')
    #else:
        #form = Contactform()

    return render(request, 'contactusform/form.html')
