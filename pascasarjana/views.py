from django.shortcuts import render

# Create your views here.
def prodipascasarjana(request):
    prodipascasarjana = ["Pendidikan Matematika"]
    

    konteks = {
        'prodipascasarjana': prodipascasarjana,

    }
    return render(request, 'indexpascasarjana.html', konteks)
