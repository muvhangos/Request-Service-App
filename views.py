from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ServiceRequest

def index(request):
    requests = ServiceRequest.objects.order_by('-created_at')
    return render(request, 'index.html', {'requests': requests})

def create_request(request):
    if request.method == 'POST':
        data = request.POST
        ServiceRequest.objects.create(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            description=data['description']
        )
        return redirect('/')