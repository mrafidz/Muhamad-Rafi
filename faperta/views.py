from django.shortcuts import render

# Create your views here.
def prodifaperta(request):
    prodifaperta = ["Agribisnis", "Agroteknologi", "Ilmu Perikanan", "Teknologi Pangan"]

    konteks = {

        'prodifaperta' : prodifaperta
    }
    return render(request, 'indexfaperta.html', konteks)
