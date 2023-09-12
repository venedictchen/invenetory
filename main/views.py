from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Flashdisk',
        'amount': '2',
        'description':'Toshiba',
        'code':'2232',
        'price':'30000',
    }

    return render(request, "main.html", context)
