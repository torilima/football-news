from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406496391',
        'name': 'Abelyvia Tori Rebecca Silalahi',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)