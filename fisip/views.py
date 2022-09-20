from django.shortcuts import render

# Create your views here.
def prodifisip(request):
    prodifisip = ["Administrasi Publik", "Ilmu Komunikasi", "Ilmu Politik"]
    

    konteks = {
        'prodifisip': prodifisip,

    }
    return render(request, 'indexfisip.html', konteks)
