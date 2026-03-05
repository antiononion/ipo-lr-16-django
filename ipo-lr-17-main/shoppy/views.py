from django.shortcuts import render

def hello_world(request):
    return render(request, 'index.html')
def shop(request):
    return render(request, 'shop.html')
def author(request):
    return render(request, 'author.html')
