from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Toshiba',
        'amount': '2',
        'description':'Flashdisk',
    }

    return render(request, "main.html", context)
