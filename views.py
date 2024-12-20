from django.shortcuts import render


def get_start(request):
    return render(request, 'example.html')
