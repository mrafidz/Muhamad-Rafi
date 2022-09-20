from django.shortcuts import render

# Create your views here.
def prodifeb(request):
    prodifeb = ["Akuntansi", "Manajemen", "Ekonomi Pembangunan"]

    konteks = {

        'prodifeb' : prodifeb
    }
    return render(request, 'indexfeb.html', konteks)
