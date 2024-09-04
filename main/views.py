from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306172363',
        'name': 'Alano Davin Mandagi Awuy',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)