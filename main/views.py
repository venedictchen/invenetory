from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Toshiba',
        'amount': '2',
        'description':'Flashdisk',
        'code':'2232',
        'price':'30000',
    }

    return render(request, "main.html", context)
