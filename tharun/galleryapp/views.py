from django.shortcuts import render

def home(request):
    return render(request, 'galleryapp/home.html')

def menu(request):
    return render(request, 'galleryapp/menu.html')

def contact(request):
    return render(request, 'galleryapp/contact.html')

def admin_page(request):
    return render(request, 'galleryapp/admin.html')