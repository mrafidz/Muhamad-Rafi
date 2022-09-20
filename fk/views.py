from django.shortcuts import render

# Create your views here.
def prodifk(request):
    prodifk = ["Farmasi", "Ilmu Keolahragaan", "Ilmu Gizi", "Kedokteran"]
    

    konteks = {
        'prodifk': prodifk,

    }
    return render(request, 'indexfk.html', konteks)